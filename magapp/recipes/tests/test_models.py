import uuid

import pytest
from model_bakery import baker

from magapp.recipes.models import Metric, Recipe

pytestmark = [pytest.mark.django_db, pytest.mark.models]


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


class TestMetricModel:
    def test_str(self, metric: Metric) -> None:
        assert metric.abbr == str(metric)

    def test_obj(self, metric: Metric) -> None:
        assert isinstance(metric, Metric)

    def test_softdelete(self, db, created_user) -> None:
        model = baker.make(
            Metric,
            _fill_optional=True,
            deleted_at=None,
        )
        assert Metric.objects.filter(pk=model.pk).exists()
        model.delete()
        assert not Metric.objects.filter(pk=model.pk).exists()
        assert Metric.all_objects.filter(pk=model.pk).exists()

    def test_harddelete(self, db, created_user) -> None:
        model = baker.make(
            Metric,
            _fill_optional=True,
            deleted_at=None,
        )
        assert Metric.objects.filter(pk=model.pk).exists()
        model.hard_delete()
        assert not Metric.objects.filter(pk=model.pk).exists()
        assert not Metric.all_objects.filter(pk=model.pk).exists()
