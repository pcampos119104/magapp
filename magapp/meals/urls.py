from django.urls import path

from magapp.meals.views import Create, Update, detail, list

app_name = 'meals'
urlpatterns = [
    path('create/', Create.as_view(), name='create'),
    path('', list, name='list'),
    path('<slug:slug>/', detail, name='detail'),
    path('<slug:slug>/update/', Update.as_view(), name='update'),
]
