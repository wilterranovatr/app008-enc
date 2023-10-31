"""
URL configuration for app_enc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    ## Path Index
    path('', views.index),
    
    ## Path View Solicitudes
    path('solicitud_nota_credito/punto_venta/', views.notaPDV),
    path('solicitud_nota_credito/financieros/', views.notaFinanciero),
    path('solicitud_nota_credito/servicios/', views.notaServicios),
    ###
    
    ## Path View Consolidacion
    path('consolidacion_nota_credito/punto_venta/', views.cnotaPDV),
    path('consolidacion_nota_credito/financieros/', views.cnotaFinanciero),
    path('consolidacion_nota_credito/servicios/', views.cnotaServicios),
    ###
    
    
    ## Path View Bandeja
    path('bandeja_nota_credito/punto_venta/', views.bnotaPDV),
    path('bandeja_nota_credito/financieros/', views.bnotaFinanciero),
    path('bandeja_nota_credito/servicios/', views.bnotaServicios),
    ###
    
    ###
    path('admin/', admin.site.urls),
    path('oauth2/', include('django_auth_adfs.urls')),
    path('login/',views.login_successful,name='login-view')
    ####
    
]
