import django_filters
from django import forms


class RecipeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr="icontains",
    )
