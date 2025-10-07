import django
from django.conf import settings
from django.contrib import admin
from django.urls import include, path


def trigger_error(request):
    """Lança propositalmente ZeroDivisionError para testar Sentry e tratamento de erros.

    Parâmetros:
        request: Objeto HttpRequest.

    Retorna:
        Nunca retorna; sempre levanta uma exceção.
    """
    division_by_zero = 1 / 0


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('magapp.base.urls')),
    path('ingredients/', include('magapp.ingredients.urls')),
    path('recipes/', include('magapp.recipes.urls')),
    path('menus/', include('magapp.menus.urls')),
    path('meals/', include('magapp.meals.urls')),
    # django browser reload
    path('__reload__/', include('django_browser_reload.urls')),
]

# for testing the 400, 404, 500 pages layout
if settings.DEBUG:
    def custom_page_not_found(request):
        """Retorna a página 404 de teste quando DEBUG está ativo.

        Parâmetros:
            request: Objeto HttpRequest da requisição.

        Retorna:
            HttpResponse: Resposta 404 gerada pela view padrão do Django.
        """
        return django.views.defaults.page_not_found(request, None)


    def custom_page_bad_request(request):
        """Retorna a página 400 de teste quando DEBUG está ativo.

        Parâmetros:
            request: Objeto HttpRequest da requisição.

        Retorna:
            HttpResponse: Resposta 400 gerada pela view padrão do Django.
        """
        return django.views.defaults.bad_request(request, None)


    def custom_server_error(request):
        """Retorna a página 500 de teste quando DEBUG está ativo.

        Parâmetros:
            request: Objeto HttpRequest da requisição.

        Retorna:
            HttpResponse: Resposta 500 gerada pela view padrão do Django.
        """
        return django.views.defaults.server_error(request)


    urlpatterns += [
        path('404/', custom_page_not_found),
        path('400/', custom_page_bad_request),
        path('500/', custom_server_error),
    ]
