from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, render
from django.views import View

from magapp.meals.forms import MealForm


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


# @login_required
def detail(request):
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    template = 'meals/partials/detail.html'
    # recipe = get_object_or_404(Recipe, slug=slug, owner=request.user)

    context = {
        'base_template': base_template,
        # 'recipe': recipe,
    }
    return render(request, template, context=context)
