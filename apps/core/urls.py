# Django Imports
from django.urls import path

# Application Imports
from apps.core.views import DefaultIndexPageView

urlpatterns = [
    path('', DefaultIndexPageView, name='index'),
]
