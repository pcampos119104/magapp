from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from magapp.core.models import ModelBase
from magapp.core.utils import create_unique_slug


class Ingredient(ModelBase):
    name = models.CharField("nome", max_length=64, help_text="Ingrediente e quantidade")
    slug = models.SlugField(max_length=64, unique=True, editable=False)
    created_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False
    )

    class Meta:
        verbose_name = "ingrediente"
        verbose_name_plural = "ingredientes"

    def save(self, *args, **kwargs):
        self.slug = create_unique_slug(self.name)
        super(Ingredient, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"slug": self.slug})
