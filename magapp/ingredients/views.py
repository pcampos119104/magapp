from django.shortcuts import render
from django.views import View


def list(request):
    template = 'ingredients/list.html'
    return render(request, template)
