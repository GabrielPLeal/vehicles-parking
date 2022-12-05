from django.test import TestCase, Client
from django.urls import reverse
from vehicle.models import VehicleModel
from customer.models import CustomerModel


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.vehicle_url = reverse('vehicle-list')
        self.customer = CustomerModel.objects.create(name="Gabriel")
        self.vehicle = VehicleModel.objects.create(customer_id=self.customer.id, plate="1234567890", kind=1)
        self.put_vehicle_url = f"{self.vehicle_url}{self.vehicle.id}/"
        

    def test_vehicle_post_if_adds_new_vehicle_should_return_status_code_200(self):
        data = {
            "customer": self.customer.id,
            "plate": "1234567890",
            "kind": 2
        }
        
        response = self.client.post(self.vehicle_url, data)
        
        self.assertContains(response, 'id', status_code=201)

    def test_vehicle_post_if_not_data_should_return_status_code_400(self):
        response = self.client.post(self.vehicle_url)
        
        print(response.data)

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_just_pass_customer_id_should_return_status_code_400(self):
        data = {"customer_id": self.customer.id}

        response = self.client.post(self.vehicle_url, data)

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_just_pass_plate_should_return_status_code_400(self):
        data = {"plate": "1234567890"}

        response = self.client.post(self.vehicle_url, data)

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_just_pass_kind_should_return_status_code_400(self):
        data = {"kind": 1}
        
        response = self.client.post(self.vehicle_url, data)

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_pass_customer_id_in_blank_should_return_status_code_400(self):
        data = {
            "customer_id": "",
            "plate": "1234567890",
            "kind": 1
        }
        
        response = self.client.post(self.vehicle_url, data)

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_pass_plate_in_blank_should_return_status_code_400(self):
        data = {
            "customer_id": self.customer.id,
            "plate": "",
            "kind": 1
        }
        
        response = self.client.post(self.vehicle_url, data)

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_pass_kind_in_blank_should_return_status_code_400(self):
        data = {
            "customer_id": self.customer.id,
            "plate": "1234567890",
            "kind": ""
        }
        
        response = self.client.post(self.vehicle_url, data)

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_pass_unexpected_key_should_return_status_code_400(self):
        data = {"unexpected": ""}        

        response = self.client.post(self.vehicle_url, data)

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_pass_invalid_kind_should_return_status_code_400(self):
        data = {
            "customer_id": self.customer.id,
            "plate": "1234567890",
            "kind": 0
        }
        
        response = self.client.post(self.vehicle_url, data)
        
        self.assertEquals(response.status_code, 400)

    def test_vehicle_put_if_update_customer_id_vehicle_should_return_status_code_200(self):
        customer_2 = CustomerModel.objects.create(name="Jonas")
        
        data = {
            "id": self.vehicle.id,
            "customer": customer_2.id,
            "plate": "0123456789",
            "kind": 2
        }

        response = self.client.put(self.put_vehicle_url, data, content_type='application/json')
        
        self.assertContains(response, "id", status_code=200)

    def test_vehicle_put_if_update_plate_vehicle_should_return_status_code_200(self):
        data = {
            "id": self.vehicle.id,
            "customer": self.customer.id,
            "plate": "0123456789",
            "kind": 1
        }

        response = self.client.put(self.put_vehicle_url, data, content_type='application/json')

        self.assertContains(response, "id", status_code=200)

    def test_vehicle_put_if_update_kind_vehicle_should_return_status_code_200(self):
        data = {
            "customer": self.customer.id,
            "plate": "0123456789",
            "kind": 2
        }
        
        response = self.client.put(self.put_vehicle_url, data, content_type='application/json')
        
        self.assertContains(response, "id", status_code=200)

    def test_vehicle_put_if_not_pass_id_in_url_request_should_return_status_code_405(self):
        response = self.client.put(self.vehicle_url, content_type='application/json')

        self.assertEquals(response.status_code, 405)

    def test_vehicle_put_if_pass_customer_id_in_blank_should_return_status_code_400(self):
        data = {
            "customer": "",
            "plate": "1234567890",
            "kind": 1
        }
        
        response = self.client.put(self.put_vehicle_url, data, content_type='application/json')

        self.assertContains(response, "This field may not be null", status_code=400)

    def test_vehicle_put_if_pass_plate_in_blank_should_return_status_code_400(self):
        data = {
            "id": self.vehicle.id,
            "customer": self.customer.id,
            "plate": "",
            "kind": 1
        }
        
        response = self.client.put(self.put_vehicle_url, data, content_type='application/json')
        
        self.assertContains(response, "This field may not be blank", status_code=400)

    def test_vehicle_put_if_pass_invalid_kind_choice_should_return_status_code_400(self):
        data = {
            "id": self.vehicle.id,
            "customer": self.customer.id,
            "plate": "1234567890",
            "kind": ""
        }
        
        response = self.client.put(self.put_vehicle_url, data, content_type='application/json')
        
        self.assertContains(response, "is not a valid choice", status_code=400)

    def test_vehicle_put_if_pass_invalid_id_should_return_status_code_404(self):
        response = self.client.put(f"{self.vehicle_url}00/", content_type='application/json')

        self.assertEquals(response.status_code, 404)
