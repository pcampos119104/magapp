from django.db import models

from magapp.core.models import ModelBase
from magapp.core.utils import create_unique_slug


class Ingredient(ModelBase):
    name = models.CharField("nome", max_length=64, help_text="Ingrediente e quantidade")
    slug = models.SlugField(max_length=64, unique=True)

    class Meta:
        verbose_name = "ingrediente"
        verbose_name_plural = "ingredientes"

    def save(self, *args, **kwargs):
        self.slug = create_unique_slug(self.title)
        super(Ingredient, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
