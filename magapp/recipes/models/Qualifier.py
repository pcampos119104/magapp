
from magapp.base.models import SoftDeletionModel
from magapp.base.utils.models import LowerCharField


class Qualifier(SoftDeletionModel):
    name = LowerCharField('nome', max_length=64, help_text='Qualificador do ingrediente')

    class Meta:
        verbose_name = 'Qualificador'
        verbose_name_plural = 'Qualificadores'

    def __str__(self):
        return self.name
