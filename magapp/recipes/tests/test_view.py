import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

pytestmark = pytest.mark.views


class TestListRecipes:
    # todo pagination
    def test_list_not_logged(self, client):
        resp = client.get(reverse('recipes:list'))
        assert resp.status_code == 302

    def test_list_logged(self, logged_client):
        resp = logged_client.get(reverse('recipes:list'))
        assert resp.status_code == 200


#
#
#
#
