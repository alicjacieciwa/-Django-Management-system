from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class RegisterForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']
#
#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)
#         self.fields['username'] = forms.CharField(
#             widget=forms.TextInput(attrs={
#                 'placeholder': 'Nazwa użytkownika'
#             }),
#             error_messages={
#                 'required': 'Wpisz nazwę użytkownika',
#             })
#         self.fields['password1'] = forms.CharField(
#             widget=forms.PasswordInput(attrs={
#                 'placeholder': 'Hasło'
#             }),
#             error_messages={
#                 'required': 'Podaj hasło',
#             })
#         self.fields['password2'] = forms.CharField(
#             widget=forms.PasswordInput(attrs={
#                 'placeholder': 'Powtórz hasło'
#             }),
#             error_messages={
#                 'required': 'Podaj hasło',
#             })
#
#         for field in ['username', 'password1', 'password2']:
#             self.fields[field].help_text = None
#             self.fields[field].label = ''
#










