from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import View

from magapp.meals.forms import MealForm


@login_required
def list(request):
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    template = 'meals/partials/listing.html'
    # qtd_per_page = 10
    # search_term = request.GET.get('search', '')
    # recipes = Recipe.objects.filter(owner=request.user).filter(title__unaccent__icontains=search_term)
    # paginator = Paginator(recipes, qtd_per_page)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'base_template': base_template,
        # 'page_obj': page_obj,
        # 'search_term': search_term,
    }
    return render(request, template, context)


class Create(LoginRequiredMixin, View):
    template = 'meals/partials/create_update.html'

    def get(self, request):
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        meal_form = MealForm()
        context = {
            'meal_form': meal_form,
            'base_template': base_template,
        }
        return render(request, self.template, context)

    @transaction.atomic
    def post(self, request):
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        meal_form = MealForm(request.POST)
        # validar os formularios
        if not meal_form.is_valid():
            # Nao passou na validacao, retorna o form com o erro.
            context = {
                'meal_form': meal_form,
                'base_template': base_template,
            }
            return render(request, self.template, context, status=400)

        # salva os formularios
        meal_form.instance.owner = request.user
        meal_form.save()

        # reset forms
        meal_form = MealForm()
        context = {
            'meal_form': meal_form,
            'base_template': base_template,
        }
        messages.success(request, 'Refeição criada.')
        return render(request, self.template, context, status=201)

class Update(LoginRequiredMixin, View):
    template = 'meals/partials/create_update.html'

    def get(self, request, slug):
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        # recipe = get_object_or_404(Recipe, slug=slug, owner=request.user)
        # recipe_form = RecipeForm(instance=recipe)
        # ingredient_formset = RecipeIngredientFormSet(instance=recipe)
        context = {
            # 'recipe_form': recipe_form,
            # 'ingredient_formset': ingredient_formset,
            'base_template': base_template,
            # 'update': True,
        }
        return render(request, self.template, context=context)

    def put(self, request, slug):
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        '''
        # recipe = get_object_or_404(Recipe, slug=slug, owner=request.user)
        # payload = QueryDict(request.body)
        # recipe_form = RecipeForm(payload, instance=recipe)
        # ingredient_formset = RecipeIngredientFormSet(payload, instance=recipe)
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
        '''
        return redirect(reverse('recipes:list'))

# @login_required
def detail(request, slug):
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    template = 'meals/partials/detail.html'
    # recipe = get_object_or_404(Recipe, slug=slug, owner=request.user)

    context = {
        'base_template': base_template,
        # 'recipe': recipe,
    }
    return render(request, template, context=context)
