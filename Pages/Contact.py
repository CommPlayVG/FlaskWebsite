from flask import Blueprint, render_template

contactUrl = Blueprint("contact", __name__)

@contactUrl.route("/contact")
def contact():
    return render_template("contact.html")
