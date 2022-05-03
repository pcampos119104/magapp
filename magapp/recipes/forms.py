from django import forms

from magapp.ingredients.models import Ingredient
from magapp.recipes.models import Recipe, RecipeIngredient


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name",)


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ("qtd", "metric_type", "ingredient", "recipe")


class RecipeStep2Form(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("directions", "font")


# Novos Forms
class RecipeStep1Form(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("title", "description")
