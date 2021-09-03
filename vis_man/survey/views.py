from django.shortcuts import render
from .models import Site

def home(request):
    context = {
        'title': 'Visitor Management System',
        'sites': Site.objects.all()
    }
    return render(request, 'survey/home.html', context)

def sites(request, pk):
    context = {
        'site': Site.objects.get(id=pk)
    }
    return render(request, 'survey/form.html', context)
    