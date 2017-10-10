from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=200,default='')
    description= models.TextField(max_length=1000, default='')
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name