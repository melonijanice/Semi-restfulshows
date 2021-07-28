from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.show),
    path('new', views.new_show),
    path('create', views.create_show),
    path('<int:id>', views.view_show),
    path('<int:id>/edit', views.edit_show),
    path('<int:id>/update', views.update_show),
    path('<int:id>/destroy', views.delete_show),
    ]