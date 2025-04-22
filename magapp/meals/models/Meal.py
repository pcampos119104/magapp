import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.forms import model_to_dict
from django.urls import reverse

from magapp.base.models import SoftDeletionModel
from magapp.base.utils.models import LowerCharField
from magapp.utils import create_unique_slug


class Meal(SoftDeletionModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = LowerCharField('título', max_length=64, help_text='Titulo da refeição')
    slug = models.SlugField(
        max_length=64, editable=False, unique=True, error_messages={'unique': 'Este slug já existe.'}
    )
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)
    recipes = models.ManyToManyField('recipes.Recipe', related_name='meals')

    class Meta:
        verbose_name = 'Refeição'
        verbose_name_plural = 'refeições'
        ordering = ['title']
        constraints = [models.UniqueConstraint('slug', name='unique_meal_slug')]

    def save(self, *args, **kwargs):
        self.slug = create_unique_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Meals({model_to_dict(self)})'

    def get_absolute_url(self):
        return reverse('meals:detail', kwargs={'slug': self.slug})
