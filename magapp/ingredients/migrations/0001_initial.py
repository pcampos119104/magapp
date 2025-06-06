# Generated by Django 5.0.2 on 2024-04-10 10:50

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import magapp.base.utils.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                (
                    'deleted_at',
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'name',
                    magapp.base.utils.models.LowerCharField(
                        error_messages={'unique': 'Este ingrediente já existe.'},
                        help_text='Ingrediente e quantidade',
                        max_length=64,
                        unique=True,
                        verbose_name='nome',
                    ),
                ),
                (
                    'slug',
                    models.SlugField(
                        editable=False,
                        error_messages={'unique': 'Este slug já existe.'},
                        max_length=64,
                        unique=True,
                    ),
                ),
                (
                    'created_by',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'verbose_name': 'ingrediente',
                'verbose_name_plural': 'ingredientes',
                'ordering': ['name'],
            },
        ),
        migrations.AddConstraint(
            model_name='ingredient',
            constraint=models.UniqueConstraint(models.F('slug'), name='unique_ingredient_slug'),
        ),
    ]
