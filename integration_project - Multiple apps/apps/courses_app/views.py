from django.shortcuts import render, redirect, HttpResponse
from .models import Course

def index(request):
    context = {
        'courses':Course.objects.all()
	}
    return render(request, 'courses_app/index.html', context)

def create(request):
    new_course = Course()
    new_course.course_name = request.POST["name"]
    new_course.course_description = request.POST["description"]
    new_course.save()
    return redirect('/')

def destroy(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request,'courses_app/destroy.html', context)

def delete(request):
    course = Course.objects.get(id=request.POST['course_id'])
    course.delete()
    return redirect('/')
