"""
URL configuration for magapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
import django


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('magapp.base.urls')),
    path('ingredients/', include('magapp.ingredients.urls')),
    # django browser reload
    path('__reload__/', include('django_browser_reload.urls')),
]

# for testing the 400, 404, 500 pages layout
if settings.DEBUG:
    def custom_page_not_found(request):
        return django.views.defaults.page_not_found(request, None)


    def custom_page_bad_request(request):
        return django.views.defaults.bad_request(request, None)


    def custom_server_error(request):
        return django.views.defaults.server_error(request)


    urlpatterns += [
        path("404/", custom_page_not_found),
        path("400/", custom_page_bad_request),
        path("500/", custom_server_error),
    ]
