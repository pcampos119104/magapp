import uuid

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.functions import Lower
from django.urls import reverse
from slugify import slugify

from magapp.base.models import SoftDeletionModel
from magapp.base.utils.models import LowerCharField
from magapp.recipes.models import Recipe


class Meal(SoftDeletionModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = LowerCharField('título', max_length=64, help_text='Titulo da refeicao')
    slug = models.SlugField(
        max_length=64, editable=False, unique=True, error_messages={'unique': 'Este slug já existe.'}
    )
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)
    recipes = models.ManyToManyField(Recipe)

    class Meta:
        verbose_name = 'Refeicao'
        verbose_name_plural = 'refeicoes'
        ordering = ['title']
        constraints = [models.UniqueConstraint('slug', name='unique_meal_slug')]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(':detail', kwargs={'slug': self.slug})
