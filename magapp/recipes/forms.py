from django import forms
from django.forms import inlineformset_factory

from magapp.ingredients.models import Ingredient
from magapp.recipes.models import Recipe, RecipeIngredient


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name",)


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ("qtd", "metric", "ingredient", "qualifiers")


RecipeIngredientFormSet = inlineformset_factory(
    Recipe, RecipeIngredient, form=RecipeIngredientForm, extra=1
)


class RecipeCreateForm(forms.ModelForm):
    # ingredients = RecipeIngredientForm(many=True)

    class Meta:
        model = Recipe
        fields = ("title", "description", "font", "directions")
