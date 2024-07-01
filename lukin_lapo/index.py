from flask import Blueprint, render_template, url_for

bp = Blueprint('index', __name__)

@bp.route('/')
def index() -> str:
    return render_template("index/index.html")
