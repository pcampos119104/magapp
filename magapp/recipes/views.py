from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, QueryDict
from django.shortcuts import get_object_or_404, render
from django.views import View

from magapp.ingredients.models import Ingredient
from magapp.recipes.forms import RecipeForm, RecipeIngredientFormSet
from magapp.recipes.models import Recipe


@login_required
def list(request):
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    template = 'recipes/partials/listing.html'
    context = {
        'base_template': base_template,
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

    def post(self, request):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
        recipe_form = RecipeForm(request.POST)
        ingredient_formset = RecipeIngredientFormSet(request.POST)
        print(request.POST)
        if not any(
            [
                recipe_form.is_valid(),
                ingredient_formset.is_valid(),
            ]
        ):
            print('algum formulario nao eh valido')
            context = {
                'recipe_form': recipe_form,
                'ingredient_formset': ingredient_formset,
                'base_template': base_template,
            }
            return render(request, self.template, context)
        print('form.is_valid()')

        # form.instance.created_by = request.user
        # form.save()
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
        if not request.htmx:
            return HttpResponseNotFound()
        recipe = get_object_or_404(Recipe, slug=slug)
        form = RecipeForm(instance=recipe)
        return render(request, self.template, context={'form': form, 'update': True})

    def put(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)
        payload = QueryDict(request.body)
        form = RecipeForm(payload, instance=recipe)
        # if has not changed compared with original
        if not form.has_changed():
            messages.success(request, 'Receita atualizada.')
            return render(request, self.template, status=204)

        if not form.is_valid():
            return render(request, self.template, context={'form': form, 'update': True})

        form.instance.created_by = request.user
        form.save()
        messages.success(request, 'Receita atualizada.')
        return render(request, self.template, status=204)
