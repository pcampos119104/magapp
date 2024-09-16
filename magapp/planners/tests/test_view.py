import pytest
from django.urls import reverse

from magapp.ingredients.tests.conftest import ingredients

pytestmark = pytest.mark.views


class TestListPlanners:
    # todo pagination
    def test_list_not_logged(self, client):
        resp = client.get(reverse('planners:list'))
        assert resp.status_code == 302

    def test_list_logged(self, logged_client):
        resp = logged_client.get(reverse('planners:list'))
        assert resp.status_code == 200
