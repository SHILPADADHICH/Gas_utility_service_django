
from django.contrib import admin
from django.urls import path, include
from . import views  



urlpatterns = [
    path('new/', views.ServiceRequestCreateView.as_view(), name='create_service_request'), 
    path('', views.ServiceRequestListView.as_view(), name='list_service_requests'),          
    path('<int:pk>/', views.ServiceRequestDetailView.as_view(), name='service_request_detail'),  
    
]
