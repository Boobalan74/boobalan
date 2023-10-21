from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . models import UserPersonalModel, ImageModel



class UserRegisterationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserPersonalForm(forms.ModelForm):
    
    class Meta:
        model = UserPersonalModel
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ('name','email','message', 'image', 'pdf_file')



