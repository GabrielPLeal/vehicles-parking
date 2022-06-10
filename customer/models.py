from django.db import models
from uuid import uuid4


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'TB_CUSTOMER'
