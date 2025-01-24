import pytest
from model_bakery import baker

from magapp.recipes.models import Metric, Qualifier


@pytest.fixture()
def metrics(db):
    return baker.make(Metric, deleted_at=None, _quantity=10)


@pytest.fixture()
def qualifiers(db):
    return baker.make(Qualifier, deleted_at=None, _quantity=10)
