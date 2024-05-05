from django.db import models
import uuid


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    vendor_code = models.CharField(max_length=200)
    contact = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    on_time_delivery_rate = models.FloatField(null=True,blank=True)
    quality_rating_avg = models.FloatField(null=True,blank=True)
    fulfillment_rate = models.FloatField(null=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.vendor_code:
            while True:
                unique_id = uuid.uuid4().hex[:8]
                try:
                    Vendor.objects.get(vendor_code=unique_id)
                except Vendor.DoesNotExist:
                    self.vendor_code = unique_id
                    break
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
    
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=200,null=True,blank=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,blank=True,null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(default=0,blank=True,null=True)

    status_coices = (
        ("pending","pending"),
        ("completed","completed"),
        ("cancelled","cancelled")
    )
    status = models.CharField(max_length=50,choices=status_coices,default="pending")

    quality_rating = models.FloatField(null=True,blank=True,default=0)
    issue_date = models.DateTimeField()
    acknowledgement_date = models.DateTimeField(null=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.po_number:
            while True:
                po_num = uuid.uuid4().hex[:8]
                print(f'\n\n\n\n\n\n\n{po_num}')
                try:
                    PurchaseOrder.objects.get(po_number=po_num)
                except PurchaseOrder.DoesNotExist:
                    print(f'\n\n\n\n\n\n\n{po_num}')
                    self.po_number = f"PO-{po_num}"
                    break
        super().save(*args,**kwargs)

    def __str__(self):
        return self.po_number
    
class HistoricalPerformace(models.Model):
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    # def __str__(self):
    #     return self.id