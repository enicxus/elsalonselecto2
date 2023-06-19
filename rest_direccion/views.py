from django.shortcuts import render 
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from menu.models import Direccion
from .serializers import direccionSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated))   
@api_view(['GET', 'PUT', 'DELETE'])
def datos_direccion(request):

    """
    TODOS LOS DATOS DE LA DIRECCION
    """

    if request.method == 'GET':
        
        direccion = Direccion.objects.all()
        serializer = direccionSerializer(direccion, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = direccionSerializer(data = data)

        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
def detalle_direccion (request,id):
    """
    get update, o delete
    """
    try:
        direccion=Direccion.objects.get(id_direccion=id)
    except Direccion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=direccionSerializer(direccion)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = direccionSerializer(direccion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DElETE':
        direccion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)