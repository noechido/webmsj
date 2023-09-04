from django.shortcuts import render
from .models import Contact, Site, Message
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import requests



def send_simple_message(emailto, emailfrom, message):
	return requests.post(
            "https://api.mailgun.net/v3/sandboxe684f8e35d2a44d6b493af7cb86426e3.mailgun.org/messages",
          		auth=("api", "c5b6466daa5ec2de2fa0920a1a64d636-e5e67e3e-782417a0"),
          		data={"from": str(emailfrom),
                            "to": [str(emailto)],
                            "subject": "Mensaje Sitio Web Misión San José",
                            "text": str(message)})


# Create your views here.
def contact_view(request):
    form = ContactForm()
    contacto = Contact.objects.all()
    site = Site.objects.all()

    if len(contacto) > 0:
        contacto = contacto[0]
    else:
        contacto = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            m = Message()
            m.nombre = request.POST.get('nombre')
            m.correo = request.POST.get('correo')
            m.mensaje = request.POST.get('mensaje')
            print(m.nombre, m.mensaje, m.correo)
            m.save()
            if (contacto):
                print('success')
                send_simple_message(contacto.mail, m.correo, m.mensaje)
            messages.success(request, 'Tu mensaje ha sido enviado.')
            return HttpResponseRedirect('/contacto')
        else:
            form = ContactForm()

    if len(site) > 0:
        site = site[0]
    else:
        site = None
    entry_dict = {
        "form": form,
        "contact": contacto,
        "site": site
    }
    return render(request, 'contact/index.html', context=entry_dict)
