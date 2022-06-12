import uuid

import pytest
from model_bakery import baker

from magapp.recipes.models import Recipe

pytestmark = pytest.mark.django_db


# Recipe
class TestRecipeModel:
    def test_str(self, recipe: Recipe) -> None:
        assert f"{recipe.title}" == str(recipe)

    def test_obj(self, recipe: Recipe) -> None:
        assert isinstance(recipe, Recipe)

    def test_softdelete(self, db, created_user) -> None:
        model = baker.make(
            Recipe,
            _fill_optional=True,
            title=str(uuid.uuid4()),
            draft=False,
            created_by=created_user,
            deleted_at=None,
        )
        assert Recipe.objects.filter(slug=model.slug).exists()
        model.delete()
        assert not Recipe.objects.filter(slug=model.slug).exists()
        assert Recipe.all_objects.filter(slug=model.slug).exists()

    def test_harddelete(self, db, created_user) -> None:
        model = baker.make(
            Recipe,
            _fill_optional=True,
            title=str(uuid.uuid4()),
            draft=False,
            created_by=created_user,
            deleted_at=None,
        )
        assert Recipe.objects.filter(slug=model.slug).exists()
        model.hard_delete()
        assert not Recipe.objects.filter(slug=model.slug).exists()
        assert not Recipe.all_objects.filter(slug=model.slug).exists()
