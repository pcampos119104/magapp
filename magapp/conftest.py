import uuid

import pytest
from model_bakery import baker


@pytest.fixture
def created_user(db, django_user_model):
    username = 'user1'
    password = 'b1a2r3a6'
    user = django_user_model.objects.create_user(username=username, password=password)
    return user

@pytest.fixture
def user_a(db, django_user_model):
    username = 'user_a'
    password = 'b1a2r3a6'
    user = django_user_model.objects.create_user(username=username, password=password)
    return user

@pytest.fixture
def user_b(db, django_user_model):
    username = 'user_b'
    password = 'b1a2r3a6'
    user = django_user_model.objects.create_user(username=username, password=password)
    return user

@pytest.fixture
def logged_client(db, client, created_user):
    client.force_login(created_user)
    return client


def gen_lower_char_field():
    return uuid.uuid4().hex[0:16]


baker.generators.add('magapp.base.utils.models.LowerCharField', gen_lower_char_field)
