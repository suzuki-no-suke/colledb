import sqlite3
con = sqlite3.connect('test.db')
con.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, specified_id INTEGER)')
con.execute('INSERT INTO test (specified_id) VALUES (3)')
con.execute('INSERT INTO test (specified_id) VALUES (11)')
con.execute('INSERT INTO test (specified_id) VALUES (1)')
con.commit()
