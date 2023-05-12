from django.urls import path
from .views import save


urlpatterns = [
    path('filme/', save),
]