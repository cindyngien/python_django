from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .forms import RegisterForm

def index(request):
    form = RegisterForm()
    context = { "regForm": form }
    return render(request, "minireg/index.html", context)

def register(request):
    myform = RegisterForm()
    if request.method == "POST":
        bound_form = RegisterForm(request.POST)
        if bound_form.is_valid():
            return render(request, "minireg/success.html")
    else:
        bound_form = RegisterForm()
        print bound_form.errors

    return redirect(reverse('index'))
