from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from magapp.ingredients.forms import IngredientForm
from django.contrib import messages

from magapp.ingredients.models import Ingredient


@login_required
def list(request):
    template = 'ingredients/list.html'
    return render(request, template)


class Create(View, LoginRequiredMixin):
    template = 'ingredients/create_modal.html'

    def get(self, request):
        if not request.htmx:
            return HttpResponseNotFound()
        return render(request, self.template, context={'form': IngredientForm()})

    def post(self, request):
        messages.success(request, "Ingrediente criado.")
        form = IngredientForm(request.POST)
        if not form.is_valid(): # nao valida se o slug eh unico
            return render(request, self.template, context={'form': form})

        form.instance.created_by = request.user
        form.save() # erro 500 slug nao eh unico
        return render(request, self.template, status=201)
