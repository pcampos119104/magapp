from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import redirect, render

from magapp.recipes.forms import RecipeForm, RecipeIngredientForm, RecipeStep1Form

"""
@login_required
def recipe_create(request):
    template = "recipes/recipe_form.html"
    form = RecipeForm(request.POST or None)

    if form.is_valid():
        form.instance.created_by = request.user
        form.save()
        return redirect("recipes:list")

    context = {
        "form": form,
        "ingredient_form": RecipeIngredientForm(),
        # "ingredient_formset_detail": ingredients_formset_detail,
    }
    return render(request, template, context)
"""


@login_required
def recipe_create(request):
    template = "recipes/recipe_add.html"
    form = RecipeStep1Form()
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def partial_add_step_2(request):
    pass


@login_required
def partial_add_step_1(request):
    form = RecipeStep1Form(request.POST)
    context = {}
    if form.is_valid():
        form.instance.created_by = request.user
        form.instance.draft = True
        form.save()
        context = {
            "form": RecipeIngredientForm(),
        }
        return render(request, "recipes/partials/recipe_add_step_2.html", context)
    else:
        context = {
            "form": form,
        }
        return render(request, "recipes/partials/recipe_add_step_1.html", context)


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
            "ingredient_detail": dtformset,
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
