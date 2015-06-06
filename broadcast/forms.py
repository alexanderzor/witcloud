# -*- coding: utf-8
from django import forms
from django.forms import TextInput
from collections import OrderedDict
from models import Task

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Название на английском(без пробелов)'}), required=True)
    file = forms.FileField(required=True)
    description = forms.CharField(max_length=400, widget=forms.Textarea(attrs={'placeholder': u'Описание к видео'}))
    verbose_title = forms.CharField(max_length=40, widget=TextInput(attrs={'placeholder': u'Название на кирилице'}), required=True)
    image = forms.ImageField(required=False)
    def save(self, commit=True):
        cd = self.cleaned_data

        task = Task.objects.create(title=cd['title'],
                                   video=cd['file'],
                                   description=cd['description'],
                                   verbose_title=cd['verbose_title'],
                                   image=cd['image'])
        if commit:
            task.save()
        return task



CHOICES = (('ask', 'Вопрос по урокам'),
           ('need', 'Нужда'),
           ('thanks', 'Благодарность'),
           ('witness', 'Свидетельство'))

class FeedBackForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    subject = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=True)
