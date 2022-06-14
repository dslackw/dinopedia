#!/usr/bin/env python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiate database object
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_folder='views/static')
    return app
