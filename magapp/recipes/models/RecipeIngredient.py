from django.db import models
from django.forms import model_to_dict
from django.urls import reverse

from magapp.base.models import SoftDeletionModel
from magapp.base.utils.models import LowerCharField
from magapp.ingredients.models import Ingredient
from magapp.recipes.models import Metric, Recipe


class RecipeIngredient(SoftDeletionModel):
    ingredient = models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)
    metric = models.ForeignKey('recipes.Metric', on_delete=models.CASCADE)
    qualifiers = models.ManyToManyField('recipes.Qualifier', blank=True)
    qtd = models.IntegerField('Quantidade', help_text='Quantidade relacionado a métrica')

    class Meta:
        verbose_name = 'Ingrediente de receita'
        verbose_name_plural = 'Ingredientes de receita'

    def __str__(self):
        return f'{self.qtd} {self.metric} de {self.ingredient.name}'

    def __repr__(self):
        return f'RecipeIngredient({model_to_dict(self)})'
