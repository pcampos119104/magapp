import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from magapp.ingredients.models import Ingredient
from magapp.recipes.forms import (
    IngredientForm,
    RecipeIngredientForm,
    RecipeStep1Form,
    RecipeStep2Form,
)
from magapp.recipes.models import Recipe, RecipeIngredient
from magapp.utils import log_start

logger = logging.getLogger(__name__)


@login_required
@log_start
def ingredient_create(request):
    template = "ingredients/ingredient_add.html"
    form = IngredientForm()
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
@log_start
def partial_add(request):
    form = IngredientForm(request.POST)

    if form.is_valid():
        form.save()
        return render(request, "ingredients/partials/ingredient_add_finish.html")
    else:
        context = {
            "form": form,
        }
        return render(
            request, "ingredients/partials/ingredient_add_partial.html", context
        )
