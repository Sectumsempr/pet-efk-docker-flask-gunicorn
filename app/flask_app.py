import logging
from typing import Tuple
from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route('/one')
def first() -> Tuple[str, int]:
    return 'HTTP 201 Created', 201


@app.route('/two')
def second() -> Tuple[str, int]:
    return 'HTTP 202 Accepted', 202


@app.route('/three')
def third() -> Tuple[str, int]:
    return 'HTTP 203 Non-Authoritative Information', 203


@app.route('/four')
def fourth() -> Tuple[str, int]:
    return 'HTTP 204 No Content', 204


@app.route('/five')
def fifth() -> Tuple[str, int]:
    return 'HTTP 205 Reset Content', 205


@app.route('/error')
def oops() -> Tuple[str, int]:
    return 'HTTP 500 Internal Server Error', 500


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
