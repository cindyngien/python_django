from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'survey_form/index.html')

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/results')
    else:
        return redirect('/')

def clear(request):
    if request.method == "POST":
        return redirect('/')

def results(request):
    return render(request, 'survey_form/results.html')
