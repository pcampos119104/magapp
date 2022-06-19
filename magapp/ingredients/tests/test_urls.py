import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


class TestRecipesUrls:
    def test_list(self) -> None:
        assert reverse("recipes:list") == "/recipes/"
        assert resolve("/recipes/").view_name == "recipes:list"

    def test_create(self) -> None:
        assert reverse("recipes:create") == "/recipes/create/"
        assert resolve("/recipes/create/").view_name == "recipes:create"


"""
    def test_update(self, rede: Rede) -> None:
        assert (
            reverse("lojas:rede-update", args=(rede.id,))
            == f"/lojas/redes/{rede.id}/update/"
        )
        assert (
            resolve(f"/lojas/redes/{rede.id}/update/").view_name == "lojas:rede-update"
        )

    def test_delete(self, rede: Rede) -> None:
        assert (
            reverse("lojas:rede-delete", args=(rede.id,))
            == f"/lojas/redes/{rede.id}/delete/"
        )
        assert (
            resolve(f"/lojas/redes/{rede.id}/delete/").view_name == "lojas:rede-delete"
        )
"""
