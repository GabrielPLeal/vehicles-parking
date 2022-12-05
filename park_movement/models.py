from django.db import models
from uuid import uuid4

from vehicle.models import VehicleModel


class ParkMovementModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    entry_date = models.DateField(auto_now=True, editable=False)
    exit_date = models.DateField(null=True)
    validate_date = models.DateField(null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    vehicle = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, null=False)
    plate = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = 'TB_PARKMOVEMENT'
