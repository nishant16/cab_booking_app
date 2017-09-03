from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from companies.models import Cab, Driver
from .serializers import CabSerializer, DriverSerializer
from django.shortcuts import get_object_or_404


# list of all cabs
class CabList(APIView):
    def get(self, request):
        cab = Cab.objects.all()
        serializer = CabSerializer(cab, many=True)
        return Response(serializer.data)

class DriverList(APIView):
    def get(self, request):
        driver = Driver.objects.all()
        serializer = DriverSerializer(driver,many =True)
        return Response(serializer.data)
