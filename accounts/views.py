from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordChangeView
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.views import View


class CustomLogin(LoginView):
    form_class = UserLoginForm
    template_name = "accounts/login.html"
    extra_context = {'title': 'Login'}


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change_form.html'


class Registration(View):
    template_name = 'accounts/registration.html'

    def get(self, request):
        context = {
            'form': UserRegistrationForm()
        }
        return render(request, self.template_name, context)

    def post(self,request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
