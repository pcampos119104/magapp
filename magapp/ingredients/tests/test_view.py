import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

pytestmark = pytest.mark.views


class TestListIngredients:
    # todo pagination
    def test_list_not_logged(self, client):
        resp = client.get(reverse('ingredients:list'))
        assert resp.status_code == 302

    def test_list_logged(self, logged_client):
        resp = logged_client.get(reverse('ingredients:list'))
        assert resp.status_code == 200

    '''
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
    '''


class TestCreateIngredients:
    headers = {'Hx-Request': 'true'}

    def test_not_htmx_call(self, logged_client):
        resp = logged_client.get(reverse('ingredients:create'))
        assert resp.status_code == 404

    def test_not_logged(self, client):
        resp = client.get(reverse('ingredients:create'), headers=self.headers)
        assert resp.status_code == 302

    def test_new_name(self, logged_client):
        payload = {
            'name': 'Test name 2'
        }
        resp = logged_client.post(
            reverse('ingredients:create'),
            data=payload,
            headers=self.headers
        )
        assert resp.status_code == 201

    def test_try_already_exists_name(self, logged_client, ingredient):
        payload = {
            'name': ingredient.name
        }
        resp = logged_client.post(
            reverse('ingredients:create'),
            data=payload,
            headers=self.headers
        )
        assertContains(resp, 'Este ingrediente já existe.', status_code=200)

    def test_create(self, client):
        pass
# update
#
#
#
#
