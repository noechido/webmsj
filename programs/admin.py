from django.contrib import admin
from programs.models import Data, Program, Site, DataCollection

# Register your models here.
admin.site.register(Data)
admin.site.register(Program)
admin.site.register(DataCollection)
admin.site.register(Site)
