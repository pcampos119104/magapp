from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from magapp.recipes.forms import RecipeForm, RecipeIngredientForm
from magapp.recipes.models import Recipe


class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Recipe
    template_name = "recipes/recipe_form.html"
    form_class = RecipeForm
    success_url = reverse_lazy("recipes:list")

    def get_context_data(self, **kwargs):
        ctx = super(CreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx["form"] = RecipeForm(self.request.POST)
            ctx["ingredient_form"] = RecipeIngredientForm(self.request.POST)
            ctx["ingredient_formset_detail"] = formset_factory(
                RecipeIngredientForm, extra=0
            )(self.request.POST)
        else:
            ctx["form"] = RecipeForm()
            ctx["ingredient_form"] = RecipeIngredientForm()
            ctx["ingredient_formset_detail"] = formset_factory(
                RecipeIngredientForm, extra=0
            )()
        return ctx

    def form_valid(self, form):
        context = self.get_context_data()
        recipe_ingredients = context["ingredient_formset_detail"]
        if recipe_ingredients.is_valid():
            form.instance.created_by = self.request.user
            recipe = form.save()
            for recipe_ingredient in recipe_ingredients:
                instance = recipe_ingredient.instance
                instance.recipe = recipe
                """
                name = recipe_ingredient.cleaned_data["name"]
                ingredient = Ingredient(name=name)
                ingredient.save()
                instance.ingredient = ingredient
                """
                instance.save()
        return super().form_valid(form)


def add_recipeingredient(request):
    form = RecipeIngredientForm(request.POST)
    formset_detail = formset_factory(RecipeIngredientForm, extra=0)(request.POST)
    context = {}
    if form.is_valid():
        dtform = form.cleaned_data
        dtformset = []
        if formset_detail and formset_detail.is_valid():
            dtformset = formset_detail.cleaned_data
        dtformset.extend([dtform])
        formset = formset_factory(RecipeIngredientForm, extra=0)(initial=dtformset)
        context = {
            "ingredient_formset_detail": formset,
            "ingredient_form": RecipeIngredientForm(),
            "is_valid": True,
        }
        return render(request, "recipes/partials/recipe_ingredient_form.html", context)
    else:
        context = {
            "is_valid": False,
            "ingredient_form": form,
        }
        result = render(
            request, "recipes/partials/recipe_ingredient_form.html", context
        )
        return result
