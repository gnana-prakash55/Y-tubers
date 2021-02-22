from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber
from contactinfo.models import Contactinfo


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_ytubers = Youtuber.objects.order_by('-created_date').all()
    contact = Contactinfo.objects.first()
    data = {
        'sliders':sliders,
        'teams':teams,
        'featured_youtubers':featured_youtubers,
        'all_ytubers':all_ytubers,
        'contact':contact,
    }
    return render(request,'webpages/home.html',data)

def about(request):
    teams = Team.objects.all()
    contact = Contactinfo.objects.first()
    data = {
        'teams':teams,
        'contact':contact,
    }
    return render(request,'webpages/about.html',data)

def services(request):
    contact = Contactinfo.objects.first()
    data = {
        'contact':contact,
    }
    return render(request,'webpages/services.html',data)

def contact(request):
    contact = Contactinfo.objects.first()
    data = {
        'contact':contact,
    }
    return render(request,'webpages/contact.html',data)