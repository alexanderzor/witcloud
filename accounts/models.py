from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.utils import timezone
import datetime
from clw import settings


class CustomUser(User):
    middle_name = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    activation_key = models.CharField(max_length=40, blank=True)
    #key_expires = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to='images/', blank=True)
    objects = UserManager()

    def has_voted(self, need):
        if not Votes.objects.filter(need_id=need).first():
            return False
        else:
            return True

    def vote(self, need):
        if not self.has_voted(need):
            v = Votes.objects.create(user_id=self, need_id=need)
            v.save()



def create_custom_user(sender, instance, created, **kwargs):
    if created:
        values = {}
        for field in sender._meta.local_fields:
            values[field.attname] = getattr(instance, field.attname)
        user = CustomUser(**values)
        user.save()

post_save.connect(create_custom_user, User)


class Thank(models.Model):
    author = models.ForeignKey(CustomUser, related_name='my_thanks', null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']


class Need(models.Model):
    author = models.ForeignKey(CustomUser, related_name='my_needs', null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    voters = models.ManyToManyField(CustomUser, through='Votes', through_fields=('need_id', 'user_id'))
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']


class Votes(models.Model):
    user_id = models.ForeignKey(CustomUser)
    need_id = models.ForeignKey(Need)

