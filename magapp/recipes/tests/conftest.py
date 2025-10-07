import pytest
from model_bakery import baker

from magapp.ingredients.models import Ingredient
from magapp.recipes.models import Metric, Qualifier


@pytest.fixture
def metrics(db):
    return baker.make(Metric, deleted_at=None, _quantity=10)


@pytest.fixture
def qualifiers(db):
    return baker.make(Qualifier, deleted_at=None, _quantity=10)

@pytest.fixture
def ingredients(db):
    return baker.make(Ingredient, _fill_optional=True, deleted_at=None, _quantity=3)
