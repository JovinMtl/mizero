from django.urls import path, re_path
from . import views



urlpatterns = [
    # path('', views.home, name= 'home'),
    # path( r"^<str:nom>/", views.good, name= 'good'),
    # re_path(r'^(?P<name>\str', views.good),
    # url(r'^.*$', views.good),
    path('', views.home),
    path('<str:key>', views.good),


]