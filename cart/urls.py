from django.urls import path
from .views import *

urlpatterns = [
    path('show-items',show_items, name = "show_items"),
]
