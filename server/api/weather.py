from flask import Blueprint, jsonify
from flask_apispec import marshal_with

from constants import ENDPOINTS
from schemas import WeatherSchema
from shared import get_docs

weather_bp = Blueprint("weather", __name__, url_prefix=ENDPOINTS.WEATHER)


@weather_bp.route(
    "/",
    methods=["GET"],
)
@marshal_with(WeatherSchema, code=200)
def get_weather():
    return jsonify(WeatherSchema().dump({"current": 72}))


def register_docs():
    """
    Register the weather API documentation.

    This function retrieves the documentation for the weather API and registers it with the appropriate blueprint.
    """
    docs = get_docs()
    docs.register(get_weather, blueprint=weather_bp.name)
