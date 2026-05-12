from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teachers/', views.teachers, name='teachers'),
    path('events/', views.events, name='events'),
]
