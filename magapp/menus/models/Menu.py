from django.contrib.auth import get_user_model
from django.db import models
from django.forms import model_to_dict
from django.urls import reverse

from magapp.base.models import SoftDeletionModel
from magapp.base.utils.models import LowerCharField
from magapp.utils import create_unique_slug


class Menu(SoftDeletionModel):
    VISIBILITY_CHOICES = [
        ('private', 'Privada'),
        ('public', 'Pública'),
    ]
    title = LowerCharField('título', max_length=64, help_text='Título do cardápio.')
    description = models.TextField('descrição', help_text='Breve descrição do cardápio.')
    slug = models.SlugField(max_length=64, unique=True, editable=False)
    visibility = models.CharField(
        max_length=10, choices=VISIBILITY_CHOICES, default='private', help_text='Se o cardápio é público.'
    )
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'cardápio'
        verbose_name_plural = 'cardápios'

    def save(self, *args, **kwargs):
        self.slug = create_unique_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Menu({model_to_dict(self)})'

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'slug': self.slug})
