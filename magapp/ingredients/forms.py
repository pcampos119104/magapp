from django import forms


class IngredientForm(forms.Form):
    name = forms.CharField()

