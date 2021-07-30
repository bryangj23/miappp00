from django.urls import path
from .views import miPrimeraVista

urlpatterns = [
    path('inicio/',miPrimeraVista)
]
