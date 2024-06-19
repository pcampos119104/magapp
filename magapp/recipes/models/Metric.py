from django.db import models
from django.forms import model_to_dict

from magapp.base.models import SoftDeletionModel
from magapp.base.utils.models import LowerCharField


class Metric(SoftDeletionModel):
    abbr = models.CharField('Abreviação', max_length=10, help_text='Abreviação da métrica.')
    name = LowerCharField('nome', max_length=20, help_text='Nome da métrica')

    class Meta:
        verbose_name = 'métrica'
        verbose_name_plural = 'métricas'

    def __str__(self):
        return self.abbr

    def __repr__(self):
        return f'Métrica({model_to_dict(self)})'
