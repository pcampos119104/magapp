from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


@login_required
def list(request):
    template = 'ingredients/list.html'
    return render(request, template)


class Create(View, LoginRequiredMixin):
    template_name = 'ingredients/create_modal.html'

    def get(self, request):
        return render(request, self.template_name)
