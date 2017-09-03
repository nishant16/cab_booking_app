from rest_framework import serializers

from companies.models import Cab, Driver


class CabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab
        fields = ('name', 'helpline_no')

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('name', 'mobile_no','cab')
