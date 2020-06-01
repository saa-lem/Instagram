# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,RedirectView
from django.http import HttpResponse
from .models import Image, Comment,Followers
from users.models import Profile
# Create your views here.
def home(request):
    message = "Welcome to Instagram"

    images = Image.objects.all()
    user = User.objects.get(username=request.user.username)

    context = {
        "message":message,
        'images':images,
        'user':user
    }
    return render(request, 'instagram/home.html',context)

class ImageListView(LoginRequiredMixin,ListView):
    
    model = Image
    template_name='instagram/home.html'
    context_object_name ='images'
    ordering = ['-created_on']

class ImageDetailView(DetailView):
    model = Image

# class ProfileDetailView(DetailView):
#     model = Profile

class ImageCreateView(LoginRequiredMixin,CreateView):
     
    model = Image
    fields = ['image','image_name','image_caption']

    def form_valid(self,form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

    
   

class ImageUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
     
    model = Image
    fields = ['image','image_name','image_caption']

    def form_valid(self,form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


    def test_func(self):
        image = self.get_object()

        if self.request.user.profile == image.profile:
            return True

        return False


class CommentCreateView(LoginRequiredMixin,CreateView):
     
    model = Comment
    fields = ['content','image', 'user']
    success_url = ('/')

    def form_valid(self,form):
      
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)

 

  

class ImageLikeRedirectView(RedirectView):
    def get_redirect_url(self,pk, *args, **kwargs):
        obj = get_object_or_404(Image, pk = pk)
        url= obj.get_absolute_url()
      
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
                status =''
            else:
                obj.likes.add(user)
                status='red'
        return url

class ImageDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Image
    success_url = ('/')
    def test_func(self):
        image = self.get_object()

        if self.request.user.profile == image.profile:
            return True

        return False
#  



class UserImageListView(ListView):
    model = Image
    template_name='instagram/home.html'
    context_object_name ='images'
    ordering = ['-created_on']


    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Image.objects.filter(profile=user.profile).order_by('-created_on')



def search_results(request):
    if 'search_user' in request.GET and request.GET["search_user"]:
        search_term = request.GET.get("search_user")
        searched_users = User.objects.filter(username__icontains=search_term)
        message=search_term
        return render(request, "instagram/search.html", {"images":searched_users, "message":message})

    else:
        message = "Search term not found"

        return render(request,'instagram/search.html',{"message":message})
def display_profile(request,username):
    profile = Profile.objects.get(user__username= username)

    context={
        "profile":profile
    }
    return render(request,'users/profile_detail.html',context)





def get_followers(request,username):
    follow = Followers.objects.filter(follower = request.user ,followed=User.objects.filter(username = username).first()).all()
    if follow :
        follow = Followers(follower = request.user ,followed=User.objects.filter(username = username).first())
        follow.save()
    else:
        follow.delete()
    
    return redirect(f'/profile/details/{username}')