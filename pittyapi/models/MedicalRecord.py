from django.db import models


class MedicalRecord(models.Model):
    dog = models.ForeignKey("Dog", on_delete=models.CASCADE)
    date = models.DateField()
    treatment = models.TextField()
    veterinarian = models.CharField(max_length=255)

    def __str__(self):
        return f"Medical record for {self.dog.name}"
