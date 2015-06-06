from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import Task, Consultant


class TaskAdmin(admin.ModelAdmin):
    description = forms.CharField(widget=CKEditorWidget())
    list_display = ('title', 'verbose_title', 'video', 'date')
    class Meta:
        model = Task

admin.site.register(Task, TaskAdmin)


class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'active')

    class Meta:
        model = Consultant

admin.site.register(Consultant, ConsultantAdmin)
