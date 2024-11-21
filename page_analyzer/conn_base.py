from datetime import date
import psycopg2
from flask import current_app
from psycopg2.extras import DictCursor


def get_db():
    return psycopg2.connect(current_app.config['DATABASE_URL'])


def add_to_url_list(new_url):
    conn = get_db()
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('INSERT INTO urls (name, created_at) VALUES (%s, %s);',
                     (new_url['name'], date.today().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()


def get_by_id(id):
    conn = get_db()
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('SELECT * FROM urls where id = (%s)', (id,))
        url = curs.fetchone()
    conn.commit()
    conn.close()
    return url


def get_by_name(name):
    conn = get_db()
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('SELECT * FROM urls where name = (%s)', (name,))
        url = curs.fetchone()
    conn.commit()
    conn.close()
    return url


# def get_check_list(url_id):
#     conn = get_db()
#     with conn.cursor(cursor_factory=DictCursor) as curs:
#         curs.execute('SELECT * FROM url_checks where url_id = (%s)\
#                      ORDER BY id DESC', (url_id,))
#         url_checks = curs.fetchall()
#     conn.close()
#     return url_checks
