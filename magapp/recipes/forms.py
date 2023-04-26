from django import forms

from magapp.ingredients.models import Ingredient
from magapp.recipes.models import Recipe, RecipeIngredient


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name",)


class RecipeAddStep1Form(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("title", "description", "font")


class RecipeAddStep2Form(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ("qtd", "metric", "ingredient", "qualifiers")


class RecipeAddStep3Form(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("directions",)
