"""Admin module of Palces app."""

from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from where_to_go.places.models import Image, Place

PREVIEW_RATIO = 0.3
NO_EXTRA_INLINE_FORMS = 0


class ImagePreviewMixin(object):
    """Mixin for getting image preview."""

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


class ImageInline(ImagePreviewMixin, SortableTabularInline):
    """Class for image inlines in Place object admin view."""

    model = Image
    extra = NO_EXTRA_INLINE_FORMS


@admin.register(Image)
class ImageAdmin(ImagePreviewMixin, admin.ModelAdmin):
    """Class for admin view for Image objects."""

    list_select_related = ['place']
    raw_id_fields = list_select_related
    search_fields = ['place__title']
    list_filter = search_fields
    ordering = ['place__title', 'position']


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    """Class for admin view for Place objects."""

    inlines = [ImageInline]
    search_fields = ['title']
