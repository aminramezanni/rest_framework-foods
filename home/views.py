from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Food
from .serializers import FoodSerializer


@api_view(['GET', 'POST'])
def food_list(request, format=None):

    if request.method == 'GET':
        foods = Food.objects.all()
        serilizer = FoodSerializer(foods, many=True)
        return Response(serilizer.data)

    if request.method == 'POST':
        serilizer = FoodSerializer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def food_detail(request, id, format=None):

    try:
        food = Food.objects.get(pk=id)
    except Food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)