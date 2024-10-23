from django.urls import reverse_lazy
from aplication.core.forms import DoctorForm
from aplication.core.models import Doctor

# mixin para crear y editar un doctor
class DoctorMixin:
    model = Doctor
    form_class = DoctorForm
    template_name = "core/doctor/form.html"
    success_url = reverse_lazy("core:doctor_list")  # Redirigir a la lista de doctores después de crear uno nuevo
  