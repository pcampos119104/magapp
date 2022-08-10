from django.db import models

from magapp.core.models import ModelBase


class Qualifier(ModelBase):
    name = models.CharField(
        "nome", max_length=64, help_text="Qualificador do ingrediente"
    )

    class Meta:
        verbose_name = "Qualificador"
        verbose_name_plural = "Qualificadores"

    def __str__(self):
        return self.name
