from django import forms
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
    email.widget.attrs.update({'class': 'form-control'})
