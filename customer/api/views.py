from rest_framework.views import APIView
from rest_framework.response import Response

from customer.models import Customer
from customer.api.serializer import CustomerSerializer


class CustomerAPIView(APIView):

    def post(self, request):
        customer_data = request.data
        serializer = CustomerSerializer(data=customer_data)
        if serializer.is_valid(raise_exception=True):
            new_customer = Customer.objects.create(name=customer_data['name'])
            new_customer.save()
            serializer = CustomerSerializer(new_customer)
            return Response({"id": serializer.data.get('id')})

    def put(self, request):
        customer_data = request.data
        serializer = CustomerSerializer(data=customer_data, context=request)
        if serializer.is_valid(raise_exception=True):
            customer = Customer.objects.get(id=customer_data['id'])
            customer.name = customer_data['name']
            customer.save()
            serializer = CustomerSerializer(customer)
            return Response({"id": serializer.data.get('id')})
