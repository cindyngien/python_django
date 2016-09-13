from django import forms

  # assumes that we have a model!
from .models import User
  # ****************************

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
