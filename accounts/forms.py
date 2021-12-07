from django import forms
from django.forms import fields
from .models import Account

class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-control',
    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-control',
    }))
    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone_Number',
        'class': 'form-control',
    }))
    
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email Address',
        'class': 'form-control',
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
    }))
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
            
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not Match!"
            )
            
    def __int__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'