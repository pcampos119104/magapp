from django.db import models

from magapp.core.models import ModelBase


class Ingredient(ModelBase):
    name = models.CharField("nome", max_length=64, help_text="Ingrediente e quantidade")

    class Meta:
        verbose_name = "ingrediente"
        verbose_name_plural = "ingredientes"

    def __str__(self):
        return self.name
