from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def list(request):
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    template = 'recipes/partials/listing.html'
    context = {
        'base_template': base_template,
    }
    return render(request, template, context)
