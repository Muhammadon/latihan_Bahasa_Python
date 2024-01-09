from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post/<slug:slug>', views.detail),
    path('category/<str:category_post>', views.category_post)
]