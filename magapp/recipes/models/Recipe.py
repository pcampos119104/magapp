from django.contrib.auth import get_user_model
from django.db import models
from django.forms import model_to_dict
from django.template.defaultfilters import slugify
from django.urls import reverse

from magapp.core.models import ModelBase


class Recipe(ModelBase):
    title = models.CharField("título", max_length=64, help_text="Título da receita.")
    directions = models.TextField("preparo", help_text="Passos para o preparo.")
    slug = models.SlugField(max_length=64, unique=True)
    ingredients = models.ManyToManyField(
        "ingredients.Ingredient", through="recipes.RecipeIngredient"
    )
    created_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=False
    )
    font = models.CharField(
        "Fonte",
        max_length=64,
        help_text="Livro de receita, link do youtube e etc.",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "receita"
        verbose_name_plural = "receitas"

    # todo make slug unique even with same title
    def save(self, *args, **kwargs):
        self.slug = get_unique_slug(self.pk, self.title, Recipe.all_objects)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Recipe({model_to_dict(self)})"

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"slug": self.slug})


def get_unique_slug(pk, title, manager):
    slug = slugify(title)
    unique_slug = slug
    counter = 2
    while manager.filter(slug=unique_slug).exists():
        if manager.filter(slug=unique_slug).values("pk")[0]["pk"] == pk:
            break
        unique_slug = "{}-{}".format(slug, counter)
        counter += 1
    return unique_slug
