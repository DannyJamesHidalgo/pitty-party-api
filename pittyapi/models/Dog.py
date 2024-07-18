from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    weight = models.FloatField()
    health_status = models.CharField(max_length=100)
    story = models.TextField()
    adoption_status = models.CharField(max_length=20)
    arrival_date = models.DateField()

    def __str__(self):
        return self.name
