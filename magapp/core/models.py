from model_utils.models import SoftDeletableModel, UUIDModel


class ModelBase(SoftDeletableModel, UUIDModel):
    class Meta:
        abstract = True
