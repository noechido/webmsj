from django.contrib import admin
from contact.models import Site, Message, Contact

# Register your models here.
admin.site.register(Site)
admin.site.register(Message)
admin.site.register(Contact)
