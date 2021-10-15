from django.shortcuts import redirect, render
from .models import Site, Visitor, History
from .forms import Sign_in_Form, Sign_out_Form
from datetime import datetime
from django.contrib import messages

'''Sign-on/Sign-out page'''
def enter_exit(request, pk):
    context = {
        'site': Site.objects.get(id=pk),
    }
    return render(request, 'survey/enter_exit.html', context)


'''Main page which shows list of sites'''
def sites(request):
    context = {
        'sites': Site.objects.all()
    }
    return render(request, 'survey/sites.html', context)


'''Sign-out page to checkout visitors'''
def sign_out(request):
    sign_out_form = Sign_out_Form()
    if request.method == 'POST':
        sign_out_form = Sign_out_Form(request.POST)
        # If not error with the email and user exists, proceed.
        if sign_out_form.is_valid():
            # Find the visitor with that email
            e = sign_out_form.cleaned_data['email']
            this_visitor = Visitor.objects.get(email=e)
            # Add visitors stay details to history
            history = History(
                checkin=this_visitor.checkin,
                checkout=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                site=this_visitor.site,
                nightstay=this_visitor.nightstay,
                visitor=this_visitor
            )
            history.save()
            # Checkout visitor
            this_visitor.checkout = True
            this_visitor.save()
            pk = this_visitor.site.id
            messages.success(request, 'Signed out successfully')
            return redirect('enter_exit', pk=pk)
    # If request is GET just render the form and Sign out page
    context = {
        'sign_out_form': sign_out_form
    }
    return render(request, 'survey/sign_out.html', context)


'''Sign-in form to checkin visitors'''
def sign_in(request, pk):
    site = Site.objects.get(id=pk)
    accomodation = site.accomodation
    exclude = {
        'accomodation': accomodation
    }
    # if site does not have an accomodation, we shouldn't ask if visitor wants to
    # stay overnight. We pass this information to the form, via exclude.
    sign_in_form = Sign_in_Form(exclude)
    if request.method == 'POST':
        sign_in_form = Sign_in_Form(exclude, request.POST)
        e = sign_in_form['email'].value()
        # Check if visitor already exists in the database. If yes, just update
        # Their details and check them in.
        if Visitor.objects.filter(email=e).exists():
            visitor = Visitor.objects.get(email=e)
            sign_in_form = Sign_in_Form(exclude, request.POST, instance=visitor)
        # sign_in_form now either has a new user or an existing user. So, now
        # we just save their information and check them in to the relevant site.
        if sign_in_form.is_valid():
            visitor = sign_in_form.save()
            visitor.site = site
            visitor.checkout = False
            visitor.checkin = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            visitor.save()
            messages.success(request, 'Signed in Successfully.')
            return redirect('enter_exit', pk=pk)

    context = {
        'site': site,
        'sign_in_form': sign_in_form
    }
    return render(request, 'survey/sign_in.html', context)
