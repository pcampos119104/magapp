from datetime import timezone

from django.db import models
from model_utils.models import SoftDeletableModel, UUIDModel

from magapp.recipes.managers import DraftManager, SoftDeletionManager


class DraftModel(models.Model):
    draft = models.BooleanField("Rascunho", help_text="Se é um rascunho")

    objects = DraftManager()

    class Meta:
        abstract = True


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True, default=None)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()


class ModelBase(SoftDeletionModel, UUIDModel):
    class Meta:
        abstract = True
