"""authproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    # 1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import TemplateView
from authorization.views import AuthListView,AuthDetailView,AuthCreateView,AuthUpdateView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='home.html')),
    re_path(r'^authorizations/$', AuthListView.as_view(), name='auths'),
    re_path(r'^authorizations/(?P<pk>\d+)/$', AuthDetailView.as_view(), name='auth_detail'),
    re_path(r'^authorizations/editauth/(?P<pk>\d+)/$', AuthUpdateView.as_view(), name='auth_update'),
    re_path(r'^authorizations/createauth/$', AuthCreateView.as_view(), name='auth_create'),
    # path('login_now/',LoginView.as_view(),'loginnow'),
     path('accounts/', include('django.contrib.auth.urls')),
]
