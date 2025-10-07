from django.shortcuts import render
from django.views import View


class HomeView(View):
    """View da página inicial do site.

    Responsável por renderizar o template base/home.html.
    """

    def get(self, request, *args, **kwargs):
        """Responde a requisições GET da home.

        Parâmetros:
            request: HttpRequest recebido.
            *args: Argumentos posicionais adicionais.
            **kwargs: Argumentos nomeados adicionais.

        Retorna:
            HttpResponse: Template renderizado base/home.html.
        """
        return render(request, 'base/home.html')
