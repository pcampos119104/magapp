from django import forms

from magapp.ingredients.models import Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Ingredient
