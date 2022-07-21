"""Models for places app."""

from django.db import models

TITLE_MAX_LENGTH = 200


class Place(models.Model):
    """Class for objects of interesting places to visit."""

    title = models.CharField(unique=True, max_length=TITLE_MAX_LENGTH, verbose_name='Название')
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    full_description = models.TextField(verbose_name='Полное описание', blank=True)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta(object):
        """Meta information of model."""

        verbose_name = 'Место интереса'
        verbose_name_plural = 'Места интереса'

    def __str__(self) -> str:
        """Present object as a string.

        Returns:
            Title of place.
        """
        return self.title
