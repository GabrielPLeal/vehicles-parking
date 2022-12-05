from rest_framework.viewsets import ModelViewSet

from customer.models import CustomerModel
from customer.serializer import CustomerSerializer


class CostumerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = CustomerModel.objects.all()
    http_method_names = ["get", "post", "put"]
