from rest_framework import serializers
from app_vendor.models import Vendor,PurchaseOrder,HistoricalPerformace

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields = '__all__'

    # def __str__(self):
    #     return self.name
    
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields='__all__'

    # def __str__(self):
    #     return self.name
        
class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=HistoricalPerformace
        fields='__all__'

    # def __str__(self):
    #     return self.name