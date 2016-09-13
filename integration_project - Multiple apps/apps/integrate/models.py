from __future__ import unicode_literals
from decimal import Decimal
from django.db import models
from ..loginapp.models import User
from ..courses_app.models import Course

#by doing this, you are going up a folder, and looking into the loginapp and courses app and importing the class here so you can use it as a FK
# Create your models here.

class Add_User(models.Model):
    user = models.ForeignKey(User, related_name="users")
    course = models.ForeignKey(Course, related_name="courses")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
