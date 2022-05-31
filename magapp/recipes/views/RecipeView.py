import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from magapp.recipes.forms import RecipeIngredientForm, RecipeStep1Form, RecipeStep2Form
from magapp.recipes.models import Recipe, RecipeIngredient
from magapp.utils import log_start

logger = logging.getLogger(__name__)


@login_required
@log_start
def recipe_create(request):
    template = "recipes/recipe_add.html"
    form = RecipeStep1Form()
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
@log_start
def partial_add_step_1(request):
    form = RecipeStep1Form(request.POST)
    context = {}
    if form.is_valid():
        form.instance.created_by = request.user
        form.instance.draft = True
        form.save()
        context = {
            "recipe_slug": form.instance.slug,
            "recipe_form": RecipeStep2Form(),
            "ingredient_form": RecipeIngredientForm(),
        }
        return render(request, "recipes/partials/recipe_add_step_2.html", context)
    else:
        context = {
            "form": form,
        }
        return render(request, "recipes/partials/recipe_add_step_1.html", context)


@login_required
@log_start
def partial_add_step_2(request, slug):
    obj = get_object_or_404(Recipe, slug=slug)
    form = RecipeStep2Form(request.POST or None, instance=obj)

    if form.is_valid():
        form.instance.draft = False
        form.save()
        return render(request, "recipes/partials/recipe_add_finish.html")
    else:
        context = {
            "recipe_form": form,
        }
        return render(request, "recipes/partials/recipe_add_step_2.html", context)


@log_start
def add_recipeingredient(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    form = RecipeIngredientForm(request.POST)
    response_form = RecipeIngredientForm()
    if form.is_valid():
        logger.debug("form.is_valid() - True")
        obj = form.save(commit=False)
        obj.recipe = recipe
        obj.save()

    else:
        logger.debug("form.is_valid() - False")
        logger.debug(f"form.errors.as_json() - {form.errors.as_json()}")
        response_form = form

    context = {
        "recipe_slug": recipe.slug,
        "ingredient_form": response_form,
        "ingredients": RecipeIngredient.objects.filter(recipe=recipe).all(),
    }
    logger.debug(f"context - {context}")
    return render(
        request, "recipes/partials/recipe_add_step_2_ingredient_form.html", context
    )
