from django.urls import path
from . import views

app_name = 'driver_manual'
urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
]