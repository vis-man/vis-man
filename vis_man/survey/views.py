from django.shortcuts import redirect, render
from .models import Site, Visitor, History
from .forms import MainForm, Signout
from datetime import datetime

def home(request):
    return render(request, 'survey/home.html')

def sites(request):
    context = {
        'title': 'Visitor Management System',
        'sites': Site.objects.all()
    }
    return render(request, 'survey/sites.html', context)

def signout(request):
    signout_form = Signout()
    
    if request.method == 'POST':
        signout_form = Signout(request.POST)
        if signout_form.is_valid():
            e = signout_form.cleaned_data['email']
            this_visitor = Visitor.objects.get(email=e)
            site_to_remove = this_visitor.site
            if not this_visitor.checkout:
                history = History(
                    checkin = this_visitor.checkin,
                    checkout = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    site = this_visitor.site,
                    nightstay = this_visitor.nightstay,
                    visitor = this_visitor
                )

                history.save()
                this_visitor.checkout = True
                this_visitor.save()
                return redirect('vis-man-home')

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

    main_form = MainForm(exclude)
    
    if request.method == 'POST':
        main_form = MainForm(exclude, request.POST)

        visitor_email = main_form['email'].value()

        # check if visitor exists and update main_form accordingly
        if Visitor.objects.filter(email=visitor_email).exists():
            visitor = Visitor.objects.get(email=visitor_email)
            main_form = MainForm(exclude, request.POST, instance=visitor)
        else:
            main_form = MainForm(exclude, request.POST)
        
        # check form is valid: save form if it is
        if main_form.is_valid():
            visitor = main_form.save()
            visitor.site = site
            visitor.checkout = False
            visitor.save()
            return redirect('vis-man-home')

    context = {
        'site':site,
        'main_form': main_form
    }
    return render(request, 'survey/form.html', context)
    
