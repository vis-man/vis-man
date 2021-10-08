from django import forms
from django.core.exceptions import ValidationError
from .models import Visitor


class Sign_in_Form(forms.ModelForm):
    # Visitor roles
    role_choices = (('staff', 'UWA Staff'),
                    ('student', 'UWA Student'),
                    ('other_staff', 'Other University staff'),
                    ('other_student', 'Other University student'),
                    ('contractor', 'Contractor'),
                    ('other', 'Other'))

    role_dropdown = forms.CharField(label='Select Role', initial=('staff', 'UWA Staff'), widget=forms.Select(choices=role_choices, attrs={'class': 'form-control'}))

    # Custom cleaning function that is called during 'sign_in_form.is_valid()' in views.py
    def clean(self):
        cleaned_data = super(Sign_in_Form, self).clean()
        this_email = cleaned_data.get('email')
        this_visitor = Visitor.objects.filter(email=this_email).first()
        if this_visitor:
            checked_out = this_visitor.checkout
            if not checked_out:
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
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'nightstay': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'emergency_first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_phone': forms.TextInput(attrs={'class': 'form-control'}),
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

    def __init__(self, exclude, *args, **kwargs):
        super(Sign_in_Form, self).__init__(*args, **kwargs)
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

class Sign_out_Form(forms.Form):
    email = forms.EmailField(label='Email')
    email.widget.attrs.update({'class': 'form-control'})

    # custom cleaning function that is called during 'sign_out_form.is_valid()' in views.py
    def clean(self):
        cleaned_data = super(Sign_out_Form, self).clean()
        this_email = cleaned_data.get('email')

        visitor = Visitor.objects.filter(email=this_email).first()
        if not visitor:
            raise ValidationError("Please enter the correct credentials.")
        else:
            checked_out = visitor.checkout
            if checked_out:
                raise ValidationError("You are already checked out.")

        return cleaned_data
