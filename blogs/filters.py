from django_filters import rest_framework as filters
from .models import Blog


# We create filters for each field we want to be able to filter on
class BlogFilter(filters.FilterSet):
    topic = filters.CharFilter(lookup_expr='icontains')
    title = filters.CharFilter(lookup_expr='icontains')
    year = filters.NumberFilter()
    year__gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    year__lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    creator__username = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = ['topic', 'title', 'year', 'year__gt', 'year__lt', 'creator__username']

