# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='media/uploads/', default='media/default.jpg')
    image_name = models.CharField(max_length=60)
    image_caption = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, blank = True, related_name ='image_likes')
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def get_absolute_url(self):
        return reverse('image-detail',kwargs = {'pk':self.pk} )



class Comment(models.Model):
    
    image =models.ForeignKey(Image, related_name = 'image_comments',on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    content = models.TextField()

    def __str__(self):
        return self.content

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()
