
# -*- coding: utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import hashlib, random
from accounts.models import CustomUser, Need, Thank
from clw.settings import SITE_DOMAIN_URL as site_url
from django.contrib.auth.forms import AdminPasswordChangeForm


class CustomUserChangeForm(UserChangeForm):

    password = ReadOnlyPasswordHashField(label=_("Password"))

    def clean_password(self):
        return self.initial["password"]

    class Meta:
        model = CustomUser
        fields = "__all__"


def accept(CustomUserAdmin, request, queryset):
    for obj in queryset:
        plaintext = get_template('email/accept_email.txt')
        htmly = get_template('email/accept_email.html')
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        obj.activation_key = hashlib.sha1(salt+obj.email).hexdigest()
        obj.save()
        d = Context({'user': obj, 'site_url': site_url})
        
        subject, from_email, to = 'Подтверждение аккаунта', 'cwitnesses@gmail.com', obj.email
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
accept.short_description = "Отправить письмо с подтверждением"


def make_published(NeedAdmin, request, queryset):
    queryset.update(active=True)


def make_active(ThankAdmin, request, queryset):
    queryset.update(active=True)


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    change_user_password_template = None
    list_display = ('username', 'date_joined',
                    'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'email', 'first_name', 'last_name', 'middle_name', 'city', 'phone', 'image'
            )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    change_password_form = AdminPasswordChangeForm
    actions = [accept]


class NeedAdmin(admin.ModelAdmin):
    list_display = ('author', 'active', )
    actions = [make_published]

    class Meta:
        model = Need
admin.site.register(Need, NeedAdmin)


class ThankAdmin(admin.ModelAdmin):
    list_display = ('author', 'active', )
    actions = [make_active]

    class Meta:
        model = Thank
admin.site.register(Thank, ThankAdmin)







admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)




