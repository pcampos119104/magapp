from django.contrib import admin

from magapp.recipes.models import Metric, Qualifier, Recipe, RecipeIngredient

admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Metric)
admin.site.register(Qualifier)
