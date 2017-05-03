# initialze database

import sqlite3

# create statement
create_statement = """
CREATE TABLE IF NOT EXISTS books (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL DEFAULT '',
    author TEXT NOT NULL DEFAULT '',
    tags TEXT NOT NULL DEFAULT '',
    created TEXT NOT NULL DEFAULT datetime('now'),
    updated TEXT NOT NULL DEFAULT datetime('now'),
    image1 TEXT NOT NULL DEFAULT '',
    image2 TEXT NOT NULL DEFAULT '',
    image3 TEXT NOT NULL DEFAULT '',
    image4 TEXT NOT NULL DEFAULT '',
)
"""[1:-1]
conn = sqlite3.connection("")

# create default table
conn.execute(create_statement)
conn.commit()
