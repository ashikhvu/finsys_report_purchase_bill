from rest_framework.response import Response
from rest_framework.decorators import api_view
from app_vendor.models import *
from .serializers import VendorSerializer,PurchaseOrderSerializer,HistoricalPerformanceSerializer
from django.db.models import F,ExpressionWrapper,DurationField,Case,When,Value
from datetime import timedelta


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
    
@api_view(['GET','POST'])
def purchase_order(request):
    if request.method=="GET":
        po = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(po,many=True)
        return Response(serializer.data)    
    elif request.method=="POST":
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        return Response()
    
@api_view(['GET','PUT','DELETE'])
def view_or_edit_purchase_order(request,pk):
    if request.method=="GET":
        po = PurchaseOrder.objects.get(id=pk)
        serializer  = PurchaseOrderSerializer(po,many=False)
        return Response(serializer.data)
    elif request.method=="PUT":
        po = PurchaseOrder.objects.get(id=pk)
        serializer = PurchaseOrderSerializer(instance=po,data=request.data)

        if serializer.is_valid():
            serializer.save()

            vendor_details = po.vendor
            po_completed_on_time=PurchaseOrder.objects.filter(vendor=vendor_details,status='completed',issue_date__lte=F('delivery_date'))
            po_completd_all = PurchaseOrder.objects.filter(vendor=vendor_details,status='completed')

            po_total = PurchaseOrder.objects.filter(vendor=vendor_details)
            # calculate on_time_delivery_rate and quality_rating_avg if status is completed
            if request.data['status']=="completed":
                delivery_rate = (int(po_completed_on_time.count())/int(po_completd_all.count()))*100
                quality_rating_total = 0
                for i in po_completd_all:
                    if not i.quality_rating == 0 and not i.quality_rating == None:
                        quality_rating_total += int(i.quality_rating)
                if not po_completd_all.count()==0:
                    quality_rating_avarage = quality_rating_total/po_completd_all.count()
                else:
                    quality_rating_avarage=0

                if HistoricalPerformace.objects.all().exists():
                    hp = HistoricalPerformace.objects.get(vendor=vendor_details)
                    hp.on_time_delivery_rate = delivery_rate
                    hp.quality_rating_avg =quality_rating_avarage
                    hp.save()
                else:
                    HistoricalPerformace.objects.create(vendor=vendor_details,on_time_delivery_rate=delivery_rate,quality_rating_avg=quality_rating_avarage)
            # calculate full_fillment if status changes
            if request.data['status'] != serializer.instance.status:
                if po_total.count() !=0:
                    full_fillment = float(po_completed_on_time.count())/float(po_total.count())
                else:
                    full_fillment=0
                if HistoricalPerformace.objects.all().exists():
                    hp = HistoricalPerformace.objects.get(vendor=vendor_details)
                    hp.fulfillment_rate=full_fillment
                    hp.save()
                else:
                    HistoricalPerformace.objects.create(vendor=vendor_details,fulfillment_rate=full_fillment)

        return Response(serializer.data)
    elif request.method == "DELETE":
        try:
            po = PurchaseOrder.objects.get(id=pk)
            po.delete()
            return Response("Deleted Purchase order successfully")
        except:
            return Response("Deletion of Purchase order falied")
    else:
        return Response() 

@api_view(['GET'])
def vendor_performance(request,pk):
    hp = HistoricalPerformace.objects.get(vendor=Vendor.objects.get(id=pk))
    serializer = HistoricalPerformanceSerializer(hp,many=False)
    return Response(serializer.data)    

@api_view(['POST'])
def po_acknowledgement(request,pk):
    po = PurchaseOrder.objects.get(id=pk)
    serializer = PurchaseOrderSerializer(instance=po,data=request.data)

    vendor_details = po.vendor
    po_completed_on_time=PurchaseOrder.objects.filter(vendor=vendor_details,status='completed',issue_date__lte=F('delivery_date'))
    po_completd_all = PurchaseOrder.objects.filter(vendor=vendor_details,status='completed')
    po_total = PurchaseOrder.objects.filter(vendor=vendor_details)

    if serializer.is_valid():
        if 'acknowledgement_date' in request.data:
            serializer.save()
            
            response_times = []
            for i in po_total:
                if i.issue_date!=None and i.acknowledgement_date!=None:
                    response_time = i.issue_date - i.acknowledgement_date
                    response_times.append(response_time.total_seconds())
            if response_times:
                avg_response_time = sum(response_times)/po_total.count()
            else:
                avg_response_time = 0
        
            hp=HistoricalPerformace.objects.get(vendor=vendor_details)
            hp.average_response_time = avg_response_time    
            hp.save()

            return Response("acknowledged")
        else:
            return Response('Please provide acknowledgement date')
    else:
        return Response("Provide all the datas along with the acknowledgement date")