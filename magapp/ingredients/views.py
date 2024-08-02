from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, QueryDict
from django.shortcuts import get_object_or_404, render
from django.views import View

from magapp.ingredients.forms import IngredientForm
from magapp.ingredients.models import Ingredient


@login_required
def list(request):
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    num_per_page = 10
    template = 'ingredients/partials/listing.html'
    search_term = request.GET.get('search', '')
    # postgres full text search https://medium.com/django-unleashed/mastering-full-text-search-enhancing-search-functionality-in-django-74f7f0f2d6a8
    ingredients = Ingredient.objects.filter(name__unaccent__icontains=search_term)
    paginator = Paginator(ingredients, num_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'base_template': base_template,
        'search_term': search_term,
    }
    return render(request, template, context)


class Create(LoginRequiredMixin, View):
    template = 'ingredients/modals/create_update.html'

    def get(self, request):
        if not request.htmx:
            return HttpResponseNotFound()
        return render(request, self.template, context={'form': IngredientForm()})

    def post(self, request):
        form = IngredientForm(request.POST)
        if not form.is_valid():
            return render(request, self.template, context={'form': form})

        form.instance.created_by = request.user
        form.save()
        messages.success(request, 'Ingrediente criado.')
        return render(request, self.template, status=201)


class Update(LoginRequiredMixin, View):
    template = 'ingredients/modals/create_update.html'

    def get(self, request, slug):
        if not request.htmx:
            return HttpResponseNotFound()
        ingredient = get_object_or_404(Ingredient, slug=slug)
        form = IngredientForm(instance=ingredient)
        return render(request, self.template, context={'form': form, 'update': True})

    def put(self, request, slug):
        ingredient = get_object_or_404(Ingredient, slug=slug)
        payload = QueryDict(request.body)
        form = IngredientForm(payload, instance=ingredient)
        # if has not changed compared with original
        if not form.has_changed():
            messages.success(request, 'Ingrediente atualizado.')
            return render(request, self.template, status=204)

        if not form.is_valid():
            return render(request, self.template, context={'form': form, 'update': True})

        form.instance.created_by = request.user
        form.save()
        messages.success(request, 'Ingrediente atualizado.')
        return render(request, self.template, status=204)


class Delete(View, LoginRequiredMixin):
    """
    For now delete only on admin.
    todo create profile for deleting ingredient
    """

    pass


def search_ingredients_selector(request):
    search_term = request.GET.get('search', '')
    if search_term:
        ingredients = Ingredient.objects.filter(name__unaccent__icontains=search_term)[:7]
    else:
        ingredients = Ingredient.objects.all()[:7]

    template = 'recipes/partials/ingredient_search_selector.html'
    context = {
        'ingredients': ingredients,
    }
    return render(request, template, context)
