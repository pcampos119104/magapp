from typing import Type

import pytest
from model_bakery import baker

from magapp.ingredients.models import Ingredient


@pytest.fixture
def ingredient(db) -> Type[Ingredient]:
    model = baker.make(
        Ingredient,
        _fill_optional=True,
        name='Farinha',
        deleted_at=None,
    )
    return model
