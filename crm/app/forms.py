"""
Definition of forms.
"""


from app.models import * 
from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from bootstrap_datepicker.widgets import DatePicker


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__'


class ClientForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)    

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args,**kwargs)
        #self.fields.pop('username')

    class Meta(UserCreationForm.Meta):
        model = Client   
        fields = '__all__'
        # fields = UserCreationForm.Meta.fields
        # + s'__all__'
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError ("Passwords don't match")
        return password2    
    
    def save(self, commit=True):
        exits = Client.objects.filter(email=self.cleaned_data["email"]).exists()
        if exits:
            print('We have the user')
            user = Client.objects.get(email=self.cleaned_data["email"])
        else:
            print('No user found')
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        #check if there is a user already created with this
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ManagerForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)    

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args,**kwargs)
        #self.fields.pop('username')

    class Meta(UserCreationForm.Meta):
        model = Client   
        fields = '__all__'
        # fields = UserCreationForm.Meta.fields
        # + s'__all__'
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError ("Passwords don't match")
        return password2    
    
    def save(self, commit=True):
        exits = Client.objects.filter(email=self.cleaned_data["email"]).exists()
        if exits:
            print('We have the user')
            user = Client.objects.get(email=self.cleaned_data["email"])
        else:
            print('No user found')
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        #check if there is a user already created with this
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user





