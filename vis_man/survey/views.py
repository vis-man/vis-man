from django.shortcuts import redirect, render
from .models import Site
from .forms import MainForm

def home(request):
    context = {
        'title': 'Visitor Management System',
        'sites': Site.objects.all()
    }
    return render(request, 'survey/home.html', context)

def sites(request, pk):
    if request.method == 'POST':
        main_form = MainForm(request.POST)
        if main_form.is_valid():
            main_form.save()
            return redirect('vis-man-home')
    else:
        main_form = MainForm()
        context = {
            'site': Site.objects.get(id=pk),
            'main_form': main_form
        }
    return render(request, 'survey/form.html', context)
    