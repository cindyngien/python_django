from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Add_User
from ..loginapp.models import User
from ..courses_app.models import Course
from django.db.models import Count

def index(request):
    context = {
        'courses':Course.objects.all()
	}
    return render(request, 'courses_app/index.html', context)
    #had to make changes to the urls.py, views.py, and index.html where it displays the FORM post.

def login(request):
    context = {
        'users': User.objects.all()
    }
    return render(request,'loginapp/index.html', context)
    #returns login app's index.html where the logic occurs with the registration/login

def new_user(request):
    context = {
		'courses': Course.objects.all().annotate(user_count = Count("courses")),
		'users': User.objects.all()
	}
    return render(request, 'integrate/index.html', context)
    #.annotate/count is each COURSE with a COUNT of USERS as "courseusers" attribute
def add_new(request):
    user = User.objects.get(id=request.POST['userid'])
    course = Course.objects.get(id=request.POST['courseid'])
    #getting user_id & course_id from here
    Add_User.objects.create(course_id=course.id, user_id=user.id)
    #adding users to a course
    return redirect('/add_user')
    #redirects to the URL that add's users (in your urls.py) --
