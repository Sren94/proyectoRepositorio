
import django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager
# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField('Usuario', max_length=50,unique=True )
    firstName = models.CharField('Nombre(s)',max_length=60,blank=True)
    lastName = models.CharField('Apellido(s)',max_length=60,blank=True)
    email = models.EmailField(unique=True)
    
    #password = models.CharField('Contraseña',max_length=100,default='asas')
    photo=models.ImageField('Fotografia', upload_to=f'user/{username}/', blank=True)
    createAt = models.DateTimeField('Fecha De Creacion',default=django.utils.timezone.now)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD='username'  
    objects= UserManager()
    REQUIRED_FIELDS=['email',]
    def get_full_name(self):
        return self.firstName+' '+self.lastName
    def get_email(self):
        return self.email
    def __str__(self):
        return self.firstName+" "+self.lastName
    