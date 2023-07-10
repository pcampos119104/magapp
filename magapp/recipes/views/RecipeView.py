import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from magapp.recipes.forms import (
    RecipeCreateForm,
    RecipeIngredientForm,
    RecipeIngredientFormSet,
)
from magapp.recipes.models import Recipe, RecipeIngredient
from magapp.utils import log_start

logger = logging.getLogger(__name__)


class RecipeCreateView(LoginRequiredMixin, View):
    @log_start
    def get(self, request):
        template = "recipes/recipe_add.html"
        recipe_form = RecipeCreateForm()
        ingredient_formset = RecipeIngredientFormSet()
        context = {
            "form": recipe_form,
            "ingredient_formset": ingredient_formset,
        }
        return render(request, template, context)

    @log_start
    def post(self, request):
        form = RecipeCreateForm(request.POST)
        ingredient_formset = RecipeIngredientFormSet(request.POST)
        logger.debug(f"request.POST - {request.POST}")
        context = {}
        if not form.is_valid() or not ingredient_formset.is_valid():
            logger.debug("form.is_valid() or ingredient_formset.is_valid() - False")
            logger.debug(f"form.errors.as_json() - {form.errors.as_json()}")
            context = {
                "form": form,
                "ingredient_formset": ingredient_formset,
            }
            logger.debug(f"context - {context}")
            return render(request, "recipes/partials/recipe_create.html", context)

        logger.debug("form.is_valid() or ingredient_formset.is_valid() - True")
        form.instance.created_by = request.user
        recipe = form.save()
        recipe_ingredients = ingredient_formset.save(commit=False)
        for recipe_ingredient in recipe_ingredients:
            recipe_ingredient.recipe = recipe
            recipe_ingredient.save()
        return render(request, "recipes/partials/recipe_add_step_finish.html")


@login_required
@log_start
def remove_recipeingredient(request, pk):
    recipe_ingredient = RecipeIngredient.objects.get(pk=pk)
    logger.debug(f"recipe_ingredient - {recipe_ingredient}")
    recipe = recipe_ingredient.recipe
    recipe_ingredient.delete()
    response_form = None

    context = {
        "recipe_slug": recipe.slug,
        "form": response_form,
        "ingredients": RecipeIngredient.objects.filter(recipe=recipe).all(),
    }
    logger.debug(f"context - {context}")
    return render(request, "recipes/partials/recipe_add_step_2.html", context)
