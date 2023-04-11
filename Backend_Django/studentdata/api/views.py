from django.shortcuts import render, redirect
from .models import StudentModal
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# class StudentList(ListAPIView):
#     queryset= StudentModal.objects.all()
#     serializer_class = StudentSerializers


# class StudentAdd(ListAPIView):
#     queryset= StudentModal.objects.all()
#     serializer_class = StudentSerializers




@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def api(request, pk= None):
    
    if request.method== 'GET':
        if pk is not None:
            obj= StudentModal.objects.get(id=pk)
            serializer= StudentSerializers(obj)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        obj= StudentModal.objects.all()
        serializer= StudentSerializers(obj, many= True)
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
    elif request.method== 'POST':
        data= request.data
        serializer= StudentSerializers(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method== 'PUT':
        id= request.data.get('id')
        obj= StudentModal.objects.get(pk=id)
        serializer= StudentSerializers(obj, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_502_BAD_GATEWAY)
    
    elif request.method=='PATCH':
        
        id= request.data.get('id')
        obj= StudentModal.objects.get(pk=id)
        serializer= StudentSerializers(obj, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_502_BAD_GATEWAY)
    
    elif request.method=='DELETE':
        id=pk
        obj= StudentModal.objects.get(pk=id)
        obj.delete()
        return Response('DELETE HO GYA Hai Bhai')
