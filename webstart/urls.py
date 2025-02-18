from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('select/', views.select, name = 'select'),
    path('result/', views.result, name = 'result'),
]