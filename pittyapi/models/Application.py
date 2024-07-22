from django.db import models
from .Adopter import Adopter


class Application(models.Model):
    dog_id = models.ForeignKey("Dog", on_delete=models.CASCADE)
    adopter_id = models.ForeignKey(
        Adopter, on_delete=models.CASCADE
    )  # Reference to Adopter model
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Application for {self.dog.name} by {self.adopter.first_name} {self.adopter.last_name}"
