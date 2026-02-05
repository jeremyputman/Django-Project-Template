# Django Imports
from django.shortcuts import render

def custom_403_view(request, exception=None):
    return render(request, "core/errors/403.html", status=403)

def custom_404_view(request, exception=None):
    return render(request, "core/errors/404.html", status=404)

def DefaultIndexPageView(request):
    return render(request, "core/index.html")