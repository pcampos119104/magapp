"""magapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from magapp.recipes import views

app_name = "recipes"
urlpatterns = [
    path("create/", views.recipe_create, name="create"),
    path("htmx/create/step-1/", views.partial_add_step_1, name="partial_add_step_1"),
    path(
        "htmx/create/step-2/<slug:slug>/",
        views.partial_add_step_2,
        name="partial_add_step_2",
    ),
    path("", views.ListView.as_view(), name="list"),
    path("<slug:slug>", views.DetailView.as_view(), name="detail"),
    # path("<uuid:pk>/update/", views.UpdateView.as_view(), name="update"),
    # path("<uuid:pk>/delete/", views.DeleteView.as_view(), name="delete"),
    path(
        "htmx/ingredient-form/<slug:slug>/",
        views.add_recipeingredient,
        name="partial_add_recipeingredient",
    ),
]