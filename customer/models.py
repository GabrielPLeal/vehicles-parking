from django.db import models
from uuid import uuid4


class CustomerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'TB_CUSTOMER'
