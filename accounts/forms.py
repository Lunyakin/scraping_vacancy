from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label='email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Введите вашу почту',
            "autocomplete": "email"
        }
        )
    )
    error_messages = {
        "invalid_login": "Пожалуйста введите корректный %(username)s и пароль."
                         "Учтите что оба поля могут быть чувствительны к регистру ",
        "inactive": "Этот аккаунт не активен",
    }


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Введите вашу почту',
            "autocomplete": "email"
        })
    )
    # password1 = forms.CharField(
    #     label='password1',
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplete": "current-password",
    #         'placeholder': 'Введите ваш пароль',
    #     })
    # )
    # password2 = forms.CharField(
    #     label='password2',
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={
    #         "autocomplete": "current-password",
    #         'placeholder': 'Введите ваш пароль еще раз',
    #     }),
    # )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email',)

    # def clean_password(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #     if password1 != password2:
    #         raise ValidationError('Пароли не совпадают.')
    #     return password2
