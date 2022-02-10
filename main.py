from flask import Flask
from Pages.Index import indexUrl

app = Flask(__name__)

app.register_blueprint(indexUrl)

if __name__ == "__main__":
    app.run(debug=True)