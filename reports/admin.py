from django.contrib import admin
from reports.models import Report, Site, Certification, Other

# Register your models here.
admin.site.register(Report)
admin.site.register(Site)
admin.site.register(Certification)
admin.site.register(Other)
