#!/usr/bin/env python3
"""Route module for the API"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user(user_id):
    """Get user information based on user ID"""
    return users.get(user_id)


@app.before_request
def before_request():
    """Set user information in flask.g.user"""
    user_id = request.args.get("login_as")
    g.user = get_user(int(user_id)) if user_id and user_id.isdigit() else None


@babel.localeselector
def get_locale():
    """Get locale"""
    if 'locale' in request.args:
        requested_locale = request.args['locale']

        if requested_locale in app.config['LANGUAGES']:
            return requested_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Return index.html"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
