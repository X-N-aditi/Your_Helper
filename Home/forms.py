from django import forms
from .models import Customer, ServiceProvider, Booking

from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'age', 'phone_number', 'address', 'state', 'city', 'pincode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
        }


from django import forms
from .models import ServiceProvider

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['name', 'email', 'service', 'title', 'service_charge', 'service_duration',
                  'age', 'dob', 'phone_number', 'address', 'state', 'city', 'pincode',
                  'identity_proof', 'year_of_experience', 'experience_certificate', 'photo']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'service_charge': forms.NumberInput(attrs={'class': 'form-control'}),
            'service_duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'identity_proof': forms.FileInput(attrs={'class': 'form-control'}),
            'year_of_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'experience_certificate': forms.FileInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }



class LoginForm(forms.Form):
    email = forms.EmailField()

class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['address']
    
