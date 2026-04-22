import csv
import sqlite3
import random
import requests
from datetime import date

# -------- DATABASE --------
conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS quiz (
    word TEXT,
    definition TEXT,
    example TEXT,
    date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS performance (
    word TEXT,
    correct INTEGER,
    wrong INTEGER
)
""")

conn.commit()

# -------- READ CSV --------
def read_csv():
    words = []
    with open("Vocabulary.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["word"]:
                words.append(row)
    return words

# -------- API CALL --------
def get_meaning(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        res = requests.get(url)
        data = res.json()

        definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        example = data[0]["meanings"][0]["definitions"][0].get("example", "No example")

        return definition, example
    except:
        return "No definition", "No example"

# -------- QUIZ GENERATE --------
def generate_quiz(words):
    return random.sample(words, min(10, len(words)))

# -------- SAVE QUIZ --------
def save_quiz(word, definition, example):
    today = str(date.today())
    cursor.execute("INSERT INTO quiz VALUES (?, ?, ?, ?)", 
                   (word, definition, example, today))
    conn.commit()

# -------- QUIZ RUN --------
def run_quiz():
    words = read_csv()
    quiz_words = generate_quiz(words)

    score = 0

    for item in quiz_words:
        word = item["word"]
        definition, example = get_meaning(word)

        print(f"\nWord: {word}")
        print(f"Definition: {definition}")

        ans = input("Did you know this word? (y/n): ")

        if ans == "y":
            score += 1
            update_performance(word, True)
        else:
            print(f"Example: {example}")
            update_performance(word, False)

        save_quiz(word, definition, example)

    print(f"\nYour Score: {score}/10")

# -------- PERFORMANCE --------
def update_performance(word, correct):
    cursor.execute("SELECT * FROM performance WHERE word=?", (word,))
    data = cursor.fetchone()

    if data:
        if correct:
            cursor.execute("UPDATE performance SET correct=correct+1 WHERE word=?", (word,))
        else:
            cursor.execute("UPDATE performance SET wrong=wrong+1 WHERE word=?", (word,))
    else:
        if correct:
            cursor.execute("INSERT INTO performance VALUES (?,1,0)", (word,))
        else:
            cursor.execute("INSERT INTO performance VALUES (?,0,1)", (word,))

    conn.commit()

# -------- REVIEW MODE --------
def review_mode():
    print("\n--- Weak Words ---")
    cursor.execute("SELECT word FROM performance WHERE wrong > correct")
    words = cursor.fetchall()

    for w in words:
        print(w[0])

# -------- MAIN --------
print("1. Start Quiz")
print("2. Review Weak Words")

choice = input("Enter choice: ")

if choice == "1":
    run_quiz()
elif choice == "2":
    review_mode()

conn.close()