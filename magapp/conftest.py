import pytest


@pytest.fixture
def created_user(db, django_user_model):
    username = 'user1'
    password = 'b1a2r3a6'
    user = django_user_model.objects.create_user(username=username, password=password)
    return user


@pytest.fixture
def logged_client(db, client, created_user):
    client.force_login(created_user)
    return client
