from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Food
from .serializers import FoodSerializer


@api_view(['GET', 'POST'])
def food_list(request):

    if request.method == 'GET':

        foods = Food.objects.all()
        serilizer = FoodSerializer(foods, many=True)
        return JsonResponse({'foods': serilizers.data})

    if request.method == 'POST':
        serilizer = FoodSerializer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)