from django.db import models
from django.forms import model_to_dict

from magapp.core.models import ModelBase
from magapp.ingredients.models import Ingredient
from magapp.recipes.models import Recipe


class RecipeIngredient(ModelBase):
    METRIC_KILOGRAM = "Kg"
    METRIC_LITER = "L"
    METRIC_CHOICES = ((METRIC_KILOGRAM, "Kilograma"), (METRIC_LITER, "Litro"))
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    qtd = models.IntegerField(
        "Quantidade", help_text="Quantidade relacionado a métrica"
    )
    metric_type = models.CharField(
        "Tipo de métrica",
        max_length=2,
        choices=METRIC_CHOICES,
        blank=False,
        null=False,
        help_text="kg, mg, litro, ml",
    )

    class Meta:
        verbose_name = "Ingrediente de receita"
        verbose_name_plural = "Ingredientes de receita"

    def __str__(self):
        return f"{self.qtd} {self.metric_type} de {self.ingredient.name}"

    def __repr__(self):
        return f"RecipeIngredient({model_to_dict(self)})"


"""
    def get_absolute_url(self):
        return reverse("recipe_ingredients:detail", kwargs={"pk": self.pk})
"""
