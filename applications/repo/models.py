from datetime import datetime
import django.utils.timezone 
from django.db import models
from applications.user.models import User
# Create your models here.
class Archive(models.Model):
    title = models.CharField(max_length=255)
    archive = models.FileField(upload_to='archive',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    createAt = models.DateTimeField('Fecha De Creacion',default=django.utils.timezone.now)
    likes = models.ManyToManyField(User, related_name='archive_liked', blank=True)
    def __str__(self):
        return self.title
    # Otros campos como descripción, me gusta, etc.
class Comment(models.Model):
    archive= models.ForeignKey(Archive, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    createAt = models.DateTimeField('Fecha De Creacion',default=django.utils.timezone.now)
    def __str__(self):
        return self.archive.title