# -*- coding: utf-8
from forms import RegistrationForm
from django.shortcuts import render
from models import CustomUser
from django.shortcuts import get_object_or_404
import hashlib, random
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from forms import LoginForm, EmailForm, SetPasswordForm, PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.http import Http404
from clw.settings import SITE_DOMAIN_URL as site_url
import time


def success_register(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
    else:
        login_form = LoginForm()
    context = {'login_form': login_form}

    return render(request, 'success_register.html', context)
def success_reset(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
    else:
        login_form = LoginForm()
    context = {'login_form': login_form}

    return render(request, 'success_reset.html', context)



def invalid_data(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
    else:
        login_form = LoginForm()
    context = {'login_form': login_form}

    return render(request, 'invalid_data.html', context)



def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            email = cd['email']
            password = cd['password']
            u = CustomUser.objects.filter(email=email).first()
            user = authenticate(username=u.username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('settings_view'))
                else:
                    HttpResponseRedirect(reverse('invalid_data'))
            else:
                HttpResponseRedirect(reverse('invalid_data'))
    else:
        login_form = LoginForm()
    HttpResponseRedirect(reverse('invalid_data'))
    


def login_2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            email = cd['email']
            password = cd['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
    else:
        login_form = LoginForm()
    return HttpResponseRedirect(reverse('invalid_data'))


@login_required(login_url='register_view')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('register_view'))


def password_view(request, activation_key):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(request.POST)
        if form.is_valid():
            user = CustomUser.objects.get(activation_key=activation_key)
            user.set_password(form.clean_password())
            user.is_active = True
            user.save()
            
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SetPasswordForm()
    context = {'form': form, 'user': user}
    return render(request, "password.html", context)


def register_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            user.activation_key = hashlib.sha1(salt+user.email).hexdigest()
            #user.key_expires = timezone.now() + timezone.timedelta(100)
            user.save()
            plaintext = get_template('email/register_email.txt')
            htmly = get_template('email/register_email.html')
            d = Context({'username': user.username})

            subject, from_email, to = 'Account has been created', 'cwitnesses@gmail.com', user.email
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect(reverse('success_register'))

    else:
        register_form = RegistrationForm()
        login_form = LoginForm()
    context = {'register_form': register_form, 'login_form': login_form}
    return render(request, "register.html", context)


def forgot_password(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        login_form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = get_object_or_404(CustomUser, email=email)
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            user.activation_key = hashlib.sha1(salt+user.email).hexdigest()
            #user.key_expires = timezone.now() + timezone.timedelta(100)
            user.save()
            plaintext = get_template('email/password_reset.txt')
            htmly = get_template('email/password_reset.html')
            d = Context({'user': user, 'site_url': site_url})


            subject, from_email, to = 'Восстановление пароля', 'cwitnesses@gmail.com', user.email
            text_content = plaintext.render(d)
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect(reverse('success_reset'))
    else:
        form = EmailForm()
        login_form = LoginForm()
    context = {'form': form, 'login_form': login_form}
    return render(request, "forgot_password.html", context)


@login_required(login_url='register_view')
def settings_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST, files=request.FILES)
        #imgform = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('settings_view'))
        else:
            pass
    else:
        form = PasswordChangeForm(user=request.user)
        #imgform = UploadFileForm()
    context = {'form': form, }
    return render(request, "profile.html", context)

