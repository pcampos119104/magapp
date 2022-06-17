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

from magapp.ingredients import views

app_name = "ingredients"
urlpatterns = [
    path("create/", views.ingredient_create, name="create"),
    path("<slug:slug>/update/", views.ingredient_update, name="update"),
    path("", views.ListView.as_view(), name="list"),
    path("<slug:slug>", views.ingredient_detail, name="detail"),
    # path("<uuid:pk>/delete/", views.DeleteView.as_view(), name="delete"),
]
