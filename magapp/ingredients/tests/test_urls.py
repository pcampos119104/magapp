import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


class TestIngredientsUrls:
    def test_list(self) -> None:
        assert reverse("ingredients:list") == "/ingredients/"
        assert resolve("/ingredients/").view_name == "ingredients:list"

    def test_create(self) -> None:
        assert reverse("ingredients:create") == "/ingredients/create/"
        assert resolve("/ingredients/create/").view_name == "ingredients:create"


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
