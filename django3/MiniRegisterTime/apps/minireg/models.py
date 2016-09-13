from __future__ import unicode_literals
from django.db import models
import re
from django.core.validators import validate_email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

from django.core.exceptions import ValidationError
  # our validator
def validateLengthGreaterThanTwo(value):
    if len(value)< 3:
      raise ValidationError(
          '{} must be longer than: 2'.format(value)
      )
def validate_Email(value):
    if not EMAIL_REGEX.match(value):
        raise ValidationError(
            '{} invalid email'.format(value)
        )

class User(models.Model):
    first_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
    last_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
    email = models.EmailField(validators = [validate_Email])
