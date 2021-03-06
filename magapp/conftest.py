import pytest
from model_bakery import baker

from magapp.ingredients.models import Ingredient
from magapp.recipes.models import Metric, Recipe
from magapp.users.models import User
from magapp.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def logged_client(db, client, created_user):
    client.force_login(created_user)
    return client


@pytest.fixture
def created_user(db, django_user_model):
    username = "user1"
    password = "b1a2r3a6"
    user = django_user_model.objects.create_user(username=username, password=password)
    return user


@pytest.fixture
def recipe(db) -> Recipe:
    model = baker.make(
        Recipe,
        _fill_optional=True,
        title="Bolo de cenoura",
        slug="bolo-de-cenoura-asdf",
        deleted_at=None,
    )
    return model


@pytest.fixture
def ingredient(db, recipe) -> Ingredient:
    model = baker.make(
        Ingredient, name="Farinha", slug="farinha-asdf", deleted_at=None, recipe=recipe
    )
    return model


@pytest.fixture
def metric(db) -> Metric:
    model = baker.make(Metric, deleted_at=None)
    return model
