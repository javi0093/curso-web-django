from django.contrib import admin
from .models import Registrado
from .forms import RegModelForm
# Register your models here.

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email", "nombre", "timestamp"]
    form = RegModelForm
    #list_display_links= ["nombre"]
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    list_field= ["email", "nombre"]
    #class Meta:
    #    model = Registrado




admin.site.register(Registrado, AdminRegistrado)