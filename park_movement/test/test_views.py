from django.test import TestCase, Client
from django.urls import reverse
from customer.models import Customer
from vehicle.models import Vehicle
from park_movement.models import ParkMovement


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.movement_url = reverse('movement')
        self.movement_exit_url = reverse('movement_exit')
        self.customer = Customer.objects.create(name='Gabriel')
        self.vehicle = Vehicle.objects.create(customer_id=self.customer.id, plate="1234567890", kind=1)

    def test_movement_post_if_adds_new_park_movement_should_return_status_code_200(self):
        response = self.client.post(self.movement_url, {
            "plate": "1234567890",
            "vehicle_id": self.vehicle.id
        })

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'id')

    def test_movement_post_if_pass_plate_in_blank_should_return_status_code_200(self):
        response = self.client.post(self.movement_url, {
            "plate": "",
            "vehicle_id": self.vehicle.id
        })

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'id')

    def test_movement_post_if_pass_vehicle_id_in_blank_should_return_status_code_200(self):
        response = self.client.post(self.movement_url, {
            "plate": "1234567890",
            "vehicle_id": ""
        })

        self.assertEquals(response.status_code, 400)

    def test_movement_post_if_pass_invalid_vehicle_id_in_blank_should_return_status_code_200(self):
        response = self.client.post(self.movement_url, {
            "plate": "1234567890",
            "vehicle_id": "00"
        })

        self.assertEquals(response.status_code, 400)

    def test_movement_post_if_not_data_in_json_should_return_status_code_400(self):
        response = self.client.post(self.movement_url)

        self.assertEquals(response.status_code, 400)

    def test_movement_post_if_pass_unexpected_key_should_return_status_code_400(self):
        response = self.client.post(self.movement_url, {
            "unexpected": ""
        })

        self.assertEquals(response.status_code, 400)

    def test_movement_put_if_update_other_fields_from_park_movement_should_return_status_code_200(self):
        park_movement = ParkMovement.objects.create(plate="1234567890", vehicle_id=self.vehicle.id)

        response = self.client.put(self.movement_url, {
            "id": park_movement.id,
            "validate_date": "2022-06-15",
            "value": 10.00
        }, content_type='application/json')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'id')

    def test_movement_put_if_pass_id_in_blank_should_return_status_code_400(self):
        response = self.client.put(self.movement_url, {
            "id": "",
            "validate_date": "2022-06-15",
            "value": 10.00
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_movement_put_if_pass_invalid_id_should_return_status_code_400(self):
        response = self.client.put(self.movement_url, {
            "id": "00",
            "validate_date": "2022-06-15",
            "value": 10.00
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_movement_put_if_pass_validate_date_in_blank_should_return_status_code_400(self):
        park_movement = ParkMovement.objects.create(plate="1234567890", vehicle_id=self.vehicle.id)

        response = self.client.put(self.movement_url, {
            "id": park_movement.id,
            "validate_date": "",
            "value": 10.00
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_movement_put_if_pass_value_in_blank_should_return_status_code_400(self):
        park_movement = ParkMovement.objects.create(plate="1234567890", vehicle_id=self.vehicle.id)

        response = self.client.put(self.movement_url, {
            "id": park_movement.id,
            "validate_date": "",
            "value": ""
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_movement_put_if_pass_unxpected_key_should_return_status_code_400(self):
        response = self.client.put(self.movement_url, {
            "unxpected": ""
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_movement_exit_put_if_update_exit_date_should_return_status_code_200(self):
        park_movement = ParkMovement.objects.create(
            plate="1234567890", vehicle_id=self.vehicle.id, validate_date="2022-06-15", value=10.00)

        response = self.client.put(self.movement_exit_url, {
            "id": park_movement.id,
            "exit_date": "2022-06-15"
        }, content_type='application/json')

        self.assertEquals(response.status_code, 200)

    def test_movement_exit_put_if_not_data_in_json_should_return_status_code_200(self):
        response = self.client.put(self.movement_exit_url, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_movement_exit_put_if_pass_invalid_id_should_return_status_code_200(self):
        response = self.client.put(self.movement_exit_url, {
            "id": "00",
            "exit_date": "2022-06-15"
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)
