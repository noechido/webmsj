from django.shortcuts import render
from howtohelp.models import MonetaryInfo, HelpMethod, Site


# Create your views here.
def help_view(request):
    mi_list = MonetaryInfo.objects.all()
    hm_list = HelpMethod.objects.all()
    if len(mi_list) >= 1:
        mi_list = mi_list[0]
    else:
        mi_list = None
    site = Site.objects.all()
    if len(site) > 0:
        site = site[0]
    else:
        site = None

    entry_dict = {
        "mi": mi_list,
        "hm": hm_list,
        "site": site
    }
    return render(request, 'howtohelp/index.html', context=entry_dict)

