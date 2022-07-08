from django.core.paginator import Paginator
from django_filters.views import FilterView

from magapp.recipes.filters import RecipeFilter
from magapp.recipes.models import Recipe


class ListView(FilterView):
    model = Recipe
    context_object_name = "recipes_list"
    filter_class = RecipeFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe_filter = RecipeFilter(self.request.GET, queryset=self.get_queryset())
        paginator = Paginator(recipe_filter.qs, 10)
        context["page_obj"] = paginator.get_page(self.request.GET.get("page"))
        context["filter"] = recipe_filter
        return context
