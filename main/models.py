from django.db import models
from django.utils.timezone import now

class Quote(models.Model):
    text = models.TextField(blank=False, null=False)
    author_name = models.CharField(max_length=255, default='Unknown')
    is_draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)


    def __str__(self):
        return self.text