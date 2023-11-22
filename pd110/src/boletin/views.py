from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import RegModelForm, ContactForm
from .models import Registrado


def inicio(request):
    titulo = "Bienvenido"
    encabezado = "Registrarse en la página"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)
    #print(dir(form))  sirve para ver que puedo hacer con el form
    
    context = {
        'el_form': form,
        'el_titulo': titulo,
        "encabezado": encabezado
    }
    
    
    if form.is_valid():
        instance = form.save(commit = False)
        email = form.cleaned_data.get("email")
        nombre = form.cleaned_data.get("nombre")
        if not instance.nombre:
            instance.nombre = "Persona"
        instance.save()
        
        context= {
            'el_titulo': "Gracias %s !" %(nombre),
        }
        
        if not nombre:
            context= {
                "el_titulo": "Gracias %s" %(email)
            }
        
        # print(instance)
        # print(instance.timestamp)
        
    if request.user.is_authenticated and request.user.is_staff:
        quueryset = Registrado.objects.all().order_by("-timestamp").filter(nombre__icontains= "")
        context ={
            "queryset": quueryset,
        }
    return render(request, "inicio.html", context)

def contact(request):
    titulo = "Contáctenos"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        """# instance = form.save(commit = False)
        for key, value in form.cleaned_data.items():
            print(key + ": ", value)
            # instance.save()"""
            
            
        
        #otra forma
        # for key in form.cleaned_data:
        #     print(key)
        #     print(form.cleaned_data.get(key))
        

        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = 'Form de contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "otroemail@gmail.com"]
        email_mensaje= "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto,
                  email_mensaje,
                  email_from,
                  email_to,
                  fail_silently=False
                  )
        #print(email, mensaje, nombre)
    context = {
        "form": form,
        'titulo': titulo,
    }
    return render(request, "forms.html", context)