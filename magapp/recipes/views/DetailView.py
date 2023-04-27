from django.views import generic

from magapp.recipes.models import Recipe


class DetailView(generic.detail.DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredient_list"] = self.object.recipeingredient_set.all()
        return context
