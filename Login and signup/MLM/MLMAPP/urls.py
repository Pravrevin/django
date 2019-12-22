from django.urls import path
from MLMAPP import views

urlpatterns = [
    path('registration/', views.registration),
]