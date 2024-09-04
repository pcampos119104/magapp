from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db import transaction
from django.http import QueryDict
from django.shortcuts import get_object_or_404, render
from django.views import View

from magapp.recipes.forms import RecipeForm, RecipeIngredientFormSet
from magapp.recipes.models import Recipe


@login_required
def list(request):
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    qtd_per_page = 10
    template = 'recipes/partials/listing.html'
    search_term = request.GET.get('search', '')
    recipes = Recipe.objects.filter(title__unaccent__icontains=search_term)
    paginator = Paginator(recipes, qtd_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'base_template': base_template,
        'page_obj': page_obj,
        'search_term': search_term,
    }
    return render(request, template, context)


class Create(LoginRequiredMixin, View):
    template = 'recipes/partials/create_update.html'

    def get(self, request):
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        recipe_form = RecipeForm()
        ingredient_formset = RecipeIngredientFormSet()
        context = {
            'recipe_form': recipe_form,
            'ingredient_formset': ingredient_formset,
            'base_template': base_template,
        }
        return render(request, self.template, context)

    @transaction.atomic
    def post(self, request):
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        recipe_form = RecipeForm(request.POST)
        ingredient_formset = RecipeIngredientFormSet(request.POST)
        # validar os formularios
        if any(
            [
                not recipe_form.is_valid(),
                not ingredient_formset.is_valid(),
            ]
        ):
            # Nao passou na validacao, retorna o form com o erro.
            context = {
                'recipe_form': recipe_form,
                'ingredient_formset': ingredient_formset,
                'base_template': base_template,
            }
            return render(request, self.template, context, status=400)

        # salva os formularios
        recipe_form.instance.created_by = request.user
        recipe = recipe_form.save()
        for form in ingredient_formset:
            if form.has_changed():
                form.instance.recipe = recipe
                form.save()

        # reset forms
        recipe_form = RecipeForm()
        ingredient_formset = RecipeIngredientFormSet()
        context = {
            'recipe_form': recipe_form,
            'ingredient_formset': ingredient_formset,
            'base_template': base_template,
        }
        messages.success(request, 'Receita criada.')
        return render(request, self.template, context, status=201)


class Update(LoginRequiredMixin, View):
    template = 'recipes/partials/create_update.html'

    def get(self, request, slug):
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        recipe = get_object_or_404(Recipe, slug=slug)
        recipe_form = RecipeForm(instance=recipe)
        ingredient_formset = RecipeIngredientFormSet(instance=recipe)
        print('################################################')
        print(recipe_form)
        print(ingredient_formset)
        context = {
            'recipe_form': recipe_form,
            'ingredient_formset': ingredient_formset,
            'base_template': base_template,
            'update': True,
        }
        return render(request, self.template, context=context)

    def put(self, request, slug):
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        recipe = get_object_or_404(Recipe, slug=slug)
        payload = QueryDict(request.body)
        recipe_form = RecipeForm(payload, instance=recipe)
        ingredient_formset = RecipeIngredientFormSet(payload, instance=recipe)

        # se nao houver mudanca, nao faz nada e notifica atualizacao
        if any([not recipe_form.has_changed(), not ingredient_formset.has_changed()]):
            messages.success(request, 'Receita atualizada.')
            # reset forms
            recipe_form = RecipeForm()
            ingredient_formset = RecipeIngredientFormSet()
            context = {
                'recipe_form': recipe_form,
                'ingredient_formset': ingredient_formset,
                'base_template': base_template,
                'update': True,
            }

            return render(request, self.template, context, status=204)

        # validar os formularios
        if any(
            [
                not recipe_form.is_valid(),
                not ingredient_formset.is_valid(),
            ]
        ):
            # Nao passou na validacao, retorna o form com o erro.
            context = {
                'recipe_form': recipe_form,
                'ingredient_formset': ingredient_formset,
                'base_template': base_template,
                'update': True,
            }
            return render(request, self.template, context, status=400)

        recipe = recipe_form.save()
        for form in ingredient_formset:
            if form.has_changed():
                form.instance.recipe = recipe
                form.save()

        messages.success(request, 'Receita atualizada.')
        return render(request, self.template, status=204)
