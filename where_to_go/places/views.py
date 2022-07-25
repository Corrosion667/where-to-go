"""Module with views logic of the places app."""

from django.views.generic import TemplateView
from where_to_go.places.models import Place


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
        geo_features = []
        for place in places:
            geo_features.append(
                {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [place.latitude, place.longitude],
                    },
                    'properties': {
                        'title': place.title,
                        'placeId': place.pk,
                        'detailsUrl': 'https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json'
                    },
                },
            )
        geo_data = {'type': 'FeatureCollection', 'features': geo_features}
        context['geo_data'] = geo_data
        return context
