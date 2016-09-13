from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'email_validations/index.html')

def add_user(request):
    my_user = User.userManager.register(request.POST['email'])
    if my_user[0]:
        messages.add_message(request, messages.SUCCESS, "The email address you entered is a VALID email address!", my_user[1], "is a VALID email address! Thank you!")
        User.objects.create(email = my_user[1])
        return redirect('/success')
    if my_user[0] == False:
        messages.add_message(request, messages.INFO, "Invalid Email Address!")
        return redirect('/')

def success(request):
    email_val = User.objects.all()
    print User.objects.all()
    context = {
        'email_vals': email_val
    }
    print email_val
    return render(request, 'email_validations/success.html', context)
