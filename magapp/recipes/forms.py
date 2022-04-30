from django import forms
from django.forms import formset_factory

from magapp.ingredients.models import Ingredient
from magapp.recipes.models import Recipe, RecipeIngredient


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name",)


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ("qtd", "metric_type", "ingredient")


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("title", "directions", "font")

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control form-control-lg", "placeholder": "Título"}
            ),
            "font": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Livro de receita, link do youtube e etc",
                }
            ),
            "directions": forms.Textarea(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Preparo",
                }
            ),
        }

    def is_valid(self):
        self.fields["ingredients"] = formset_factory(RecipeIngredientForm, extra=0)(
            self.data or None
        )
        return super(RecipeForm, self).is_valid()


# Novos Forms
class RecipeStep1Form(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("title", "description")
