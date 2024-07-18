from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Dog,
    Adopter,
    Adoption,
    Fostering,
    MedicalRecord,
    PittyParty,
    Application,
)

admin.site.register(Dog)
admin.site.register(Adopter)
admin.site.register(Adoption)
admin.site.register(Fostering)
admin.site.register(MedicalRecord)
admin.site.register(PittyParty)
admin.site.register(Application)
