from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View


@login_required
def list(request):
    template = 'ingredients/list.html'
    return render(request, template)
