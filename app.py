from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from routes import init_app
init_app(app)

if __name__ == "__main__":
    app.run(host=Config.HOST,port=Config.PORT,debug=Config.DEBUG)
