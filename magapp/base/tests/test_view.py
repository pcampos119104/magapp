import uuid

import pytest
from django.urls import reverse

pytestmark = pytest.mark.views


class TestBaseViews:
    def test_home(self, client):
        resp = client.get(reverse('base:home'))
        assert resp.status_code == 200
