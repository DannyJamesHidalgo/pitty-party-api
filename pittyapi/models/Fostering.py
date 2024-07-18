from django.db import models
from django.contrib.auth.models import User


class Fostering(models.Model):
    dog = models.ForeignKey("Dog", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Using Django's User model
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Fostering of {self.dog.name} by {self.user.username}"
