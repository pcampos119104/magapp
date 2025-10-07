import pytest
from django.urls import reverse

pytestmark = pytest.mark.views


class TestListRecipes:
    # todo pagination
    def test_list_not_logged(self, client):
        resp = client.get(reverse('recipes:list'))
        assert resp.status_code == 302

    def test_list_logged(self, logged_client):
        resp = logged_client.get(reverse('recipes:list'))
        assert resp.status_code == 200


class TestCreateRecipes:
    def test_create_not_logged(self, client):
        resp = client.post(reverse('recipes:create'), data={})
        assert resp.status_code == 302

    def test_create_valid_data(self, logged_client, ingredients, metrics, qualifiers):
        valid_data = {
            'title': ['Titulo'],
            'description': ['Descricao'],
            'font': ['https://www.youtube.com/watch?v=NvOqLE8r64g'],
            'directions': ['1. passo 1\n2. passo 2\n3. passo 3'],
            'ingredients-TOTAL_FORMS': '3',
            'ingredients-INITIAL_FORMS': '0',
            'ingredients-MIN_NUM_FORMS': '0',
            'ingredients-MAX_NUM_FORMS': '1000',
            'ingredients-0-qtd': ['11'],
            'ingredients-0-metric': metrics[0].id,
            'ingredients-0-ingredient': ingredients[0].id,
            'ingredients-0-qualifiers': [qualifiers[0].id],
            'ingredients-2-qtd': ['22'],
            'ingredients-2-metric': metrics[1].id,
            'ingredients-2-ingredient': ingredients[1].id,
            'ingredients-2-qualifiers': [qualifiers[1].id, qualifiers[2].id],
            'ingredients-3-qtd': ['33'],
            'ingredients-3-metric': metrics[2].id,
            'ingredients-3-ingredient': ingredients[2].id,
        }
        resp = logged_client.post(reverse('recipes:create'), data=valid_data)
        assert resp.status_code == 201

    def test_create_invalid_data(self, logged_client):
        invalid_data = {'title': 'Test Recipe'}
        resp = logged_client.post(reverse('recipes:create'), data=invalid_data)
        assert resp.status_code == 400
