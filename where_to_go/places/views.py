"""Module with views logic of the Places app."""

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from where_to_go.places.models import Place
from where_to_go.places.schemas import PlaceSchema

JSON_INDENT = 4


class MainPageView(TemplateView):
    """View for main (home) site page."""

    template_name = 'main_page.html'

    def get_context_data(self, **kwargs: dict) -> dict:
        """Get context that will be transferred to JS script in template.

        Args:
            kwargs: keyword arguments in a dictionary.

        Returns:
            Context with added places' geo data to it.
        """
        context = super().get_context_data(**kwargs)
        places = Place.objects.all()
        geo_jsons = []
        for place in places:
            geo_jsons.append(
                {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [place.latitude, place.longitude],
                    },
                    'properties': {
                        'title': place.title,
                        'placeId': place.pk,
                        'detailsUrl': reverse('place_details', args=[place.pk]),
                    },
                }
            )
        geo_data = {'type': 'FeatureCollection', 'features': geo_jsons}
        context['geo_data'] = geo_data
        return context


def get_place_details(request: WSGIRequest, pk: int) -> JsonResponse:
    """View for place details.

    Args:
        request: wsgi request received from user.
        pk: id of place which details to get.

    Returns:
        JsonResponse with place details or 404 page if place does not exist.
    """
    place = get_object_or_404(Place, pk=pk)
    schema = PlaceSchema()
    serialised_place = schema.dump(place)
    return JsonResponse(
        serialised_place, json_dumps_params={'ensure_ascii': False, 'indent': JSON_INDENT},
    )
