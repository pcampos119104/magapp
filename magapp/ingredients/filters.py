import django_filters
from django import forms


class IngredientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        widget=forms.TextInput(attrs={"class": "form-control bg-light border-0 small"}),
        lookup_expr="icontains",
    )
