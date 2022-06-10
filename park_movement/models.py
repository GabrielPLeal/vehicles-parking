from django.db import models
from uuid import uuid4

from vehicle.models import Vehicle


class ParkMovement(models.Model):

    class Meta:
        db_table = 'TB_PARKMOVEMENT'

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    entry_date = models.DateField(auto_now=True, editable=False)
    exit_date = models.DateField(null=True)
    validate_date = models.DateField(null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    plate = models.CharField(max_length=50)
