import json
from django.db import models
import uuid

from enums.enums import StatusOrder

# Create your models here.
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255,null=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.CharField(max_length=255,null=True)
    name_customer = models.CharField(max_length=255,null=False)
    id_customer = models.IntegerField(null=False)
    email = models.EmailField(null=True)
    payment_method = models.CharField(max_length=255,null=False)
    phone_number = models.CharField(max_length=20,null=False)
    check_in_datetime = models.DateTimeField(null=True, blank=True)
    check_out_datetime = models.DateTimeField(null=True, blank=True)
    service_use = models.JSONField()
    status = models.CharField(max_length=255, blank=True,default=StatusOrder.PENDING.value)

    def __str__(self):
        return self.id
    