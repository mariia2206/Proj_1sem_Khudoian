import sqlite3 as sq
info_users = [
    (1, 'Алексей', 1, 22, 1000),
    (2, 'Миша', 1, 19, 800),
    (3, 'Сергей', 1, 19, 900),
    (4, 'Мария', 2, 18, 1500),
    (5, 'Александр', 1, 20, 1100),
]

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)
    #cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
sex INTEGER NOT NULL DEFAULT 1, old INTEGER,
score INTEGER
)""")
