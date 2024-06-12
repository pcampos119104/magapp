from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, QueryDict
from django.shortcuts import get_object_or_404, render
from django.views import View

from magapp.recipes.forms import RecipeForm
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
    template = 'recipes/modals/create_update.html'

    def get(self, request):
        if not request.htmx:
            return HttpResponseNotFound()
        return render(request, self.template, context={'form': RecipeForm()})

    def post(self, request):
        form = RecipeForm(request.POST)
        if not form.is_valid():
            return render(request, self.template, context={'form': form})

        form.instance.created_by = request.user
        form.save()
        messages.success(request, 'Receita criada.')
        return render(request, self.template, status=201)


class Update(LoginRequiredMixin, View):
    template = 'recipes/modals/create_update.html'

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
