from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('add/', add_book, name="add_book"),
    path('edit/<int:pk>', edit_book, name="edit_book"),
    path('delete/<int:pk>', delete_book, name="delete_book"),
]