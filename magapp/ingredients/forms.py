from django import forms

from magapp.ingredients.models import Ingredient


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name",)



