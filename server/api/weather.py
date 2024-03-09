from constants import ENDPOINTS
from flask import Blueprint, jsonify

weather_bp = Blueprint("weather", __name__, url_prefix=ENDPOINTS.WEATHER)


@weather_bp.route(
    "/",
    methods=["GET"],
)
def get_weather():
    return jsonify({"weather": "sunny"})
