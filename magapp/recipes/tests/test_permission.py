import pytest
from model_bakery import baker

from magapp.recipes.models import Recipe

pytestmark = pytest.mark.auth


class TestUpdatePermissionRecipes:
    def test_same_user_edit(self, db, client, user_a):
        recipe = baker.make(Recipe, deleted_at=None, owner=user_a)
        client.force_login(user_a)
        resp = client.get(recipe.get_absolute_url())
        assert resp.status_code == 200

    def test_different_user_edit(self, db, client, user_a, user_b):
        recipe = baker.make(Recipe, deleted_at=None, owner=user_b)
        client.force_login(user_a)
        resp = client.get(recipe.get_absolute_url())
        assert resp.status_code == 404
