from django.test import TestCase, Client
from django.urls import reverse, resolve

from customer.models import CustomerModel
from customer.view import CostumerViewSet



class TestViews(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.customer = CustomerModel.objects.create(name='Jonas')
        self.customer_url = reverse("customer-list")
        self.put_customer_url = f'{self.customer_url}{self.customer.id}/'

    def test_customer_post_if_adds_new_customer_should_return_status_code_201(self):
        response = self.client.post(self.customer_url, {
            "name": "Gabriel"
        })

        self.assertContains(response, "id", status_code=201)

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

        self.assertContains(response, 'id', status_code=201)

    def test_customer_put_if_update_customer_should_return_status_code_200(self):
        data =  {"name": "Jonas Santos"}

        response = self.client.put(self.put_customer_url, data, content_type='application/json')
        
        self.assertContains(response, "id", status_code=200)
    
    def test_customer_put_if_not_pass_id_in_url_request_should_return_status_code_405(self):
        response = self.client.put(self.customer_url, content_type='application/json')

        self.assertEquals(response.status_code, 405)
    
    def test_customer_put_if_pass_invalid_id_in_url_request_should_return_status_code_404(self):
        response = self.client.put(f"{self.customer_url}00/", content_type='application/json')

        self.assertEquals(response.status_code, 404)

    def test_customer_put_if_not_data_in_json_should_return_status_code_400(self):
        response = self.client.put(self.put_customer_url, content_type='application/json')

        self.assertEquals(response.status_code, 400)

    def test_customer_put_if_name_in_blank_should_return_status_code_400(self):
        data = {"name": ""}

        response = self.client.put(self.put_customer_url, data, content_type='application/json')

        self.assertEquals(response.status_code, 400)
    
    def test_customer_put_if_pass_unexpected_key_should_return_status_code_400(self):
        data = {"unxpected": ""}
        
        response = self.client.put(self.put_customer_url,data , content_type='application/json')

        self.assertEquals(response.status_code, 400)
