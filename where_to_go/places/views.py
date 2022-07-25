"""Module with views logic of the places app."""

from django.views.generic import TemplateView

geo_fixture = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json"
          }
        },
      ],
    }


class MainPageView(TemplateView):
    """View for main (home) site page."""

    template_name = 'main_page.html'

    def get_context_data(self, **kwargs: dict) -> dict:
        """Get context that will be transferred to JS script in template.

        Args:
            kwargs: keyword arguments in a dictionary.

        Returns:
            Context with added geo data to it.
        """
        context = super().get_context_data(**kwargs)
        context['geo_data'] = geo_fixture
        return context
