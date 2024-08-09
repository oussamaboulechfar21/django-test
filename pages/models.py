# myapp/models.py

from django.db import models

class UserInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
