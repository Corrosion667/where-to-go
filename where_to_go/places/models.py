"""Models for Places app."""

import os

from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField

TITLE_MAX_LENGTH = 200
NON_ZERO_INDEX = 1


class Place(models.Model):
    """Class for objects of interesting places to visit."""

    title = models.CharField(unique=True, max_length=TITLE_MAX_LENGTH, verbose_name=_('Title'))
    description_short = models.TextField(verbose_name=_('Short description'), blank=True)
    description_long = HTMLField(verbose_name=_('Full description'), blank=True)
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

    @property
    def imgs(self) -> models.QuerySet:
        """Get evaluated queryset with Images linked with Place object.

        Returns:
            Images QuerySet.
        """
        return self.images.all()


class Image(models.Model):
    """Class for places' images."""

    position = models.PositiveIntegerField(default=NON_ZERO_INDEX, verbose_name=_('Display order'))
    place = models.ForeignKey(
        Place,
        on_delete=models.SET_NULL,
        related_name='images',
        blank=True,
        null=True,
        verbose_name=Place._meta.verbose_name,
    )
    file = models.ImageField(
        verbose_name=_('File with image'),
        upload_to=os.path.join('images', 'places'),
    )

    class Meta(object):
        """Meta information of model."""

        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        ordering = ['position']

    def __str__(self) -> str:
        """Present object as a string.

        Returns:
            Position with place of interest to which image attached to.
        """
        return f'{self.position} {self.place}'
