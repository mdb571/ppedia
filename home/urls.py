from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', views.home,name='home'),
    path('gloves/',views.gloves,name='gloves'),
    path('masks/',views.masks,name='masks'),
    path('boots/',views.boots,name='boots'),
    path('gowns/',views.gowns,name='gowns'),
    path('goggles/',views.goggles,name='goggles'),
    ]
