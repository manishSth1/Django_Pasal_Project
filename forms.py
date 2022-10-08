#from django.forms import Form, ModelForm   #Form -> field name write by urself, ModelForm-> In any Model, already datatypes are defined, look and create
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model    # use -> main user authentication model make by yourself, from settings.py
from django.core.validators import RegexValidator

User = get_user_model()

class SignupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'username',
            'name': 'username',
            'class': 'form-control'
        }
    ), required=True,)

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'John',
            'class': 'form-control'
        }
    ), required=True,)

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Doe',
            'class': 'form-control'
        }
    ), required=True,)

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder': 'john@example.com',
            'class': 'form-control'
        }
    ), required=True,)

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'The password must contain at least 8 alphanumeric characters',
            'class': 'form-control'
        } ), 
        required=True,
        validators=[RegexValidator(r'^[a-zA-Z0-9]{8,60}$', message='The password must contain at least 8 alphanumeric characters'),]
        
        )




    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    
    def save(self, **kwargs):
        user =  super().save(**kwargs)
        user.set_password(user.password)
        user.save()
        return user


