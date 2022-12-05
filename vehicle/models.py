from django.db import models
from uuid import uuid4

from customer.models import CustomerModel


class VehicleModel(models.Model):

    class Kind(models.IntegerChoices):
        moto = 1
        carro = 2

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, null=False)
    plate = models.CharField(max_length=10, blank=False)
    kind = models.IntegerField(choices=Kind.choices, null=False)

    class Meta:
        db_table = 'TB_CUSTOMER_VEHICLES'