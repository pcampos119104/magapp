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
    """Lista ingredientes com paginação e filtro por nome.

    Parâmetros:
        request: HttpRequest contendo parâmetros de consulta (search, page) e flag HTMX.

    Retorna:
        HttpResponse: Template de listagem com page_obj e termo de busca no contexto.
    """
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    qtd_per_page = 10
    template = 'ingredients/partials/listing.html'
    search_term = request.GET.get('search', '')
    # postgres full text search https://medium.com/django-unleashed/mastering-full-text-search-enhancing-search-functionality-in-django-74f7f0f2d6a8
    ingredients = Ingredient.objects.filter(name__unaccent__icontains=search_term)
    paginator = Paginator(ingredients, qtd_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'base_template': base_template,
        'search_term': search_term,
    }
    return render(request, template, context)


class Create(LoginRequiredMixin, View):
    """Cria um novo ingrediente via modal HTMX."""

    template = 'ingredients/modals/create_update.html'

    def get(self, request):
        """Exibe o formulário de criação de ingrediente.

        Retorna:
            HttpResponse: Conteúdo HTML do formulário para uso em modal HTMX.
        """
        if not request.htmx:
            return HttpResponseNotFound()
        return render(request, self.template, context={'form': IngredientForm()})

    def post(self, request):
        """Processa o envio do formulário de criação de ingrediente.

        Retorna:
            HttpResponse: Em caso de sucesso, retorna 201; em caso de erro, o formulário com validações.
        """
        form = IngredientForm(request.POST)
        if not form.is_valid():
            return render(request, self.template, context={'form': form})

        form.instance.owner = request.user
        form.save()
        messages.success(request, 'Ingrediente criado.')
        return render(request, self.template, status=201)


class Update(LoginRequiredMixin, View):
    """Atualiza um ingrediente existente via modal HTMX."""

    template = 'ingredients/modals/create_update.html'

    def get(self, request, slug):
        """Exibe o formulário de edição de ingrediente.

        Parâmetros:
            slug (str): Slug do ingrediente a ser editado.

        Retorna:
            HttpResponse: Formulário preenchido para edição.
        """
        if not request.htmx:
            return HttpResponseNotFound()
        ingredient = get_object_or_404(Ingredient, slug=slug)
        form = IngredientForm(instance=ingredient)
        return render(request, self.template, context={'form': form, 'update': True})

    def put(self, request, slug):
        """Processa a atualização de um ingrediente.

        Retorna:
            HttpResponse: 204 quando não há alterações ou após atualização bem-sucedida;
            200 com formulário em caso de erros.
        """
        ingredient = get_object_or_404(Ingredient, slug=slug)
        payload = QueryDict(request.body)
        form = IngredientForm(payload, instance=ingredient)
        # if has not changed compared with original
        if not form.has_changed():
            messages.success(request, 'Ingrediente atualizado.')
            return render(request, self.template, status=204)

        if not form.is_valid():
            return render(request, self.template, context={'form': form, 'update': True})

        form.instance.owner = request.user
        form.save()
        messages.success(request, 'Ingrediente atualizado.')
        return render(request, self.template, status=204)


class Delete(View, LoginRequiredMixin):
    """For now delete only on admin.
    todo create profile for deleting ingredient
    """

    pass


def search_ingredients_selector(request):
    """Busca ingredientes para o seletor de receitas (autocomplete/HTMX).

    Parâmetros:
        request: HttpRequest com o parâmetro de busca 'search'.

    Retorna:
        HttpResponse: Fragmento HTML com a lista de resultados limitados.
    """
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
