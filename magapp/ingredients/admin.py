from django.contrib import admin

# Register your models here.
from magapp.ingredients.models import Ingredient

admin.site.register(Ingredient)
