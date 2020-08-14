from django.views.generic import TemplateView, ListView

from .models import City
from django.db.models import Q


class CitiesPageView(TemplateView):
    template_name = 'searchcities/cities.html'

class SearchResultsView(ListView):
    model = City
    template_name = 'searchcities/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list
