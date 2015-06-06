# -*- coding: utf-8
from django import forms
from models import CustomUser
from django.forms import TextInput
from collections import OrderedDict


class EmailForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': u'E-mail'}), required=True)


class LoginForm(EmailForm):
    error_messages = {
            'invalid_data': "Введен неправильный пароль или e-mail",
        }
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': u'Пароль'}), required=True)


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Имя'}))
    last_name = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Фамилия'}))
    middle_name = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Отчество'}))
    city = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Город'}))
    email = forms.EmailField(widget=TextInput(attrs={'placeholder': u'E-mail'}))
    phone = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Телефон'}))


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Имя'}), required=True)
    last_name = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Фамилия'}), required=True)
    middle_name = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Отчество'}), required=True)
    city = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Город'}), required=True)
    email = forms.EmailField(widget=TextInput(attrs={'placeholder': u'E-mail'}), required=True)
    phone = forms.CharField(max_length=20, widget=TextInput(attrs={'placeholder': u'Телефон'}), required=True)

    class Meta:
        model = CustomUser



    def username(self):
        return self.cleaned_data['email']

    def save(self, commit=True):
        user = CustomUser.objects.create_user(first_name=self.cleaned_data['first_name'],
                                              last_name=self.cleaned_data['last_name'],
                                              middle_name=self.cleaned_data['middle_name'],
                                              city=self.cleaned_data['city'],
                                              email=self.cleaned_data['email'],
                                              phone=self.cleaned_data['phone'],
                                              username=self.username())
        if commit:
            user.is_active = False
            user.save()
        return user


class SetPasswordForm(forms.Form):
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="New password",
                                widget=forms.PasswordInput(attrs={'placeholder': u'Пароль'}),
                                required=True)
    password2 = forms.CharField(label="New password confirmation",
                                widget=forms.PasswordInput(attrs={'placeholder': u'Подтвердите пароль'}),
                                required=True)

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2


class PasswordChangeForm(forms.Form):

    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
        'password_incorrect': "Your old password was entered incorrectly. "
                                "Please enter it again.",
    }
    old_password = forms.CharField(widget=forms.PasswordInput,
                                   required=False)
    new_password1 = forms.CharField(widget=forms.PasswordInput,
                                    required=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput,
                                    required=False)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

    def clean_new_password(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    first_name = forms.CharField(max_length=20, widget=TextInput(), required=False)
    last_name = forms.CharField(max_length=20, widget=TextInput(), required=False)
    middle_name = forms.CharField(max_length=20, widget=TextInput(), required=False)
    city = forms.CharField(max_length=20, widget=TextInput(), required=False)
    email = forms.EmailField(widget=TextInput(), required=False)
    phone = forms.CharField(max_length=20, widget=TextInput(), required=False)
    file = forms.ImageField(required=False)

    def clean_old_password(self):
        if self.cleaned_data["old_password"]:
            old_password = self.cleaned_data["old_password"]
            if not self.user.check_password(old_password):
                raise forms.ValidationError(
                    self.error_messages['password_incorrect'],
                    code='password_incorrect',
                )
            return old_password

    def save(self, commit=True):
        cd = self.cleaned_data
        user = self.user
        files = self.files
        if cd['first_name']:
            user.first_name = cd['first_name']
        if cd['last_name']:
            user.last_name = cd['last_name']
        if cd['middle_name']:
            user.middle_name = cd['middle_name']
        if cd['city']:
            user.city = cd['city']
        if cd['email']:
            user.email = cd['email']
        if cd['phone']:
            user.phone = cd['phone']
        if files:
            user.image = self.files['file']
        if self.clean_old_password():
            if cd['new_password1'] and cd['new_password2']:
                user.set_password(self.clean_new_password())
        if commit:
            user.save()
        return user


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()
