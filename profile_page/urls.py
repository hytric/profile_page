"""profile_page URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from profile_page import settings
from webpage.views import Main, Programing, SeTA, Facebook_meta

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view()),
    path('Main', Main.as_view()),
    path('Programing', Programing.as_view()),
    path('SeTA', SeTA.as_view()),
    path('8o2th7vj1zswq2rfw00oh4syua51s1', Facebook_meta.as_view())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)