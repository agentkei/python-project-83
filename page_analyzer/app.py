#!/usr/bin/env python3
from flask import (
    Flask,
    render_template,
    request,
    flash,
    url_for,
    redirect,
    get_flashed_messages
)
from dotenv import load_dotenv
import os
from page_analyzer.validator import validate
from page_analyzer.url_formatter import formate


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')


from page_analyzer.conn_base import ( # noqa
    add_to_url_list,
    get_by_id,
    get_by_name
)


@app.route("/")
def main():
    return render_template('main.html')


@app.route('/urls', methods=['POST'])
def add_new_url():
    new_url = request.form.to_dict()
    formatted_url = formate(new_url['url'])
    errors = validate(formatted_url)
    same_url = get_by_name(formatted_url)

    if errors:
        if 'without_url' in errors:
            flash(errors['without_url'], 'alert-warning')
        elif 'incorrect_url' in errors:
            flash(errors['incorrect_url'], 'alert-danger')
        return render_template('main.html', new_url=new_url, errors=errors), 422

    if same_url:
        added_url = same_url
        id = added_url['id']
        flash('Страница уже существует', 'alert-info')
        return redirect(url_for('get_url', id=id))

    new_url['name'] = formatted_url
    add_to_url_list(new_url)
    flash('Страница успешно добавлена', 'alert-success')
    added_url = get_by_name(formatted_url)
    id = added_url['id']
    return redirect(url_for('get_url', id=id))


@app.get('/urls/<int:id>')
def get_url(id):
    url = get_by_id(id)
    print(url)
    # checks = get_check_list(id)
    errors = get_flashed_messages(with_categories=True)
    return render_template('url_id.html', url=url, errors=errors)


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('error.html', message='Страница не найдена'), 404


# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('error.html',
#                            message='Внутренняя ошибка сервера'), 500
