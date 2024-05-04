from django.urls import path
from . import views

urlpatterns = [
    path('vendors/',views.vendors,name="vendors"),
    path('vendors/<str:pk>/',views.view_or_edit_vendor,name="view_or_edit_vendor"),
]