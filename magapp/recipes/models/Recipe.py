from django.contrib.auth import get_user_model
from django.db import models
from django.forms import model_to_dict
from django.urls import reverse

from magapp.core.models import DraftModel, ModelBase
from magapp.core.utils import create_unique_slug


class Recipe(DraftModel, ModelBase):
    title = models.CharField("título", max_length=64, help_text="Título da receita.")
    description = models.TextField("descrição", help_text="Breve descrição da receita")
    directions = models.TextField("preparo", help_text="Passos para o preparo.")
    slug = models.SlugField(max_length=64, unique=True, editable=False)
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

    def save(self, *args, **kwargs):
        self.slug = create_unique_slug(self.title)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Recipe({model_to_dict(self)})"

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"slug": self.slug})
