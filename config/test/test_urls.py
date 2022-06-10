from django.test import SimpleTestCase
from django.urls import reverse, resolve
from customer.api.views import CustomerAPIView
from vehicle.api.views import VehicleAPIView
from park_movement.api.views import ParkMovementAPIView, ParkMovementExitAPIView


class TestUrls(SimpleTestCase):

    def test_customer_url_is_resolved(self):
        url = reverse('customer')
        self.assertEqual(resolve(url).func.view_class, CustomerAPIView)

    def test_vehicle_url_is_resolved(self):
        url = reverse('vehicle')
        self.assertEqual(resolve(url).func.view_class, VehicleAPIView)

    def test_movement_url_is_resolved(self):
        url = reverse('movement')
        self.assertEqual(resolve(url).func.view_class, ParkMovementAPIView)

    def test_movement_exit_url_is_resolved(self):
        url = reverse('movement_exit')
        self.assertEqual(resolve(url).func.view_class, ParkMovementExitAPIView)
