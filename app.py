from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from routes import init_app
init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
