from django.shortcuts import render, redirect, HttpResponse
import random
import string

def index(request):
    return render(request, 'random_word_gen/index.html')

def show(request):
    if request.method == "POST":
        if "counter" not in request.session:
            request.session['counter'] = 0
        N = 14
        request.session['randword'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))
        request.session['counter'] += 1
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    if request.method == "POST":
        request.session['counter'] = 0
        return redirect('/')
