import pytest
from django.core.exceptions import FieldDoesNotExist

from magapp.ingredients.models import Ingredient
from magapp.recipes.models import Recipe

pytestmark = pytest.mark.django_db


# Ingredient
class TestIngredient:
    def test_ingredient_str(self, ingredient: Ingredient) -> None:
        assert ingredient.name == str(ingredient)

    def test_ingredient_obj(self, ingredient: Ingredient) -> None:
        assert isinstance(ingredient, Ingredient)

    def test_ingredient_fk(self, ingredient: Ingredient) -> None:
        assert isinstance(ingredient.recipe, Recipe)

    # todo refatorar, apresentar o erro para cada field
    def test_ingredient_fields(self, ingredient: Ingredient) -> None:
        try:
            ingredient._meta.get_field("name")
        except FieldDoesNotExist:
            pytest.fail("Falta field")
