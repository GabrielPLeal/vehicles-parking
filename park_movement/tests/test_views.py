from django.test import TestCase, Client
from django.urls import reverse
from customer.models import CustomerModel
from vehicle.models import VehicleModel
from park_movement.models import ParkMovementModel


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.movement_url = reverse('movement-list')
        self.movement_exit_url = reverse('movement-exit-list')
        self.customer = CustomerModel.objects.create(name='Gabriel')
        self.vehicle = VehicleModel.objects.create(customer_id=self.customer.id, plate="1234567890", kind=1)
        self.park_movement = ParkMovementModel.objects.create(plate="1234567890", vehicle_id=self.vehicle.id)
        self.put_movement_url = f'{self.movement_url}{self.park_movement.id}/'
        self.put_movement_exit_url = f'{self.movement_exit_url}{self.park_movement.id}/'

    def test_movement_post_if_adds_new_park_movement_should_return_status_code_201(self):
        response = self.client.post(self.movement_url, {
            "plate": "1234567890",
            "vehicle": self.vehicle.id
        })
        
        self.assertContains(response, 'id', status_code=201)

    def test_movement_post_if_pass_plate_in_blank_should_return_status_code_400(self):
        response = self.client.post(self.movement_url, {
            "plate": "",
            "vehicle": self.vehicle.id
        })
        
        self.assertContains(response, 'This field may not be blank', status_code=400)

    def test_movement_post_if_pass_vehicle_id_in_blank_should_return_status_code_400(self):
        response = self.client.post(self.movement_url, {
            "plate": "1234567890",
            "vehicle": ""
        })
        
        self.assertContains(response, 'This field may not be null', status_code=400)

    def test_movement_post_if_pass_invalid_uuid_should_return_status_code_400(self):
        response = self.client.post(self.movement_url, {
            "plate": "1234567890",
            "vehicle": "00"
        })
        
        self.assertContains(response, '“00” is not a valid UUID.', status_code=400)
    
    def test_movement_post_if_pass_unexist_vehicle_id_should_return_status_code_400(self):
        response = self.client.post(self.movement_url, {
            "plate": "1234567890",
            "vehicle": "d1ca9c7c-8f11-481b-aa7a-92f24d9d25d7"
        })
        
        self.assertContains(response, 'Invalid pk', status_code=400)

    def test_movement_post_if_not_data_in_json_should_return_status_code_400(self):
        response = self.client.post(self.movement_url)

        self.assertEquals(response.status_code, 400)

    def test_movement_post_if_pass_unexpected_key_should_return_status_code_400(self):
        response = self.client.post(self.movement_url, {
            "unexpected": ""
        })

        self.assertEquals(response.status_code, 400)

    def test_movement_put_if_update_fields_from_park_movement_should_return_status_code_200(self):
        data = {
            "vehicle": self.vehicle.id,
            "plate": "123456789",
            "value": 10.00
        }
        
        response = self.client.put(self.put_movement_url, data, content_type='application/json')

        self.assertContains(response, 'id', status_code=200)

    def test_movement_put_if_not_pass_id_in_url_request_should_return_status_code_405(self):
        response = self.client.put(self.movement_url, content_type='application/json')

        self.assertEquals(response.status_code, 405)

    def test_movement_put_if_pass_invalid_id_in_url_request_should_return_status_code_404(self):
        response = self.client.put(f"{self.movement_url}00/", content_type='application/json')

        self.assertEquals(response.status_code, 404)

    def test_movement_put_if_pass_validate_date_in_blank_should_return_status_code_400(self):
        data = {
            "vehicle": self.vehicle.id,
            "plate": "123456789",
            "validate_date": "",
        }
    
        response = self.client.put(self.put_movement_url, data, content_type='application/json')
        
        self.assertContains(response, 'Date has wrong format', status_code=400)

    def test_movement_exit_put_if_update_exit_date_should_return_status_code_200(self):
        data = {"exit_date": "2022-06-15"}
        response = self.client.put(self.put_movement_exit_url, data, content_type='application/json')

        self.assertContains(response, 'exit_date', status_code=200)

    def test_movement_exit_put_if_not_data_in_json_should_return_status_code_200(self):
        response = self.client.put(self.put_movement_exit_url, content_type='application/json')

        self.assertEquals(response.status_code, 200)

    def test_movement_exit_put_if_pass_invalid_id_should_return_status_code_404(self):
        data = {"exit_date": "2022-06-15"}
        response = self.client.put(f"{self.movement_exit_url}00/", data, content_type='application/json')

        self.assertEquals(response.status_code, 404)
