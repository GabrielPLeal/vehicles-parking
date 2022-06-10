from django.test import TestCase, Client
from django.urls import reverse
from vehicle.models import Vehicle
from customer.models import Customer


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.vehicle_url = reverse('vehicle')
        self.customer = Customer.objects.create(name="Gabriel")

    def test_vehicle_post_if_adds_new_vehicle_should_return_status_code_200(self):
        response = self.client.post(self.vehicle_url, {
            "customer_id": self.customer.id,
            "plate": "1234567890",
            "kind": 2
        })

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'id')

    def test_vehicle_post_if_not_data_in_json_should_return_status_code_400(self):
        response = self.client.post(self.vehicle_url)

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_just_pass_customer_id_should_return_status_code_400(self):
        response = self.client.post(self.vehicle_url, {
            "customer_id": self.customer.id
        })

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_just_pass_plate_should_return_status_code_400(self):
        response = self.client.post(self.vehicle_url, {
            "plate": "1234567890"
        })

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_just_pass_kind_should_return_status_code_400(self):
        response = self.client.post(self.vehicle_url, {
            "kind": 1
        })

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_pass_customer_id_in_blank_should_return_status_code_400(self):
        response = self.client.post(self.vehicle_url, {
            "customer_id": "",
            "plate": "1234567890",
            "kind": 1
        })

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_pass_plate_in_blank_should_return_status_code_400(self):
        response = self.client.post(self.vehicle_url, {
            "customer_id": self.customer.id,
            "plate": "",
            "kind": 1
        })

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_pass_kind_in_blank_should_return_status_code_400(self):
        response = self.client.post(self.vehicle_url, {
            "customer_id": self.customer.id,
            "plate": "1234567890",
            "kind": ""
        })

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_pass_unexpected_key_should_return_status_code_400(self):
        response = self.client.post(self.vehicle_url, {
            "unexpected": ""
        })

        self.assertEquals(response.status_code, 400)

    def test_vehicle_post_if_pass_invalid_kind_should_return_status_code_400(self):
        response = self.client.post(self.vehicle_url, {
            "customer_id": self.customer.id,
            "plate": "1234567890",
            "kind": 0
        })
        self.assertEquals(response.status_code, 400)

    def test_vehicle_put_if_update_customer_id_vehicle_should_return_status_code_200(self):
        vehicle = Vehicle.objects.create(customer_id=self.customer.id, plate="1234567890", kind=1)
        customer_2 = Customer.objects.create(name="Jonas")

        response = self.client.put(self.vehicle_url, {
            "id": vehicle.id,
            "customer_id": customer_2.id,
            "plate": "0123456789",
            "kind": 2
        }, content_type='application/json')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "id")

    def test_vehicle_put_if_update_plate_vehicle_should_return_status_code_200(self):
        vehicle = Vehicle.objects.create(customer_id=self.customer.id, plate="1234567890", kind=1)

        response = self.client.put(self.vehicle_url, {
            "id": vehicle.id,
            "customer_id": self.customer.id,
            "plate": "0123456789",
            "kind": 1
        }, content_type='application/json')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "id")

    def test_vehicle_put_if_update_kind_vehicle_should_return_status_code_200(self):
        vehicle = Vehicle.objects.create(customer_id=self.customer.id, plate="1234567890", kind=1)

        response = self.client.put(self.vehicle_url, {
            "id": vehicle.id,
            "customer_id": self.customer.id,
            "plate": "0123456789",
            "kind": 2
        }, content_type='application/json')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "id")

    def test_vehicle_put_if_pass_all_values_in_blank_should_return_status_code_400(self):
        response = self.client.put(self.vehicle_url, {
            "id": "",
            "customer_id": "",
            "plate": "",
            "kind": ""
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_vehicle_put_if_pass_customer_id_in_blank_should_return_status_code_400(self):
        vehicle = Vehicle.objects.create(customer_id=self.customer.id, plate="1234567890", kind=1)
        response = self.client.put(self.vehicle_url, {
            "id": vehicle.id,
            "customer_id": "",
            "plate": "1234567890",
            "kind": 1
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_vehicle_put_if_pass_plate_in_blank_should_return_status_code_400(self):
        vehicle = Vehicle.objects.create(customer_id=self.customer.id, plate="1234567890", kind=1)
        response = self.client.put(self.vehicle_url, {
            "id": vehicle.id,
            "customer_id": self.customer.id,
            "plate": "",
            "kind": 1
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_vehicle_put_if_pass_kind_in_blank_should_return_status_code_400(self):
        vehicle = Vehicle.objects.create(customer_id=self.customer.id, plate="1234567890", kind=1)
        response = self.client.put(self.vehicle_url, {
            "id": vehicle.id,
            "customer_id": self.customer.id,
            "plate": "1234567890",
            "kind": ""
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_vehicle_put_if_pass_invalid_kind_should_return_status_code_400(self):
        vehicle = Vehicle.objects.create(customer_id=self.customer.id, plate="1234567890", kind=1)
        response = self.client.put(self.vehicle_url, {
            "id": vehicle.id,
            "customer_id": self.customer.id,
            "plate": "1234567890",
            "kind": 0
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_vehicle_put_if_pass_invalid_id_should_return_status_code_400(self):
        response = self.client.put(self.vehicle_url, {
            "id": "00",
            "customer_id": self.customer.id,
            "plate": "1234567890",
            "kind": 1
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)
