from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Vendor, PurchaseOrder, HistoricalPerformace
from api.serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_vendors_get(self):
        response = self.client.get(reverse('vendors'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vendors_post(self):
        data = {'name': 'Test Vendor'}
        response = self.client.post(reverse('vendors'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_view_or_edit_vendor_get(self):
    #     vendor = Vendor.objects.create(name='Test Vendor')
    #     response = self.client.get(reverse('view_or_edit_vendor', kwargs={'pk': vendor.pk}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_view_or_edit_vendor_put(self):
    #     vendor = Vendor.objects.create(name='Test Vendor')
    #     data = {'name': 'Updated Vendor'}
    #     response = self.client.put(reverse('view_or_edit_vendor', kwargs={'pk': vendor.pk}), data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_view_or_edit_vendor_delete(self):
    #     vendor = Vendor.objects.create(name='Test Vendor')
    #     response = self.client.delete(reverse('view_or_edit_vendor', kwargs={'pk': vendor.pk}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_purchase_order_get(self):
    #     response = self.client.get(reverse('purchase_orders'))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_purchase_order_post(self):
    #     data = {'field1': 'value1', 'field2': 'value2'}  # Provide sample data as required
    #     response = self.client.post(reverse('purchase_orders'), data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_view_or_edit_purchase_order_get(self):
    #     po = PurchaseOrder.objects.create()  # Provide necessary fields for PurchaseOrder creation
    #     response = self.client.get(reverse('view_or_edit_purchase_order', kwargs={'pk': po.pk}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_view_or_edit_purchase_order_put(self):
    #     po = PurchaseOrder.objects.create()  # Provide necessary fields for PurchaseOrder creation
    #     data = {'field1': 'updated_value1', 'field2': 'updated_value2'}  # Provide updated data
    #     response = self.client.put(reverse('view_or_edit_purchase_order', kwargs={'pk': po.pk}), data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_view_or_edit_purchase_order_delete(self):
    #     po = PurchaseOrder.objects.create()  # Provide necessary fields for PurchaseOrder creation
    #     response = self.client.delete(reverse('view_or_edit_purchase_order', kwargs={'pk': po.pk}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_vendor_performance(self):
    #     vendor = Vendor.objects.create()  # Provide necessary fields for Vendor creation
    #     response = self.client.get(reverse('vendor_performance', kwargs={'pk': vendor.pk}))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_po_acknowledgement_post(self):
    #     po = PurchaseOrder.objects.create()  # Provide necessary fields for PurchaseOrder creation
    #     data = {'acknowledgement_date': '2024-05-06'}  # Provide acknowledgement data
    #     response = self.client.post(reverse('po_acknowledgement', kwargs={'pk': po.pk}), data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
