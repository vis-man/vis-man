from django.shortcuts import redirect, render
from .models import Site, Visitor, History
from .forms import MainForm, Signout
from datetime import datetime
# from django.contrib import messages 

def home(request):
    return render(request, 'survey/home.html')

def sites(request):
    context = {
        'title': 'Visitor Management System',
        'sites': Site.objects.all()
    }
    return render(request, 'survey/sites.html', context)

def signout(request):
    if request.method == 'POST':
        signout_form = Signout(request.POST)
        if signout_form.is_valid():
            e = signout_form.cleaned_data['email']
            ph = signout_form.cleaned_data['phone_number']
            visitor = Visitor.objects.get(email=e, phone_number=ph)
            if not visitor.checkout:
                site = Site.objects.get(visitors=visitor)
                site.visitors.remove(visitor)

                history = History(
                    checkin = visitor.checkin,
                    checkout = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    nightstay = visitor.nightstay
                )

                history.visitor = visitor
                history.save()
                visitor.checkout = True
                visitor.save()
                return redirect('vis-man-home')

    signout_form = Signout()
    context = {
        'signout_form': signout_form
    }
    return render(request, 'survey/signout.html', context)

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
    