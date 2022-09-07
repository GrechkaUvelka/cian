import sqlite3


def connect(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS offers(
        offer_id INTEGER,
        price INTEGER,
        room_count TEXT,
        total_area INTEGER,
        floor_num TEXT,
        date TEXT,
        parse_date TEXT,
        address TEXT,
        url TEXT,
        PRIMARY KEY("offer_id")
    )""")
    conn.commit()
    conn.close()


def write_db(values_to_db):
    conn = sqlite3.connect('offers.db')
    cursor = conn.cursor()
    cursor.executemany("""INSERT OR IGNORE INTO offers VALUES(?,?,?,?,?,?,?,?,?);""", values_to_db)
    conn.commit()

def parse_url():
    conn = sqlite3.connect('offers.db')
    cursor = conn.cursor()
    cursor.execute(""" SELECT url FROM offers""")
    urls = cursor.fetchall()
    return urls
