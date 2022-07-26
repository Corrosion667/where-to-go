"""Admin module of Palces app."""

from django.contrib import admin

from where_to_go.places.models import Image, Place

admin.site.register(Image)


class ImageInline(admin.TabularInline):
    """Class for image inlines in Place object admin view."""

    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    """Class for admin view for Place objects."""

    inlines = [
        ImageInline,
    ]
