"""paypal URL Configuration

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
from django.contrib import admin
from django.http import request
from django.shortcuts import render
from django.urls import path

from paypal_api.controller.main import Main
from paypal_api.controller.paypal_recv import PaypalRecv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paypal-transaction-complete', PaypalRecv.as_view()),
    path('paypal', PaypalRecv.as_view()),
    path('', Main.as_view()),
]
