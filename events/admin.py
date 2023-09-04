from django.contrib import admin
from events.models import Event, Notice, Site

# Register your models here.
admin.site.register(Event)
admin.site.register(Notice)
admin.site.register(Site)
