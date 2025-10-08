from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db import transaction
from django.http import QueryDict
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from magapp.recipes.forms import RecipeForm, RecipeIngredientFormSet
from magapp.recipes.models import Recipe


@login_required
def list(request):
    """Lista receitas do usuário com paginação e filtro por título.

    Parâmetros:
        request: HttpRequest com parâmetros 'search' e 'page', e flag HTMX.

    Retorna:
        HttpResponse: Template de listagem com objetos paginados.
    """
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    qtd_per_page = 10
    template = 'recipes/partials/listing.html'
    search_term = request.GET.get('search', '')
    recipes = Recipe.objects.filter(owner=request.user).filter(title__unaccent__icontains=search_term)
    paginator = Paginator(recipes, qtd_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'base_template': base_template,
        'page_obj': page_obj,
        'search_term': search_term,
    }
    return render(request, template, context)


@login_required
def detail(request, slug):
    """Exibe o detalhe de uma receita do usuário.

    Parâmetros:
        slug (str): Identificador (slug) da receita.

    Retorna:
        HttpResponse: Template com dados da receita.
    """
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    template = 'recipes/partials/detail.html'
    recipe = get_object_or_404(Recipe, slug=slug, owner=request.user)

    context = {
        'base_template': base_template,
        'recipe': recipe,
    }
    return render(request, template, context=context)


class Create(LoginRequiredMixin, View):
    """Cria uma nova receita com ingredientes relacionados."""

    template = 'recipes/partials/create_update.html'

    def get(self, request):
        """Exibe o formulário de criação de receita e seus ingredientes."""
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
        """Processa a criação de uma receita e seus ingredientes.

        Retorna:
            HttpResponse: 201 em caso de sucesso; 400 com formulários e erros de validação.
        """
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
        recipe = recipe_form.save(commit=False)
        recipe.owner = request.user
        recipe.save()
        for form in ingredient_formset:
            if form.has_changed():
                form.instance.recipe = recipe
                form.save()
        recipe_form.save_m2m()

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
    """Atualiza uma receita existente e seus ingredientes."""

    template = 'recipes/partials/create_update.html'

    def get(self, request, slug):
        """Exibe os formulários de edição de receita e ingredientes."""
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        recipe = get_object_or_404(Recipe, slug=slug, owner=request.user)
        recipe_form = RecipeForm(instance=recipe)
        ingredient_formset = RecipeIngredientFormSet(instance=recipe)
        context = {
            'recipe_form': recipe_form,
            'ingredient_formset': ingredient_formset,
            'base_template': base_template,
            'update': True,
        }
        return render(request, self.template, context=context)

    def put(self, request, slug):
        """Processa a atualização de uma receita e seus ingredientes.

        Retorna:
            HttpResponseRedirect: Redireciona para a listagem após atualização.
        """
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        recipe = get_object_or_404(Recipe, slug=slug, owner=request.user)
        payload = QueryDict(request.body)
        recipe_form = RecipeForm(payload, instance=recipe)
        ingredient_formset = RecipeIngredientFormSet(payload, instance=recipe)
        # se nao houver mudanca, nao faz nada e notifica atualizacao
        if all([not recipe_form.has_changed(), not ingredient_formset.has_changed()]):
            messages.success(request, 'Receita atualizada.')
            return redirect(reverse('recipes:list'))

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

        recipe_form.save()
        ingredient_formset.save()

        messages.success(request, 'Receita atualizada.')
        return redirect(reverse('recipes:list'))
