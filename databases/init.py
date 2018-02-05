import sqlite3


def init_db(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    sql = """
        DROP TABLE IF EXISTS author;
        CREATE TABLE author (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(256) );
        DROP TABLE IF EXISTS book;
        CREATE TABLE book (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(256) );
        DROP TABLE IF EXISTS author_book;
        CREATE TABLE author_book (author_id INTEGER, book_id INTEGER);
        INSERT INTO author VALUES(1, 'James Hetfield');
        INSERT INTO author VALUES(2, 'Lars Ulrich');
        INSERT INTO book VALUES (1, 'Ride the Lightning');
        INSERT INTO book VALUES (2, 'Master of Puppets');
        INSERT INTO book VALUES (3, '…And Justice for All');
        INSERT INTO book VALUES (4, 'Hardwired...To Self-Destruct');
        INSERT INTO author_book VALUES(1,1);
        INSERT INTO author_book VALUES(1,2);
        INSERT INTO author_book VALUES(2,3);
        INSERT INTO author_book VALUES(2,4);"""
    for s in sql.split('\n'):
        cur.execute(s)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    init_db("myLibrary.db")

