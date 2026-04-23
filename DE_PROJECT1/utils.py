import pandas as pd
import requests
import csv
import os

def load_csv():
    return pd.read_csv("Vocabulary.csv")

def fetch_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        try:
            definition = data[0]['meanings'][0]['definitions'][0]['definition']
            return definition
        except:
            return None
    return None

def validate(word, definition):
    return word and definition

#  WRONG WORD SAVE
def save_wrong_word(word, definition):
    file_exists = os.path.isfile("wrong_words.csv")

    with open("wrong_words.csv", "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Word", "Definition"])

        writer.writerow([word, definition])