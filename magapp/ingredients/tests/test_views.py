import uuid

import pytest
from django.urls import reverse
from model_bakery import baker

from magapp.django_assertions import assert_contains
from magapp.recipes.models import Recipe

pytestmark = pytest.mark.django_db


class TestRecipesViews:
    def test_list_view(self, client):
        recipes = baker.make(
            Recipe, 5, title=str(uuid.uuid4())[:6], draft=False, deleted_at=None
        )
        resp = client.get(reverse("recipes:list"))
        assert resp.status_code == 200
        assert_contains(resp, recipes[0].title)
        assert_contains(resp, recipes[0].get_absolute_url())
        assert_contains(resp, recipes[-1].title)
        assert_contains(resp, recipes[-1].get_absolute_url())

    @pytest.mark.skip
    def test_detail_view(self, client, recipe: Recipe):
        resp = client.get(reverse("recipes:detail", args=(recipe.slug,)))
        assert resp.status_code == 200
        assert_contains(resp, recipe.title)

    def test_create_view_no_login(self, client):
        resp = client.get(reverse("recipes:create"))
        assert resp.status_code == 302

    def test_create_view_with_login(self, logged_client):
        resp = logged_client.get(reverse("recipes:create"))
        assert resp.status_code == 200
        assert_contains(resp, "id_title")

    @pytest.mark.skip
    def test_delete_view(self, logged_client):
        recipe = baker.make(Recipe, _fill_optional=True, is_removed=False)
        resp = logged_client.delete(reverse("recipes:delete", args=(recipe.id,)))
        assert_contains(resp, '"ok": true')


"""
    def test_loja_update_view(self, client, loja: Loja):
        resp = client.get(reverse("lojas:loja-update", args=(loja.id,)))
        assert_contains(resp, loja.nome)
"""
