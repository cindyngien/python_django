from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'disappearing_ninjas/index.html')

def ninjascolor(request, color):
    turtles = {
        'blue': ["leonardo.jpg"],
        'purple': ["donatello.jpg"],
        'orange': ["michelangelo.jpg"],
        'red': ["raphael.jpg"],
        '': ["leonardo.jpg", "donatello.jpg", "michelangelo.jpg", "raphael.jpg"]
    }
    if color in turtles:
        context = {'color': turtles[color]} #variable to reference the turtle colors
    else:
        context = {'color': ["notapril.jpg"]} #string because this is not a variable

    return render(request, 'disappearing_ninjas/one_ninja.html', context)
