import json
from django.db import models

# Create your models here.

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_url = models.JSONField(max_length=200, blank=True,default='[]')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.TextField(max_length=200, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.TextField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    time_service = models.IntegerField()
    status = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.name
    
    def set_image_url(self, urls):
        self.image_url = json.dumps(urls)

    def get_image_url(self):
        try:
            return json.loads(self.image_url)
        except json.JSONDecodeError:
            return []
    
    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price
