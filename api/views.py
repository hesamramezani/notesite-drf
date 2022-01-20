from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveAPIView
from .models import contactmodel, User , uploadmodel
from .serializers import contactmodelserializer, userserializer, uploadserializer
from .permission import IsSuperUser, IsOwner  # its personal permission
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser


class create_contact(CreateAPIView):
    queryset = contactmodel.objects.all()
    serializer_class = contactmodelserializer


class list_contact(ListAPIView):
    queryset = contactmodel.objects.all()
    serializer_class = contactmodelserializer
    permission_classes = (IsAdminUser,)


class create_user(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userserializer


class list_user(ListAPIView):
    queryset = User.objects.all()
    serializer_class = userserializer
    permission_classes = (IsSuperUser,)


class userinformation(APIView):
    def get(self, request, pk):
        queryset = User.objects.get(pk=pk)
        serializer = userserializer(queryset)
        return Response(serializer.data, status=200)

    permission_classes = (IsOwner,)


class upload(APIView):
    parser_classes = [JSONParser, FormParser, MultiPartParser]

    def post(self, request):
        serializer = uploadserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    permission_classes = (IsAuthenticated,)

class delete_upload(APIView):
    def delete(self , request , pk):
        queryset = uploadmodel.objects.get(pk = pk)
        queryset.delete()
        return Response(status=204)

class uploadlist(ListAPIView):
    queryset = uploadmodel.objects.all()
    serializer_class = uploadserializer


