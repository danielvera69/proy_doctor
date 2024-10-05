from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from aplication.core.forms import DoctorForm
from aplication.core.models import Doctor
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
   data={"title":"Medical","title1":"Sistema Medico Online"}
   #return HttpResponse("<h1>Pantalla de Inicio</h1>")
   #return JsonResponse(data)
   return render(request,'core/home.html',data)

def doctor_List(request):
    data={"title":"Medical","title1":"Consulta de Doctores"}
    doctores = Doctor.objects.all() # queryset[d1,d2,d3]
    for doctor in doctores:
       print(doctor.first_name," ",doctor.clinic.name)
    data["doctores"]=doctores
    print(data)
    return render(request,"core/doctor/list.html",data)

def doctor_create(request):
   data = {"title": "Doctores","title1": "Añadir Doctores"}
   if request.method == "POST":
      print(request.POST)
      form = DoctorForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("core:doctor_list")
      else:
         data["form"] = form
         data["error"] = "Error al crear el Doctor."
         return render(request, "core/doctor/form.html", data)
   else:
      form = DoctorForm()
      # <tr>inputtext,select <\>
      data["form"] = form
   print(form)
   return render(request, "core/doctor/form.html", data)
 
def doctor_update(request,id):
   data = {"title": "Doctores","title1": "Editar Doctor"}
   doctor = Doctor.objects.get(pk=id)# doctor1
   if request.method == "POST":
      form = DoctorForm(request.POST,instance=doctor)
      if form.is_valid():
         form.save()
         return redirect("core:doctor_list")
      else:
         data["form"] = form
         data["error"] = "Error al editar el Doctor."
         return render(request, "core/doctor/form.html", data)
   else:
      form = DoctorForm(instance=doctor)
      data["form"] = form
   print(form)
   return render(request, "core/doctor/form.html", data)
@login_required
def doctor_delete(request,id):
   doctor = Doctor.objects.get(id=id)
   data = {"title":"Eliminar","title1":"Eliminar Doctor","doctor":doctor}
   if request.method == "POST":
      doctor.delete()
      return redirect("core:doctor_list")
   return render(request, "core/doctor/delete.html", data)