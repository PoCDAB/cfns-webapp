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
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from djgeojson.views import GeoJSONLayerView

from webapp.models import aisDecoded

from webapp import views, API

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', API.UserViewSet)
router.register(r'groups', API.GroupViewSet)
router.register(r'ais', API.AisViewSet)

# Errors handlers
handler404 = 'webapp.views.handler404'
handler500 = 'webapp.views.handler500'

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', views.homeView, name='home'),
    url(r'^login/$', views.loginView, name='login'),
    url(r'^logout/$', views.loggedoutView, name='logout'),
    url(r'^profile/$', views.profileView, name='profile'),
    url(r'^geoview/$', views.geomapView, name='geoview'),
    url(r'^api/V1/', include(router.urls), name='api-root'),
    url(r'^ais-data$', views.decoded_ais_dataset, name='ais-data')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
