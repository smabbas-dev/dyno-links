from django.db import models

class DynamicLink(models.Model):
    original_url = models.URLField()
    dynamic_path = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
