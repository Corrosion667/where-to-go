"""Admin module of Palces app."""

from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from where_to_go.places.models import Image, Place

PREVIEW_RATIO = 0.3

admin.site.register(Image)


class ImageInline(admin.TabularInline):
    """Class for image inlines in Place object admin view."""

    model = Image
    readonly_fields = ('preview_image',)

    @admin.display(description=_('Preview'))
    def preview_image(self, image: Image) -> str:
        """Get image as HTML tag for preview.

        Args:
            image: Image object.

        Returns:
            HTML tag of the image.
        """
        width = image.file.width * PREVIEW_RATIO
        height = image.file.height * PREVIEW_RATIO
        return format_html(f'<img src="{image.file.url}" width="{width}" height={height} />')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    """Class for admin view for Place objects."""

    inlines = [ImageInline]
