from django.shortcuts import redirect, render
from .models import Site
from .forms import MainForm

def home(request):
    return render(request, 'survey/home.html')

def sites(request):
    context = {
        'title': 'Visitor Management System',
        'sites': Site.objects.all()
    }
    return render(request, 'survey/sites.html', context)

def signout(request):
    return render(request, 'survey/signout.html')

def forms(request, pk):
    site = Site.objects.get(id=pk)
    accomodation = site.accomodation
    exclude = {
        'accomodation': accomodation
    }
    
    if request.method == 'POST':
        main_form = MainForm(exclude, request.POST)
        if main_form.is_valid():
            visitor = main_form.save()
            site.visitors.add(visitor)
            return redirect('vis-man-home')

    main_form = MainForm(exclude)
    context = {
        'site':site,
        'main_form': main_form
    }
    return render(request, 'survey/form.html', context)
    