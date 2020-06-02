# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from .models import *


# Create your tests here.


class TestImage(TestCase):

    def setUp(self):
        self.new_user = User(email='lee@gmail.com',
                             username='lee', password='leejones1')
        self.new_user.save()

        self.new_image = Image(image='media/default.jpg', image_name='hacker', image_caption='This guy is a real hacker',
                               profile=self.new_user.profile)
        self.new_image.save_image()

    def test_isinstance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_save_image(self):
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def tear_down(self):
        self.remove()


class TestProfile(TestCase):
    def setUp(self):
        self.new_user = User(email='lee@gmail.com',
                             username='lee', password='leejones1')
        self.new_user.save()

        self.new_image = Image(image='media/default.jpg', image_name='hacker', image_caption='This guy is a real hacker',
                               profile=self.new_user.profile)
        self.new_image.save_image()
        self.new_profile = self.new_user.profile
        self.new_profile.save_profile()

    def test_isinstance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))


    def test_save_profile(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_profile(self):
        self.new_profile.delete_profile()
        profiles = Profile.objects.all()

        self.assertTrue(len(profiles)==0)

    def tear_down(self):
        self.remove()


class TestComment(TestCase):

    def setUp(self):
        self.new_user = User(email='lee@gmail.com',
                             username='lee', password='leejones1')
        self.new_user.save()

        self.new_image = Image(image='media/default.jpg', image_name='hacker', image_caption='This guy is a real hacker',
                               profile=self.new_user.profile)
        self.new_image.save_image()

        self.new_comment = Comment(
            content='lovely image', image=self.new_image, user= self.new_user)

        self.new_comment.save_comments()


    def test_isinstance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))  


    def test_save_comment(self):
        comments = Comment.objects.all()
        self.assertTrue(len(comments)>0)


    def test_delete_comment(self):
        self.new_comment.delete_comments()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)==0)

    def tear_down(self):
         self.remove()