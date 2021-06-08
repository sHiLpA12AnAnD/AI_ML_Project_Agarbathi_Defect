import kwargs as kwargs
from django.urls import path
from . import views
from dashapp.dash_apps.finished_apps import stackbar, piechart

urlpatterns = [
    path('', views.index, name='index'),
]
