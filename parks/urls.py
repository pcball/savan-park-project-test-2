from django.urls import path

from . import views

app_name = "parks"

urlpatterns = [
    path("", views.home, name="home"),
    path("tenants/", views.tenants, name="tenants"),
    path("news/", views.news, name="news"),
    path("services/", views.services, name="services"),
    path("invest/", views.invest, name="invest"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
]
