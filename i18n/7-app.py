#!/usr/bin/env python3
"""Route module for the API"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


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


def get_user():
    """Get user information based on user ID"""
    try:
        user_id = int(request.args.get("login_as"))
        if user_id in users.keys():
            return users[user_id]
    except Exception:
        return None


@app.before_request
def before_request():
    """Set user information in flask.g.user"""
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale():
    """Get locale"""
    if 'locale' in request.args:
        requested_locale = request.args['locale']

        if requested_locale in app.config['LANGUAGES']:
            return requested_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Returns a URL-provided or user time zone"""
    timezone_url = request.args.get("timezone")
    try:
        if not timezone_url:
            timezone = g.user["timezone"]
        else:
            timezone = timezone_url
        return timezone
    except (pytz.exceptions.UnknownTimeZoneError, Exception):
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """Return index.html"""
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
