import uuid

import pytest
from django.urls import reverse
from model_bakery import baker

from magapp.django_assertions import assert_contains
from magapp.ingredients.models import Ingredient

pytestmark = pytest.mark.django_db


class TestIngredientsViews:
    def test_list_view(self, client):
        ingredients = baker.make(
            Ingredient, 5, name=str(uuid.uuid4())[:6], deleted_at=None
        )
        resp = client.get(reverse("ingredients:list"))
        assert resp.status_code == 200
        assert_contains(resp, ingredients[0].name)
        assert_contains(resp, ingredients[0].get_absolute_url())
        assert_contains(resp, ingredients[-1].name)
        assert_contains(resp, ingredients[-1].get_absolute_url())

    @pytest.mark.skip
    def test_detail_view(self, client, ingredient: Ingredient):
        resp = client.get(reverse("ingredients:detail", args=(ingredient.slug,)))
        assert resp.status_code == 200
        assert_contains(resp, ingredient.title)

    def test_create_view_no_login(self, client):
        resp = client.get(reverse("ingredients:create"))
        assert resp.status_code == 302

    def test_create_view_with_login(self, logged_client):
        resp = logged_client.get(reverse("ingredients:create"))
        assert resp.status_code == 200
        assert_contains(resp, "id_name")

    @pytest.mark.skip
    def test_delete_view(self, logged_client):
        ingredient = baker.make(Ingredient, _fill_optional=True, is_removed=False)
        resp = logged_client.delete(
            reverse("ingredients:delete", args=(ingredient.id,))
        )
        assert_contains(resp, '"ok": true')


"""
    def test_loja_update_view(self, client, loja: Loja):
        resp = client.get(reverse("lojas:loja-update", args=(loja.id,)))
        assert_contains(resp, loja.nome)
"""
