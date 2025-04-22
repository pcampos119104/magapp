from django import forms

from magapp.meals.models import Meal


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('title', 'recipes')
