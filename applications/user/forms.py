from django import forms
from django.contrib.auth import authenticate
from .models import User

class userRegisterForm(forms.ModelForm):
    password=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'contraseña',
                'class':'form-control'
            }
        )
    )
    password2=forms.CharField(
        label='Repetir Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña contraseña',
                'class':'form-control'
            }
        )
    )
    username=forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingresa tu username',
                'class':'form-control'
            }
        )
    )
    email=forms.EmailField(
        label='email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Ingresa tu email',
                'class':'form-control'
            }
        )
    )
    firstName=forms.CharField(
        label='Nombre(s)',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingresa tu nombre',
                'class':'form-control'
            }
        )
    )
    lastName=forms.CharField(
        label='Apellido(s)',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Ingresa tu nombre',
                'class':'form-control'
            }
        )
    )
    
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'firstName',
            'lastName',
            
        )
    def clean_password2(self):
        if self.cleaned_data['password']!=self.cleaned_data['password2']:
            self.add_error('password2','Las Contraseñas No Coinciden')
class LoginForm(forms.Form):
    userName=forms.CharField(
        label='Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Por ejemplo juan123',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'contraseña',
                'class':'form-control'
            }
        )
    )
    def clean(self):
        cleaned_data=super(LoginForm,self).clean()
        username=self.cleaned_data['userName']
        password=self.cleaned_data['password']
        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Usuario o Contraseña no coinciden')
        return self.cleaned_data

class UpdateUserForm(forms.ModelForm):
    email=forms.EmailField(
        label='Email', 
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Ingresa Tu Correo',
                'class':'form-control'
            }
        )
        )
    photo=forms.ImageField(
        label='Fotografia',
        required=False,
        
    )
    class Meta:
        model = User
        fields = ('email','photo')

    

    