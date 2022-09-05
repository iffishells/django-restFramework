from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Drink
from .serializers import DrinkSerializer


@api_view(['GET', 'POST'])
def get_drinks_list(request, format=None):
    if request.method == 'GET':
        Drinks = Drink.objects.all()
        serializer = DrinkSerializer(Drinks, many=True)
        return JsonResponse({'Serializer-object': serializer.data})
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'Delete', 'GET'])
def get_drink_details(request, id, format=None):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'Delete':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
