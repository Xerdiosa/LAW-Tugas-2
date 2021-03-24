from django.db import models
from django.utils.timezone import now

class Metadata(models.Model):
    title = models.CharField(max_length=30, unique=True)
    author = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now)