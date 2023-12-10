from django.urls import path
from . import views

urlpatterns = [
    path('handle_search_get/', views.handle_search_get, name='handle_search_get'),
    path('handle_search_post/', views.handle_search_post, name='handle_search_post'),
    path('', views.index),
]
