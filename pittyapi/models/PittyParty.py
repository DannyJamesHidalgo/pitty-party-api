from django.db import models


class PittyParty(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Pitty Party on {self.date}"
