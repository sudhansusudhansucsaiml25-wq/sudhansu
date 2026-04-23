from utils import load_csv, fetch_word, validate, save_wrong_word
from database import setup, insert_word, update_perf, cursor
from quiz import generate_quiz

def main():
    setup()

    df = load_csv()

    #  Step 1: store words
    for word in df['Word']:
        definition = fetch_word(word)

        if validate(word, definition):
            insert_word(word, definition)

    #  Step 2: quiz
    words = df['Word'].tolist()
    quiz = generate_quiz(words)

    print("\n DAILY QUIZ ")
    print("="*25)

    score = 0

    for word in quiz:
        cursor.execute("SELECT definition FROM words WHERE word=?", (word,))
        result = cursor.fetchone()

        if result:
            definition = result[0]
        else:
            continue

        print(f"\n Word: {word}")
        user = input("Apna answer likh (ya 'skip'): ")

        if user.lower() in definition.lower():
            print(" Correct")
            score += 1
            update_perf(word, True)
        else:
            print(" Wrong")
            print(f" Correct Meaning: {definition}")

            update_perf(word, False)
            save_wrong_word(word, definition)   #  main feature

    print(f"\n Final Score: {score}/10")

if __name__ == "__main__":
    main()