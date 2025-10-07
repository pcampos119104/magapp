
import pytest
from model_bakery import baker

from magapp.ingredients.models import Ingredient


@pytest.fixture
def ingredient(db):
    model = baker.make(
        Ingredient,
        _fill_optional=True,
        name='Farinha',
        deleted_at=None,
    )
    return model


@pytest.fixture
def ingredients(db):
    return baker.make(Ingredient, _fill_optional=True, deleted_at=None, _quantity=3)
