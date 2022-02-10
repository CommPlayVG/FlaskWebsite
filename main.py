from flask import Flask

from Pages.Index import indexUrl
from Pages.Contact import contactUrl

app = Flask(__name__)

app.register_blueprint(indexUrl)
app.register_blueprint(contactUrl)

if __name__ == "__main__":
    app.run(debug=True)