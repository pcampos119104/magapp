from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render


# @login_required
def detail(request):
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    template = 'menus/partials/detail.html'
    # recipe = get_object_or_404(Recipe, slug=slug, owner=request.user)

    context = {
        'base_template': base_template,
        # 'recipe': recipe,
    }
    return render(request, template, context=context)
