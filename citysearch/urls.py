from django.urls import path

from .views import CitiesPageView, SearchResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', CitiesPageView.as_view(), name='cities'),
]
