import uuid

import pytest
from django.urls import reverse

pytestmark = pytest.mark.views


class TestIngredientsViews:
    def test_list_not_logged(self, client):
        resp = client.get(reverse('ingredients:list'))
        assert resp.status_code == 302

    def test_list_logged(self, logged_client):
        resp = logged_client.get(reverse('ingredients:list'))
        assert resp.status_code == 200
