from django.contrib import admin
from rutinas.models import Sucursal, Instructor, Rutina, Sexo

# Register your models here.

admin.site.register(Sucursal)
admin.site.register(Instructor)
admin.site.register(Rutina)
admin.site.register(Sexo)
