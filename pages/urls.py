# myapp/urls.py

from django.urls import path
from .views import add_user_info

urlpatterns = [
    path('add/', add_user_info, name='add_user_info'),
]
