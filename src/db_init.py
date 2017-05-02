# initialze database

import sqlite3

# create statement
create_statement = """
CREATE TABLE IF NOT EXISTS books (

)
"""[1:-1]
conn = sqlite3.connection("")
