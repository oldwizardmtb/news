from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('category/<category_id>', get_category)
]