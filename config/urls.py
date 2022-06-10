from django.urls import path

from customer.api.views import CustomerAPIView
from vehicle.api.views import VehicleAPIView
from park_movement.api.views import ParkMovementAPIView, ParkMovementExitAPIView


urlpatterns = [
    path('api/v1/customer/', CustomerAPIView.as_view(), name='customer'),
    path('api/v1/vehicle/', VehicleAPIView.as_view(), name='vehicle'),
    path('api/v1/movement/', ParkMovementAPIView.as_view(), name='movement'),
    path('api/v1/movement_exit/', ParkMovementExitAPIView.as_view(), name='movement_exit')
    ]
