from flask import Flask
from app.routes import main as routes

app = Flask(__name__)

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run()