from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("foods/", views.food_list, name="foods"),
    path("foods/<int:id>/", views.food_detail, name="food-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
