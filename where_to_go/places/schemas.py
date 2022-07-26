"""Module for serialization of Places app models."""

from marshmallow import Schema, fields


class ImageSchema(Schema):
    """Schema for serialization Image objects."""

    file_url = fields.Function(lambda image: image.file.url)


class CoodrinatesSchema(Schema):
    """Schema for serialization place's coordinates."""

    lat = fields.Float(as_string=True)
    lng = fields.Float(as_string=True)


class PlaceSchema(Schema):
    """Schema for serialization Place objects."""

    imgs = fields.Pluck(ImageSchema, 'file_url', many=True)
    coordinates = fields.Method('get_coordinates')

    class Meta(object):
        """Meta information of schema."""

        additional = ('title', 'description_short', 'description_long')

    @staticmethod
    def get_coordinates(place) -> dict:
        """Get coordinates as a dict with latitude and longitude.

        Args:
            place: Place object.

        Returns:
            Dictionary with coordinates.
        """
        return CoodrinatesSchema().dump({'lat': place.latitude, 'lng': place.longitude})
