import sqlite3

def create_db():
    con=sqlite3.connect(database="covid_db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS patient(pid  INTEGER PRIMARY KEY AUTOINCREMENT,name text,Doctor text,Hospital text,Gender text ,Contact text,Swap_NO text ,Date text,Report text)")
    con.commit()
    con.close()

create_db()