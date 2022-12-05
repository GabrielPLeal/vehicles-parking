from rest_framework import serializers

from park_movement.models import ParkMovementModel
from vehicle.models import VehicleModel


class ParkMovementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParkMovementModel
        fields = "__all__"

class ParkMovementExitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParkMovementModel
        fields = ("id", "exit_date")
