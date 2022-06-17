import logging

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django_filters.views import FilterView

from magapp.ingredients.filters import IngredientFilter
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
    form = IngredientForm()
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            return render(
                request, "ingredients/partials/ingredient_add_update_finish.html"
            )
        else:
            return render(
                request,
                "ingredients/partials/ingredient_add_partial.html",
                {
                    "form": form,
                },
            )

    elif request.method == "GET":
        template = "ingredients/ingredient_add.html"
        return render(request, template, {"form": form})


@login_required
@log_start
def ingredient_update(request, slug):
    ingredient = get_object_or_404(Ingredient, slug=slug)
    if request.method == "POST":
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return render(
                request, "ingredients/partials/ingredient_add_update_finish.html"
            )
        else:
            return render(
                request,
                "ingredients/partials/ingredient_update_partial.html",
                {
                    "form": form,
                },
            )
    elif request.method == "GET":
        form = IngredientForm(instance=ingredient)
        template = "ingredients/ingredient_update.html"
        return render(request, template, {"form": form})


class ListView(FilterView):
    model = Ingredient
    context_object_name = "ingredient_list"
    filter_class = IngredientFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredient_filter = IngredientFilter(
            self.request.GET, queryset=self.get_queryset()
        )
        paginator = Paginator(ingredient_filter.qs, 10)
        context["page_obj"] = paginator.get_page(self.request.GET.get("page"))
        context["filter"] = ingredient_filter
        return context


@log_start
def ingredient_detail(request, slug):
    template = "ingredients/ingredient_detail.html"
    context = {
        "ingredient": get_object_or_404(Ingredient, slug=slug),
    }
    return render(request, template, context)
