from django.views import generic

from magapp.recipes import facade
from magapp.recipes.models import Recipe


class DetailView(generic.detail.DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredient_list"] = facade.list_recipe_ingredients(self.object)
        return context
