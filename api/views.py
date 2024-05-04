from rest_framework.response import Response
from rest_framework.decorators import api_view
from app_vendor.models import *
from .serializers import VendorSerializer

@api_view(['GET','POST'])
def vendors(request):
    if request.method=='GET':
        vendor =  Vendor.objects.all()
        serializer =  VendorSerializer(vendor,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response()
    
@api_view(['GET','PUT','DELETE'])
def view_or_edit_vendor(request,pk):
    if request.method=="GET":
        try:
            vendor = Vendor.objects.get(id=pk)
            serializer = VendorSerializer(vendor,many=False)
            return Response(serializer.data)
        except:
            return Response("Item Doesn't exists")
    elif request.method=="PUT":
        try:
            vendor = Vendor.objects.get(id=pk) 
            serializer = VendorSerializer(instance=vendor,data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except:
            return Response()
    elif request.method=="DELETE":
        try:
            vendor = Vendor.objects.get(id=pk)
            vendor.delete()
            return Response("Vendor deleted successfull")
        except:
            return Response("Vendor deletion failed")
    else:
        return Response()