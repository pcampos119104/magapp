# Generated by Django 3.1.13 on 2021-11-18 11:00

import uuid

import django.db.models.deletion
import model_utils.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Título da receita.', max_length=64, verbose_name='título')),
                ('directions', models.TextField(help_text='Passos para o preparo.', verbose_name='preparo')),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('font', models.CharField(blank=True, help_text='Livro de receita, link do youtube e etc.', max_length=64, null=True, verbose_name='Fonte')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'receita',
                'verbose_name_plural': 'receitas',
            },
        ),
    ]
