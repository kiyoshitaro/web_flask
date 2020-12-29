import sqlite3
conn = sqlite3.connect("quotes.db")

# To open sql file 
curr = conn.cursor()

curr.execute("""create table quotes_db(
    title text,
    author text,
    tag text)""")

conn.commit()
conn.close()