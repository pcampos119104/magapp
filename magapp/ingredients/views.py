from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from magapp.ingredients.forms import IngredientForm
from django.contrib import messages

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
        messages.info(request, "Profile details updated.")
        return render(request, self.template, status=201)
