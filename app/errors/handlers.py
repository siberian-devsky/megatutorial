#!.venv/bin/bash

from flask import render_template, session
from app import db
from app.errors import bp

@bp.app_errorhandler
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def server_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500