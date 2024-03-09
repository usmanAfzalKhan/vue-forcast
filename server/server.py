from flask import Flask
from api import weather_bp

app = Flask(__name__)


app.register_blueprint(weather_bp)


if __name__ == "__main__":
    app.run(port=5000)
