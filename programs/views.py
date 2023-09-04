"""
Created by Framework
This file is where you can create views for the App
Modified by: Jorge Nino
Date: 15/03/20
"""
from django.shortcuts import render
from .models import Program, Site


# Create your views here.
def programs_view(request):
    programs = Program.objects.all()
    site = Site.objects.all()
    if len(site) > 0:
        site = site[0]
    else:
        site = None
    return render(request, 'programs/index.html', context={
        "programs": programs,
        "site": site
    })
