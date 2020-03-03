from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.

class Document(models.Model):
    SOURCE_CHOICES = []

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="exports")
    created_time = models.DateTimeField(auto_created=True)
    type = models.CharField(max_length=100)
    source_type = models.CharField(SOURCE_CHOICES, blank=True, null=True, max_length=20)

    source_id = models.CharField(blank=True, null=True, max_length=50)
    input_meta_data = JSONField(default=dict, null=True, blank=True)
