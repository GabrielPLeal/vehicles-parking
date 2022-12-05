from django.test import SimpleTestCase
from django.urls import reverse, resolve

from customer.view import CostumerViewSet
from vehicle.view import VehicleViewSet
from park_movement.view import ParkMovementViewSet, ParkMovementExitViewSet


class TestUrls(SimpleTestCase):

    def test_customer_url_is_resolved(self):
        url = reverse("customer-list")
        self.assertEqual(resolve(url).func.__name__, CostumerViewSet.__name__)

    def test_vehicle_url_is_resolved(self):
        url = reverse("vehicle-list")
        self.assertEqual(resolve(url).func.__name__, VehicleViewSet.__name__)

    def test_movement_url_is_resolved(self):
        url = reverse("movement-list")
        self.assertEqual(resolve(url).func.__name__, ParkMovementViewSet.__name__)

    def test_movement_exit_url_is_resolved(self):
        url = reverse("movement-exit-list")
        self.assertEqual(resolve(url).func.__name__, ParkMovementExitViewSet.__name__)
