from typing import List

from magapp.ingredients.models import Ingredient
from magapp.recipes.models import Recipe


def list_recipes() -> List[Recipe]:
    """
    List recipes
    :return:
    """
    return list(Recipe.objects.all())


def get_ingredients_by_recipe(recipe: Recipe) -> List[Ingredient]:
    return list(recipe.recipeingredient_set.all())


def get_recipe(slug: str) -> Recipe:
    return Recipe.objects.get(slug=slug)


def create_recipe(recipe: Recipe) -> None:
    recipe.save()


def list_recipe_ingredients(recipe: Recipe) -> List[Ingredient]:
    return recipe.recipeingredient_set.all()
