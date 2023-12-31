#!/usr/bin/env python3
"""
App module
"""
from flask import Flask, request, render_template, g
from flask_babel import Babel
from typing import Union


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Available languages class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)


def get_user():
    """This func returns user dict if ID can be found"""
    try:
        return users.get(int(request.args.get('login_as')))
    except Exception:
        return None


@babel.localeselector
def get_locale() -> Union[str, None]:
    """ This func gets locale from request"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """ This func finds user and sets as global on flask.g.user """
    g.user = get_user()


@app.route('/')
def index() -> str:
    """ Index """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
