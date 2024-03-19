from apispec import APISpec
from flask import Flask
from flask_apispec import FlaskApiSpec
from apispec.ext.marshmallow import MarshmallowPlugin

docs = None

spec = APISpec(
    title="Vue Forecast API",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[MarshmallowPlugin()],
)


def initialize_docs(app: Flask):
    """
    Registers the FlaskApiSpec instance for generating API documentation.

    Parameters:
    - app (Flask): The Flask application instance.
    """
    global docs
    docs = FlaskApiSpec(app)
