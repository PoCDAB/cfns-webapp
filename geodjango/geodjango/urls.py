"""geodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.gis import admin
from django.conf.urls import url, include
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings
from webapp import views

# Errors handlers
handler404 = 'webapp.views.handler404'
handler500 = 'webapp.views.handler500'

urlpatterns = [
    url(r'^admin', admin.site.urls, name='admin'),
    url(r'^$', views.home_page, name='home'),
    url(r'^worldborders', views.world_borders_page, name = 'world_borders'),
    url(r'^api', views.api_page, name = 'api' ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

