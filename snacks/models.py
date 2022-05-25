from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, help_text='Enter a brief description.')

    def __str__(self):
        return self.name