from marshmallow import Schema, fields


class WeatherSchema(Schema):
    """
    Schema for representing weather data.
    """

    current = fields.Integer(
        required=True, description="The current temperature in degrees."
    )
