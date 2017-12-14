# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    

class Review(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()
    book_reviewers = models.ManyToManyField(User)


# Create your models here.
