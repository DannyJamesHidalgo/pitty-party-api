from django.db import models
from .Adopter import Adopter


class Adoption(models.Model):
    dog = models.ForeignKey("Dog", on_delete=models.CASCADE)
    adopter = models.ForeignKey(
        Adopter, on_delete=models.CASCADE
    )  # Reference to Adopter model
    adoption_date = models.DateField()
    adoption_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Adoption of {self.dog.name} by {self.adopter.first_name} {self.adopter.last_name}"
