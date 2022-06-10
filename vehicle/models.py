from django.db import models
from uuid import uuid4

from customer.models import Customer


class Vehicle(models.Model):

    class Meta:
        db_table = 'TB_CUSTOMER_VEHICLES'

    class Kind(models.IntegerChoices):
        moto = 1
        carro = 2

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plate = models.CharField(max_length=10)
    kind = models.IntegerField(choices=Kind.choices)
