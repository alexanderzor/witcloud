from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Task(models.Model):
    title = models.CharField(max_length=20, unique=True)
    number = models.IntegerField(blank=True, null=True)
    video = models.FileField(upload_to='video/', blank=True)
    date = models.DateField(default=timezone.now())
    description = RichTextField(blank=True)
    verbose_title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='scc/images/', blank=True)
    private = models.BooleanField(default=False, blank=True)
    url = models.URLField(blank=True)



class Consultant(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=40)
    skype = models.CharField(max_length=40)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/consultants/')
    active = models.BooleanField(default=True)
