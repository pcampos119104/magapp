import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory, modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from magapp.recipes.forms import (
    RecipeAddStep1Form,
    RecipeAddStep2Form,
    RecipeAddStep3Form,
    RecipeCreateForm,
    RecipeIngredientForm,
    RecipeIngredientFormSet,
)
from magapp.recipes.models import Recipe, RecipeIngredient
from magapp.utils import log_start

logger = logging.getLogger(__name__)


@login_required
@log_start
def recipe_add(request):
    template = "recipes/recipe_add.html"
    form = RecipeAddStep1Form()
    context = {
        "form": form,
    }
    return render(request, template, context)


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
        form.instance.draft = False
        recipe = form.save()
        recipe_ingredients = ingredient_formset.save(commit=False)
        for recipe_ingredient in recipe_ingredients:
            recipe_ingredient.recipe = recipe
            recipe_ingredient.save()
        return render(request, "recipes/partials/recipe_add_step_finish.html")


@login_required
@log_start
def recipe_add_step_1(request):
    form = RecipeAddStep1Form(request.POST)
    context = {}
    if not form.is_valid():
        context = {
            "form": form,
        }
        return render(request, "recipes/partials/recipe_add_step_1.html", context)

    form.instance.created_by = request.user
    form.instance.draft = True
    form.save()
    context = {
        "recipe_slug": form.instance.slug,
        "form": RecipeAddStep2Form(),
    }
    return render(request, "recipes/partials/recipe_add_step_2.html", context)


@login_required
@log_start
def recipe_add_step_2(request, slug):
    recipe = Recipe.all_objects.filter(slug=slug).first()
    logger.debug(f"recipe - {recipe.pk}, {recipe.id} ")
    form = RecipeAddStep2Form(data=request.POST)
    response_form = RecipeAddStep2Form()
    if not form.is_valid():
        logger.debug("form.is_valid() - False")
        logger.debug(f"form.errors.as_json() - {form.errors.as_json()}")
        response_form = form

    logger.debug("form.is_valid() - True")
    obj = form.save(commit=False)
    obj.recipe = recipe
    obj.save()
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

    if not form.is_valid():
        context = {
            "form": form,
        }
        return render(request, "recipes/partials/recipe_add_step_3.html", context)

    form.instance.draft = False
    form.save()
    return render(request, "recipes/partials/recipe_add_step_finish.html")


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
