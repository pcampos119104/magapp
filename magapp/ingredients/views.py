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
    # Ingredient.objects.filter(name__unaccent__lower__trigram_similar="banana")
    ingredients = Ingredient.objects.all()
    paginator = Paginator(ingredients, num_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, template, {'page_obj': page_obj, 'base_template': base_template})


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


class Update(View, LoginRequiredMixin):
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
