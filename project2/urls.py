"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1.views import *
from app2.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1f1/',app1f1,name='app1f1'),
    path('app1f2/',app1f2,name='app1f2'),
    path('app2f1/',app2f1,name='app2f1'),
    path('app2f2/',app2f2,name='app2f2'),
]
