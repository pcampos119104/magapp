import uuid

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from slugify import slugify

from magapp.base.models import SoftDeletionModel
from magapp.base.utils.models import LowerCharField


class Ingredient(SoftDeletionModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = LowerCharField(
        'nome',
        unique=True,
        max_length=64,
        help_text='Ingrediente e quantidade',
        error_messages={'unique': 'Este ingrediente já existe.'},
    )
    slug = models.SlugField(
        max_length=64, editable=False, unique=True, error_messages={'unique': 'Este slug já existe.'}
    )
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude)
        # If slug is the same ingredient name already exist, easier war to ignore accents
        if Ingredient.objects.filter(slug=slugify(self.name)).exists():
            raise ValidationError({'name': 'Este ingrediente já existe.'})

    class Meta:
        verbose_name = 'ingrediente'
        verbose_name_plural = 'ingredientes'
        ordering = ['name']
        constraints = [models.UniqueConstraint('slug', name='unique_ingredient_slug')]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredients:detail', kwargs={'slug': self.slug})
