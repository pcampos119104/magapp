from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from magapp.ingredients.forms import IngredientForm
from django.contrib import messages

from magapp.ingredients.models import Ingredient


@login_required
def list(request):
    if not request.htmx:
        # Return the full page if not htmx
        return render(request, 'ingredients/list.html')
    num_per_page = 3
    template = 'ingredients/partials/listing.html'
    # Ingredient.objects.filter(name__unaccent__lower__trigram_similar="banana")
    ingredients = Ingredient.objects.all()
    paginator = Paginator(ingredients, num_per_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, template, {'page_obj': page_obj})


class Create(View, LoginRequiredMixin):
    template = 'ingredients/modals/create.html'

    def get(self, request):
        if not request.htmx:
            return HttpResponseNotFound()
        return render(request, self.template, context={'form': IngredientForm()})

    def post(self, request):
        form = IngredientForm(request.POST)
        if not form.is_valid():
            return render(request, self.template, context={'form': form})

        messages.success(request, "Ingrediente criado.")
        form.instance.created_by = request.user
        form.save()
        return render(request, self.template, status=201)
