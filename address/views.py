from django.shortcuts import render
from address.models import Address
from address.serializers import AddressSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
class AddressOpearations(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(active='Y'))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        #self.perform_destroy(instance)
        instance.active='N'
        instance.save()
        return Response(status=HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.active=='Y':
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response(status=HTTP_204_NO_CONTENT)