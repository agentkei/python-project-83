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
    return dict(url)


def get_by_name(name):
    conn = get_db()
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('SELECT * FROM urls where name = (%s)', (name,))
        url = curs.fetchone()
    conn.commit()
    conn.close()
    return url


def add_to_check_list(url_id, status_code=None, h1='',
                      title='', description=''):
    conn = get_db()
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('INSERT INTO url_checks (url_id, status_code, h1, title,\
                      description, created_at)\
                      VALUES (%s, %s, %s, %s, %s, %s);',
                     (url_id, status_code, h1, title, description,
                      date.today().strftime('%Y-%m-%d')))
    conn.commit()
    conn.close()


def get_check_list(url_id):
    conn = get_db()
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('SELECT * FROM url_checks where url_id = (%s)\
                     ORDER BY id DESC', (url_id,))
        url_checks = curs.fetchall()
    conn.close()
    return url_checks


def get_url_last_check():
    conn = get_db()
    with conn.cursor(cursor_factory=DictCursor) as curs:
        curs.execute('''SELECT u.id AS site_id,
                     u.name AS site_name,
                     MAX(uc.created_at) AS last_check_date,
                     MAX(uc.status_code) AS last_status_code
                     FROM urls u
                     LEFT JOIN url_checks uc ON u.id = uc.url_id
                     GROUP BY u.id, u.name
                     ORDER BY u.id DESC;''')
        last_checks_list = curs.fetchall()
    conn.close()
    return last_checks_list
