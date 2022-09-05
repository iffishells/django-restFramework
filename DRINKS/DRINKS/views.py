from django.http import JsonResponse

from .models import Drink
from .serializers import DrinkSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def get_drinks_list(request):
    if request.method == 'GET':
        Drinks = Drink.objects.all()
        serializer = DrinkSerializer(Drinks, many=True)
        return JsonResponse({'Serializer-object': serializer.data})
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
