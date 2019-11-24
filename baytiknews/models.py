from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    def __str__(self):
        return self.title