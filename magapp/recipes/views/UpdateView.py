import logging

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import formset_factory, modelformset_factory
from django.urls import reverse_lazy
from django.views import generic

from magapp.recipes.forms import RecipeForm, RecipeIngredientForm
from magapp.recipes.models import Recipe, RecipeIngredient


class UpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):
    model = Recipe
    form_class = RecipeForm
    success_url = reverse_lazy("recipes:list")
    logger = logging.getLogger(__name__)

    def test_func(self):
        if not self.request.user == self.get_object().created_by:
            return False
        return True

    def get_context_data(self, **kwargs):
        ctx = super(UpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            ctx["form"] = RecipeForm(self.request.POST)
            ctx["ingredient_form"] = RecipeIngredientForm(self.request.POST)
            ctx["ingredient_formset_detail"] = formset_factory(
                RecipeIngredientForm, extra=0
            )(self.request.POST)
        else:
            ctx["form"] = RecipeForm(instance=self.get_object())
            ctx["ingredient_form"] = RecipeIngredientForm()

            ingredient_form_set = modelformset_factory(
                RecipeIngredient, extra=0, form=RecipeIngredientForm
            )
            qset = (
                self.get_object()
                .recipeingredient_set.all()
                .select_related("ingredient")
            )
            ctx["ingredient_formset_detail"] = ingredient_form_set(queryset=qset)
            """
            ctx["ingredient_formset_detail"] = formset_factory(
                RecipeIngredientForm, extra=0
            )()
            """
        return ctx


"""
    def form_valid(self, form):
        self.logger.info("form_valid - START")
        context = self.get_context_data()
        ingredient = context["ingredient"]
        self.logger.debug(f"ingredient.is_valid() {ingredient.is_valid()}")
        self.logger.debug(f"ingredient.errors() {ingredient.errors}")
        if ingredient.is_valid():
            total_form = ingredient.cleaned_data
            # todo Show error validation on template
            if not any("name" in d for d in total_form):
                return self.form_invalid(form)
            ingredient.instance = form.save()
            ingredient.save()
        self.logger.info("form_valid - FINISH")
        return super().form_valid(form)
"""
