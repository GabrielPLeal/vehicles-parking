from rest_framework.viewsets import ModelViewSet

from park_movement.models import ParkMovementModel
from park_movement.serializer import (
    ParkMovementSerializer,
    ParkMovementExitSerializer
)


class ParkMovementViewSet(ModelViewSet):
    serializer_class = ParkMovementSerializer
    queryset = ParkMovementModel.objects.all()
    http_method_names = ["get", "post", "put"]


class ParkMovementExitViewSet(ModelViewSet):
    serializer_class = ParkMovementExitSerializer
    queryset = ParkMovementModel.objects.all()
    http_method_names = ["put"]
