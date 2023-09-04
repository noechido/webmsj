from django.contrib import admin
from howtohelp.models import MonetaryInfo, HelpMethod, Site

# Register your models here.
admin.site.register(MonetaryInfo)
admin.site.register(HelpMethod)
admin.site.register(Site)