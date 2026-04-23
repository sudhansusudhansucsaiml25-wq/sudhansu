import random
from database import get_weak_words

def generate_quiz(all_words):
    weak = get_weak_words()

    quiz = []

    # pehle weak words
    quiz.extend(weak[:5])

    # baaki random
    remaining = list(set(all_words) - set(quiz))
    quiz.extend(random.sample(remaining, min(10-len(quiz), len(remaining))))

    return quiz