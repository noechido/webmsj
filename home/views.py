"""
Created by Framework
This file is where you can create views for the App
Modified by: Jorge Nino
Date: 15/03/20
"""
from django.shortcuts import render
from home.models import Images, Video, AboutUs, Patrons, Directors, Mision, Vision, Values


# Create your views here.
def index(request):
    images_list = Images.objects.all()
    about_list = AboutUs.objects.all()
    video_list = Video.objects.all()
    patrons_list = Patrons.objects.all()
    director_list = Directors.objects.all()
    mision_list = Mision.objects.all()
    vision_list = Vision.objects.all()
    values_list = Values.objects.all()
    if len(images_list) >= 3:
        images_list = images_list[:3]
    if len(mision_list) >= 1:
        mision_list = mision_list[0]
    if len(vision_list) >= 1:
        vision_list = vision_list[0]
    if len(about_list) >= 1:
        about_list = about_list[0]
    if len(video_list) > 0:
        video_list = video_list[0].url.replace('watch?v=', 'embed/')
    else:
        video_list = None

    entry_dict = {
        "imagenes": images_list,
        "valores": values_list,
        "vision": vision_list,
        "mision": mision_list,
        "video": video_list,
        "about": about_list,
        "directors": director_list,
        "patrons": patrons_list
    }
    return render(request, 'home/index.html', context=entry_dict)
