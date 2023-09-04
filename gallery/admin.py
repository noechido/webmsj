from django.contrib import admin
from gallery.models import Images, Site, Category, Year

# Register your models here.
admin.site.register(Images)
admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Year)
