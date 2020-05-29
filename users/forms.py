from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class InstaRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True,label='',widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Email'}))
    fullName = forms.CharField(max_length=60,required = True, label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}))
    username = forms.CharField(max_length=60,required = True, label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password1 = forms.CharField(max_length = 30,required = True, label='', widget = forms.TextInput(attrs={
        "class":"form-control",
        "name":"password1",
        "type":"password",
        "placeholder":"Password"
    }))
    password2 = forms.CharField(max_length = 30,required = True,label='', widget = forms.TextInput(attrs={
        "class":"form-control",
        "name":"password2",
        "type":"password",
        "placeholder":"Confirm Password"
    }))

    class Meta:
        model = User
        fields = ['email','fullName','username','password1','password2']

    def save(self, commit=True):
        user =super(InstaRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.fullName = self.cleaned_data['fullName']
        user.username = self.cleaned_data['username']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()


        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required = True,label='',widget=forms.TextInput(attrs = {'class':'form-control','placeholder':'Email'}))
    fullName = forms.CharField(max_length=60,required = True, label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}))
    username = forms.CharField(max_length=60,required = True, label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))

    class Meta:
        model = User
        fields = ['email','fullName','username']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio']