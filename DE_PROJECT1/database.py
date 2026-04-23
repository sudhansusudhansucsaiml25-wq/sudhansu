import sqlite3

conn = sqlite3.connect("vocab.db")
cursor = conn.cursor()

def setup():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS words (
        word TEXT PRIMARY KEY,
        definition TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS performance (
        word TEXT,
        correct INTEGER,
        attempts INTEGER
    )
    """)

    conn.commit()

def insert_word(word, definition):
    cursor.execute("INSERT OR IGNORE INTO words VALUES (?, ?)", (word, definition))
    conn.commit()

def update_perf(word, correct):
    cursor.execute("SELECT * FROM performance WHERE word=?", (word,))
    row = cursor.fetchone()

    if row:
        attempts = row[2] + 1
        correct_count = row[1] + (1 if correct else 0)
        cursor.execute("UPDATE performance SET correct=?, attempts=? WHERE word=?",
                       (correct_count, attempts, word))
    else:
        cursor.execute("INSERT INTO performance VALUES (?, ?, ?)",
                       (word, 1 if correct else 0, 1))

    conn.commit()

def get_weak_words():
    cursor.execute("SELECT word, correct, attempts FROM performance")
    data = cursor.fetchall()

    return [w for w,c,a in data if a>0 and c/a < 0.5]