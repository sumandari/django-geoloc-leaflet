"""django_geoloc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

# for leaflet map
from djgeojson.views import GeoJSONLayerView

from django.contrib.auth.models import User
from userprofile import views
from userprofile.models import Profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserList.as_view(), name='home'),
    path('user/<username>/', views.UserDetail.as_view(), name='user-detail'),
    path('user/<username>/edit', views.UserEdit.as_view(), name='user-edit'),
    path('map/', views.map, name='map'),
    # map
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=Profile, 
                            properties=('user_list', 'phone', 'address')), name='data')




]
