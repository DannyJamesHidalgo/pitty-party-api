from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Dog,
    Adopter,
    Adoption,
    Fostering,
    MedicalRecord,
    Event,
    Application,
)

admin.site.register(Dog)
admin.site.register(Adopter)
admin.site.register(Adoption)
admin.site.register(Fostering)
admin.site.register(MedicalRecord)
admin.site.register(Event)
admin.site.register(Application)
