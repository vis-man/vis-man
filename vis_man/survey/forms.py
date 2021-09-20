from django import forms
from django.core.exceptions import ValidationError
from .models import Visitor
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class MainForm(forms.ModelForm):
    role_choices = (('staff', 'UWA Staff'),
                    ('student', 'UWA Student'),
                    ('other_staff', 'Other University staff'),
                    ('other_student', 'Other University student'),
                    ('contractor', 'Contractor'),
                    ('other', 'Other'))

    role_dropdown = forms.CharField(label='Select Role', initial=('staff', 'UWA Staff'), widget=forms.Select(choices=role_choices, attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super(MainForm, self).clean()

        this_phone_number = cleaned_data.get('phone_number')

        if Visitor.objects.filter(phone_number=this_phone_number).exists():
            this_visitor = Visitor.objects.filter(phone_number=this_phone_number).first()
            checked_out = getattr(this_visitor, 'checkout')
            if not checked_out:
                print("\t This visitor is already checked in somewhere else.")
                raise ValidationError("You are already checked in. Please check out to continue.")

        return cleaned_data

    class Meta:
        model = Visitor

        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
            'nightstay',
            'emergency_first_name',
            'emergency_last_name',
            'emergency_phone',
            'emergency_relation',
            'planned_checkout'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': PhoneNumberPrefixWidget(attrs={'class': 'form-control'}, initial='AU'),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'nightstay': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'emergency_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_phone': PhoneNumberPrefixWidget(attrs={'class': 'form-control'}, initial='AU'),
            'emergency_relation': forms.TextInput(attrs={'class': 'form-control'}),
            'planned_checkout': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'role': '',
            'nightstay': 'Are you planning to stay overnight?',
            'emergency_first_name': 'Emergency Contact First Name',
            'emergency_last_name': 'Emergency Contact last Name',
            'emergency_phone': 'Emergency Contact Number',
            'emergency_relation': 'Relationship',
            'planned_checkout': 'Planned Checkout',
        }

        error_messages = {
            'phone_number' : { 'invalid': 'Please enter a valid phone number.' },
            'emergency_phone' : { 'invalid': 'Please enter a valid phone number for your emergency contact.' },
        }

    def __init__(self, exclude, *args, **kwargs):
        super(MainForm, self).__init__(*args, **kwargs)
        self.order_fields(['first_name',
                       'last_name',
                       'email',
                       'phone_number',
                       'role_dropdown',
                       'role',
                       'nightstay',
                       'emergency_first_name',
                       'emergency_last_name',
                       'emergency_phone',
                       'emergency_relation',
                       'planned_checkout'])
        if not exclude['accomodation']:
            del self.fields['nightstay']
            del self.fields['emergency_first_name']
            del self.fields['emergency_last_name']
            del self.fields['emergency_phone']
            del self.fields['emergency_relation']

class Signout(forms.Form):
    email = forms.EmailField(label='Email')
    phone_number = PhoneNumberField(label=('Phone Number'), required=True, widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control'}, initial='AU'))
    phone_number.error_messages['invalid'] = 'Please enter a valid phone number.'
    email.widget.attrs.update({'class': 'form-control'})

    # custom cleaning function that is called during 'form.is_valid()' in views.py
    def clean(self):
        cleaned_data = super(Signout, self).clean()

        this_phone_number = cleaned_data.get('phone_number')
        this_email = cleaned_data.get('email')

        if not ((Visitor.objects.filter(phone_number=this_phone_number).exists()) or
        (Visitor.objects.filter(phone_number=this_email).exists())):
            print("\t This visitor does not exist in the DB.")
            raise ValidationError("Please enter the correct credentials.")
        
        this_visitor = Visitor.objects.filter(phone_number=this_phone_number).first()
        checked_out = getattr(this_visitor, 'checkout')

        if checked_out:
            print("\t This visitor is already checked out.")
            raise ValidationError("You are already checked out.")

        return cleaned_data
