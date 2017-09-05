from .models import Cab, Driver
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.core.validators import validate_email


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/admin")

        return render(request, 'companies/signup.html')
    return render(request, 'companies/login.html')


def signup_view(request):
    if request.method == 'POST':
        errors = []
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        val = True
        try:
            email = request.POST['email']
            validate_email(email)
        except Exception as e:
            errors.append(e.message)
            val = False
            print e

        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if val:
            if password == password_confirm:
                user = User()
                user.first_name = firstname
                user.last_name = lastname
                user.email = email
                user.username = username
                user.set_password(password)
                user.save()

                return redirect('login')

        return render(request, 'companies/signup.html', {'errors': errors})

    return render(request, 'companies/signup.html')
