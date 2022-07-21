"""Models for places app."""

from django.db import models
from django.utils.translation import gettext_lazy as _

TITLE_MAX_LENGTH = 200


class Place(models.Model):
    """Class for objects of interesting places to visit."""

    title = models.CharField(unique=True, max_length=TITLE_MAX_LENGTH, verbose_name=_('Title'))
    short_description = models.TextField(verbose_name=_('Short description'), blank=True)
    full_description = models.TextField(verbose_name=_('Full description'), blank=True)
    latitude = models.FloatField(verbose_name=_('Latitude'))
    longitude = models.FloatField(verbose_name=_('Longitude'))

    class Meta(object):
        """Meta information of model."""

        verbose_name = _('Place of interest')
        verbose_name_plural = _('Places of interest')

    def __str__(self) -> str:
        """Present object as a string.

        Returns:
            Title of place.
        """
        return self.title
