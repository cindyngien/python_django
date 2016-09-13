from django.shortcuts import render, HttpResponse, redirect
import random
import time

def index(request):
    if "total" not in request.session:
        request.session["total"] = 0
    if "log" not in request.session:
        request.session["log"] = ""
    return render(request, 'ninja_gold/index.html')

def processmoney(request):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            farmNum = random.randint(10,20)
            request.session['total'] += farmNum
            request.session['log'] = "\n you've earned " + str(farmNum) + " from the farm " + time.strftime('%a, %d %b %Y %H:%M:%S') + request.session['log']
        elif request.POST['building'] == 'cave':
            caveNum = random.randint(5,10)
            request.session['total'] += caveNum
            request.session['log'] = "\n you've earned " + str(caveNum) + " from the cave " + time.strftime('%a, %d %b %Y %H:%M:%S') + request.session['log']
        elif request.POST['building'] == 'house':
            houseNum = random.randint(2,5)
            request.session['total'] += houseNum
            request.session['log'] = "\n you've earned " + str(houseNum) + " from the house " + time.strftime('%a, %d %b %Y %H:%M:%S') + request.session['log']
        elif request.POST['building'] == 'casino':
            casinoNum = random.randint(-50,50)
            request.session['total'] += casinoNum
            if casinoNum < 0:
                request.session['log'] = "\n you've lost " + str(casinoNum) + " ouch! better luck next time " + time.strftime('%a, %d %b %Y %H:%M:%S') + request.session['log']
            else:
                request.session['log'] = "\n you've earned " + str(casinoNum) + " from the casino " + time.strftime('%a, %d %b %Y %H:%M:%S') + request.session['log']
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
