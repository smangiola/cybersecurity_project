import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "bob123", hashlib.sha256("banana1".encode()).hexdigest()
username2, password2 = "susie234", hashlib.sha256("fruit3".encode()).hexdigest()
username3, password3 = "lily567", hashlib.sha256("tiger67".encode()).hexdigest()
username4, password4 = "bill890", hashlib.sha256("rainbow101".encode()).hexdigest()
username5, password5 = "ariana45", hashlib.sha256("blueberry5".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username5, password5))

conn.commit()









