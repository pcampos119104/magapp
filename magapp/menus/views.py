from django.shortcuts import render


# @login_required
def detail(request):
    """Detalhe do menu (placeholder)."""
    base_template = 'base/_partial_base.html' if request.htmx else 'base/_base.html'
    template = 'menus/partials/detail.html'
    # recipe = get_object_or_404(Recipe, slug=slug, owner=request.user)

    context = {
        'base_template': base_template,
        # 'recipe': recipe,
    }
    return render(request, template, context=context)
