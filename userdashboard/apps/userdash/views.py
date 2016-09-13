from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'userdash/index.html')

def signin(request):
    #go from sign in to account register link
    return render(request,'userdash/signin.html')

def register(request):
    #from sign in go to register page and also link to already have account
    if request.method == 'POST':
        user = User.objects.register(request.POST) #user = a tuple, 2 options, (True, user) or (False, errors)
        if user[0]:
            request.session['user_id']= user[1].id
            request.session['first_name']=user[1].first_name
            return redirect('dashregister')
        #build flash messages here using user[1]
        for error in user[1]: #always going to be referring as user 1 because it's the first user in the list
            messages.error(request, error)
        return redirect('dashregister')
    return render(request,'userdash/register.html')
