from django.conf.urls import url
from django.contrib import admin
from aplicacion import views

urlpatterns = [
    url(r'^$', views.prenda, name='index'),
    url(r'^prenda/', views.prenda, name='prenda'),

]
