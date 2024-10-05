from django.contrib import admin
from aplication.core.models import Clinic, Doctor, License, Profession

# Register your models here.
admin.site.register(Doctor)
admin.site.register(License)
admin.site.register(Profession)
admin.site.register(Clinic)