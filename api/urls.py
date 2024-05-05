from django.urls import path
from . import views

urlpatterns = [
    path('vendors/',views.vendors,name="vendors"),
    path('vendors/<str:pk>/',views.view_or_edit_vendor,name="view_or_edit_vendor"),
    path('purchase_orders/',views.purchase_order,name="purchase_order"),
    path('purchase_orders/<str:pk>/',views.view_or_edit_purchase_order,name="view_or_edit_purchase_order"),
    path('vendors/<str:pk>/performance/',views.vendor_performance,name="vendor_performance"),
    path('purchase_orders/<str:pk>/acknowledge/',views.po_acknowledgement,name="po_acknowledgement"),
]