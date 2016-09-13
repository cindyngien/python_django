from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
#Our new manager!
class UserManager(models.Manager):
    def register(self, email):
        if not EMAIL_REGEX.match(email):
            return(False, "Invalid Email!")
        else:
            return(True, email)

class User(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
    objects = models.Manager()
