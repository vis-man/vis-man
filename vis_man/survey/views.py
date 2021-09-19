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

        this_phone_number = main_form['phone_number'].value()

        if Visitor.objects.filter(phone_number=this_phone_number).exists():
            print("\t Visitor with this phone number already exists. Updating...")
            this_visitor = Visitor.objects.get(phone_number=this_phone_number)
            # the 'instance=this_visitor' arg tells django to update the relevant visitor.
            main_form = MainForm(exclude, request.POST, instance=this_visitor)
        else:
            print("\t This is a new visitor.")
            main_form = MainForm(exclude, request.POST)

        if main_form.is_valid():
            visitor = main_form.save()
            site.visitors.add(visitor)

            ph = main_form.cleaned_data['phone_number']

            this_visitor = Visitor.objects.get(phone_number=ph)
            this_visitor.checkout = False
            print("CHECKOUT:")
            print(this_visitor)
            print(this_visitor.checkout)
            this_visitor.save()
            ###
            return redirect('vis-man-home')

    context = {
        'site':site,
        'main_form': main_form
    }
    return render(request, 'survey/form.html', context)
    
