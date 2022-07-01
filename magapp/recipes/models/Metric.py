from django.db import models
from django.forms import model_to_dict

from magapp.core.models import ModelBase


class Metric(ModelBase):
    abbr = models.CharField(
        "Abreviação", max_length=10, help_text="Abreviação da métrica."
    )
    name = models.CharField("nome", max_length=20, help_text="Nome da métrica")

    class Meta:
        verbose_name = "métrica"
        verbose_name_plural = "métricas"

    def __str__(self):
        return self.abbr

    def __repr__(self):
        return f"Métrica({model_to_dict(self)})"
