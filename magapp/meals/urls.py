from django.urls import path

from magapp.meals.views import Create, Update, detail, list, recipes_modal, recipes_search

app_name = 'meals'
urlpatterns = [
    path('create/', Create.as_view(), name='create'),
    path('', list, name='list'),
    path('<slug:slug>/', detail, name='detail'),
    path('<slug:slug>/update/', Update.as_view(), name='update'),
    path('partial/recipes/', recipes_modal, name='recipes_modal'),
    path('partial/recipes_search/', recipes_search, name='recipes_search'),
]
