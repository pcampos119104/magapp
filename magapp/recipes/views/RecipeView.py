import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from magapp.recipes.forms import (
    RecipeAddStep1Form,
    RecipeAddStep2Form,
    RecipeAddStep3Form,
)
from magapp.recipes.models import Recipe, RecipeIngredient
from magapp.utils import log_start

logger = logging.getLogger(__name__)


@login_required
@log_start
def recipe_create(request):
    template = "recipes/recipe_add.html"
    form = RecipeAddStep1Form()
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
@log_start
def recipe_add_step_1(request):
    form = RecipeAddStep1Form(request.POST)
    context = {}
    if form.is_valid():
        form.instance.created_by = request.user
        form.instance.draft = True
        form.save()
        context = {
            "recipe_slug": form.instance.slug,
            "form": RecipeAddStep2Form(),
        }
        return render(request, "recipes/partials/recipe_add_step_2.html", context)
    else:
        context = {
            "form": form,
        }
        return render(request, "recipes/partials/recipe_add_step_1.html", context)


@login_required
@log_start
def recipe_add_step_2(request, slug):
    recipe = Recipe.all_objects.filter(slug=slug).first()
    logger.debug(f"recipe - {recipe}")
    form = RecipeAddStep2Form(request.POST)
    response_form = RecipeAddStep2Form()
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
        "form": response_form,
        "ingredients": RecipeIngredient.objects.filter(recipe=recipe).all(),
    }
    logger.debug(f"context - {context}")
    return render(request, "recipes/partials/recipe_add_step_2.html", context)


@login_required
@log_start
def recipe_add_step_3(request, slug):
    obj = Recipe.all_objects.filter(slug=slug).first()
    form = RecipeAddStep3Form(request.POST or None, instance=obj)

    if form.is_valid():
        form.instance.draft = False
        form.save()
        return render(request, "recipes/partials/recipe_add_step_finish.html")
    else:
        context = {
            "form": form,
        }
        return render(request, "recipes/partials/recipe_add_step_3.html", context)


@login_required
@log_start
def remove_recipeingredient(request, pk):
    recipe_ingredient = RecipeIngredient.objects.get(pk=pk)
    logger.debug(f"recipe_ingredient - {recipe_ingredient}")
    recipe = recipe_ingredient.recipe
    recipe_ingredient.delete()
    response_form = RecipeAddStep2Form()

    context = {
        "recipe_slug": recipe.slug,
        "form": response_form,
        "ingredients": RecipeIngredient.objects.filter(recipe=recipe).all(),
    }
    logger.debug(f"context - {context}")
    return render(request, "recipes/partials/recipe_add_step_2.html", context)
