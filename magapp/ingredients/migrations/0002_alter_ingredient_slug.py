# Generated by Django 4.0.4 on 2022-05-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='slug',
            field=models.SlugField(editable=False, max_length=64, unique=True),
        ),
    ]
