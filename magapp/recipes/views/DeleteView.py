from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from magapp.recipes.models import Recipe


class DeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.edit.DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipes:list")

    def test_func(self):
        if not self.request.user == self.get_object().created_by:
            return False
        return True
