import django_filters
from django import forms


class RecipeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        widget=forms.TextInput(attrs={"class": "form-control bg-light border-0 small"}),
        lookup_expr="icontains",
    )
