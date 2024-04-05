import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from slugify import slugify

from magapp.base.models import SoftDeletionModel


class Ingredient(SoftDeletionModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        "nome",
        unique=True,
        max_length=64,
        help_text="Ingrediente e quantidade",
        error_messages={'unique': 'Este ingrediente já existe.'}

    )
    slug = models.SlugField(max_length=64, editable=False)
    created_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False
    )

    class Meta:
        verbose_name = "ingrediente"
        verbose_name_plural = "ingredientes"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredients:detail", kwargs={"slug": self.slug})
