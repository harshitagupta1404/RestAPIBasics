"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from core import views as core_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', core_views.test_view, name='test_view')
    #path('', core_views.TestView.as_view(), name='test_view'),
    path('', core_views.PostView.as_view(), name='post_view'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('rest-auth/', include('rest_auth.urls'))
]
