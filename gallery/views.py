from django.shortcuts import render
from .models import Images, Site, Year


# Create your views here.
def gallery_view(request):
    year_list = Year.objects.order_by('anio').all()
    site = Site.objects.all()
    if len(site) > 0:
        site = site[0]
    else:
        site = None

    return render(request, 'gallery/index.html', context={
        "years": year_list,
        "site": site
    })


def gallery_detail_view(request, year):
    images_list = Year.objects.all().filter(anio=year)[0].imagenes.all
    site = Site.objects.all()
    if len(site) > 0:
        site = site[0]
    else:
        site = None
    return render(request, 'gallery/gallery_detail.html', context={
        "images": images_list,
        "site": site
    })
