from django.db import models

class Quote(models.Model):
    text = models.TextField(blank=False, null=False)
    author_name = models.CharField(max_length=255, default='Unknown')
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return self.text