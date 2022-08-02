from django.contrib import admin

from magapp.ingredients.models import Ingredient, Qualifier

admin.site.register(Ingredient)
admin.site.register(Qualifier)
