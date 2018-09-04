#!/usr/bin/env python

from flask import (Flask, render_template)
from models import user
from models.user import User
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)


@app.route('/')
def index():
    user.initialize()
    john_doe = User.select().where(
        User.email == "john@doe.com"
    ).get()
    return render_template('invoice.html', user=john_doe)


if __name__ == '__main__':
    app.run(**app_start_config)
