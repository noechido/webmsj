"""
Created by Framework
This file is where you can create views for the App
Modified by: Jorge Nino
Date: 15/03/20
"""
from django.shortcuts import render
from .models import Event, Notice, Site
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def events_view(request):
    events = Event.objects.all()
    notices = Notice.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(events, 3)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    page = request.GET.get('page', 1)
    paginator = Paginator(notices, 3)
    try:
        notices = paginator.page(page)
    except PageNotAnInteger:
        notices = paginator.page(1)
    except EmptyPage:
        notices = paginator.page(paginator.num_pages)
    site = Site.objects.all()
    if len(site) > 0:
        site = site[0]
    else:
        site = None

    return render(request, 'events/index.html', context={
        "events": events,
        "notices": notices,
        "site": site
    })
