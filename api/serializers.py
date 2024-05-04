from rest_framework import serializers
from app_vendor.models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields = '__all__'

    def __str__(self):
        return self.name