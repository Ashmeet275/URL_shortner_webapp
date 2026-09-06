import sqlite3

DB_NAME = "database.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS URLS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ORIGINAL_URL TEXT NOT NULL,
            SHORT_CODE TEXT UNIQUE NOT NULL,
            VISIT_COUNT INTEGER DEFAULT 0
            )
        ''')

def insert_url(origina_url, short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            INSERT INTO URLS (ORIGINAL_URL, SHORT_CODE)
            VALUES(?,?)
        ''',(origina_url, short_code))

def get_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('''
            SELECT * FROM URLS WHERE SHORT_CODE = ?
        ''',(short_code,))
        return cur.fetchone()

def visit_count(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            UPDATE URLS
            SET VISIT_COUNT = VISIT_COUNT + 1
            WHERE SHORT_CODE = ?
        ''',(short_code,))

def get_allurls():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.execute('''
            SELECT ORIGINAL_URL, SHORT_CODE, VISIT_COUNT 
            FROM URLS
            ORDER BY ID DESC
        ''')
        return cur.fetchall()

def del_url(short_code):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('DELETE FROM URLS WHERE SHORT_CODE = ?',
                     (short_code,))
