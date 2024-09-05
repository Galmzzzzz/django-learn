from django.urls import path
from . import views
urlpatterns = [
    path('', views.mews, name='mews'),
    path('create/', views.create, name='create'),
]
