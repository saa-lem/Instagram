# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .forms import InstaRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Profile

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = InstaRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            fullName = form.cleaned_data['fullName']
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = InstaRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserUpdateForm(instance = request.user)
        
        p_form = ProfileUpdateForm(instance = request.user.profile)


    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'users/profile.html',context)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile