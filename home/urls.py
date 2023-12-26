from django.urls import path
from . import views


urlpatterns = [
    path("foods/", views.food_list, name="foods"),
]
