# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
import re

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def index(request):
    

    request.session["init"] = True
    return render(request, 'index.html')

def new_user(request):
    print request.method
    error = False
    if request.method == "POST":
        name = request.POST["name"]
        alias = request.POST["alias"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        error = False
        if len(email) < 0 or len(password) < 0 or len(name) < 0 or len(alias) < 0:
            messages.add_message(request, messages.INFO, "Please Input All Fields")
            error = True
        if len(password) < 8:
            messages.add_message(request, messages.INFO, "Passwords must be longer than 8 characters")
            error = True
        if password != confirm:
            messages.add_message(request, messages.INFO, "Passwords must match")
            error = True
        if not re.match(EMAIL_REGEX, email):
            messages.add_message(request, messages.INFO, "Email must be in proper format")
            error = True

        if error == True:
            print "There was an error numnuts"
            return redirect("/new_user")

        request.session["context"] = {
            "name" : name,
            "alias" : alias,
            "email" : email,
            "password" : password,
            "confirm" : confirm
        }
        User.objects.create(name=name,alias=alias, email=email, password=password)
        
        return redirect("/books")
    else:
        return redirect("/")
def login(request):
    print request.method
    error = False
    if request.method == "POST":
        error = False
        email = request.POST["email"]
        password = request.POST["password"]
        name = User.objects.filter(email=email)
        if len(email) < 0 or len(password) < 0:
            messages.add_message(request, messages.INFO, "Please Input All Fields")
            error = True
        current_user = User.objects.filter(email=email)

        if len(current_user) < 1:
            messages.add_message(request, messages.INFO, "No users in database")
            error = True
        for user in current_user:
            if user.email != email or user.password != password:
                messages.add_message(request, messages.INFO, "Email or password did not match user in database.")
                error = True

        if error == True:
            return redirect("/")    

        
        request.session["context"] = {
            "name" : name[0].name,
            "email" : email,
            "password" : password
           
        }
        print "hey"
        return redirect("/books")

def books(request):
    context = request.session["context"]
    all_users = User.objects.all()
    all_reviews = Review.objects.all()
    context["all_users"] = all_users
    context["all_reviews"] = all_reviews
    print all_users
    all
    return render(request, "books.html", context)

def dump_users(request):
    User.objects.all().delete()
    return redirect("/books")

def logout(request):
    if request.session:
        for key in request.session.keys():
            del request.session[key]
    return redirect("/")
def review(request, review_id):
    book = Review.objects.filter(id = review_id)
    title = book[0].title
    review = book[0].review
    rating = book[0].rating

    context = {
        "title" : title,
        "review" : review,
        "rating" : rating,
        "id" : review_id
    }
    return render(request, "book_reviews.html", context)
def add_book(request, review_id):
    
    return render(request, "book_reviews.html", context)
def process(request):
    
# Create your views here.
