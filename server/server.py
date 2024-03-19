from flask import Flask

from api import weather_bp
from shared import spec, initialize_docs
from constants import ENDPOINTS


def create_app() -> Flask:
    """
    Create and configure the Flask application.

    Returns:
        Flask: The Flask application object.
    """
    app = Flask(__name__)
    return app


def register_blueprints(app: Flask):
    """
    Register the blueprints for the Flask application.

    Args:
        app (Flask): The Flask application object.
    """
    app.register_blueprint(weather_bp)


def register_docs(app: Flask):
    """
    Register the FlaskApiSpec instance for generating API documentation.

    Args:
        app (Flask): The Flask application object.
    """
    app.config.update(
        {
            "APISPEC_SPEC": spec,
            "APISPEC_SWAGGER_URL": ENDPOINTS.DOCS + "/swagger.json",
            "APISPEC_SWAGGER_UI_URL": ENDPOINTS.DOCS,
        }
    )
    initialize_docs(app)


app = create_app()

register_blueprints(app)

register_docs(app)


if __name__ == "__main__":
    app.run(port=5000)
