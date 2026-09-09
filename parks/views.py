from django.shortcuts import render

from .models import HeroStat, NewsItem, Tenant


def home(request):
    context = {
        "stats": HeroStat.objects.all(),
        "tenants": Tenant.objects.filter(is_featured=True)[:6],
        "news": NewsItem.objects.all()[:3],
    }
    return render(request, "parks/home.html", context)


def tenants(request):
    return render(request, "parks/tenants.html", {"tenants": Tenant.objects.all()})


def news(request):
    return render(request, "parks/news.html", {"news": NewsItem.objects.all()})


def services(request):
    return render(request, "parks/services.html")


def invest(request):
    return render(request, "parks/invest.html")


def gallery(request):
    return render(request, "parks/gallery.html")


def contact(request):
    return render(request, "parks/contact.html")
