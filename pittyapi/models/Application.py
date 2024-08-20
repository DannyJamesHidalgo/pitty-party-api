from django.db import models
from .Adopter import Adopter


class Application(models.Model):
    dog = models.ForeignKey("Dog", on_delete=models.CASCADE)
    adopter = models.ForeignKey(
        "Adopter", on_delete=models.CASCADE
    )  # Reference to Adopter model
    approved = models.BooleanField(default=False)

    # New fields: Phone number, Email, and Adoption pitch
    phone_number = models.CharField(
        max_length=20, blank=True, null=True
    )  # Adjust max_length as needed
    email = models.EmailField(blank=True, null=True)
    adoption_pitch = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255)
    question_1 = models.BooleanField(default=False)
    question_2 = models.BooleanField(default=False)
    question_3 = models.BooleanField(default=False)

    def __str__(self):
        return f"Application for {self.dog.name} by {self.adopter.first_name} {self.adopter.last_name}"
