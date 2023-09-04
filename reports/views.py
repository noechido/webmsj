"""
Created by Framework
This file is where you can create views for the App
Modified by: Jorge Nino
Date: 15/03/20
"""
from django.shortcuts import render
from .models import Report, Site, Certification, Other


# Create your views here.
def reports_view(request):
    reports = Report.objects.all()
    certification = Certification.objects.all()
    site = Site.objects.all()
    other = Other.objects.all()
    if len(site) > 0:
        site = site[0]
    else:
        site = None
    return render(request, 'reports/index.html', context={
        "reports": reports,
        "certifications": certification,
        "other": other,
        "site": site
    })