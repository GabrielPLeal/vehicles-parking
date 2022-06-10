from django.test import TestCase, Client
from django.urls import reverse
from customer.models import Customer


class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.customer_url = reverse('customer')

    def test_customer_post_if_adds_new_customer_should_return_status_code_200(self):
        response = self.client.post(self.customer_url, {
            "name": "Gabriel"
        })

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'id')

    def test_customer_post_if_not_data_in_json_should_return_status_code_400(self):
        response = self.client.post(self.customer_url)

        self.assertEquals(response.status_code, 400)

    def test_customer_post_if_name_in_blank_should_return_status_code_400(self):
        response = self.client.post(self.customer_url, {
            "name": ""
        })

        self.assertEquals(response.status_code, 400)

    def test_customer_post_if_pass_unexpected_key_should_return_status_code_400(self):
        response = self.client.post(self.customer_url, {
            "unexpected": ""
        })

        self.assertEquals(response.status_code, 400)

    def test_customer_post_if_pass_id_key_should_ignore_value_id_return_status_code_200(self):
        response = self.client.post(self.customer_url, {
            "id": "1234567",
            "name": "Gabriel"
        })

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'id')

    def test_customer_put_if_update_customer_should_return_status_code_200(self):
        customer = Customer.objects.create(name='Jonas')

        response = self.client.put(self.customer_url, {
            "id": customer.id, "name": "Jonas Santos"
        }, content_type='application/json')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "id")

    def test_customer_put_if_not_data_in_json_should_return_status_code_400(self):
        response = self.client.put(self.customer_url, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_customer_put_if_no_pass_name_should_return_status_code_400(self):
        customer = Customer.objects.create(name='Jonas')

        response = self.client.put(self.customer_url, {
            "id": f"{customer.id}"
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_customer_put_if_not_pass_id_should_return_status_code_400(self):
        response = self.client.put(self.customer_url, {
            "name": "Gabriel"
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_customer_put_if_name_in_blank_should_return_status_code_400(self):
        customer = Customer.objects.create(name='Jonas')

        response = self.client.put(self.customer_url, {
            "id": f"{customer.id}",
            "name": ""
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_customer_put_if_id_in_blank_should_return_status_code_400(self):
        response = self.client.put(self.customer_url, {
            "id": "",
            "name": "Gabriel"
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_customer_put_if_id_not_valid_uuid_should_return_status_code_400(self):
        response = self.client.put(self.customer_url, {
            "id": "Invalid uuid",
            "name": "Gabriel"
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_customer_put_if_pass_unexpected_key_should_return_status_code_400(self):
        response = self.client.put(self.customer_url, {
            "unxpected": ""
        }, content_type='application/json')

        self.assertEquals(response.status_code, 400)
