from flask import Blueprint, render_template

indexUrl = Blueprint("index", __name__)

@indexUrl.route("/")
def index():
    return render_template("index.html")
