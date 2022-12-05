from rest_framework.viewsets import ModelViewSet

from vehicle.models import VehicleModel
from vehicle.serializer import VehicleSerializer


class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = VehicleModel.objects.all()
    http_method_names = ["get", "post", "put"]
