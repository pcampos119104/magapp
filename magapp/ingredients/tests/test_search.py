import pytest
from model_bakery import baker

from magapp.ingredients.models import Ingredient

pytestmark = pytest.mark.search


class TestSearchIngredients:
    def test__search(self, logged_client):
        # batAtà
        baker.make(
            Ingredient,
            _fill_optional=True,
            name='batata',
            deleted_at=None,
        )
        ingredient = Ingredient.objects.filter(name__unaccent__icontains='batAtà')
        assert len(ingredient) == 1
