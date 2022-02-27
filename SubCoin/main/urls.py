from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search/', views.search_results, name='search'),
    path('discussion/', views.discussion, name='discussion'),
]
