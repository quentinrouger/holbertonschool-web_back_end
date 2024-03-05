#!/usr/bin/env python3
"""Route module for the API"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """Return index.html"""
    return render_template('1-index.html')


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


if __name__ == '__main__':
    app.run()
