from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from django.conf import settings
from users.forms import UserRegisterForm, UserForm
import random

# Create your views here.


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Подтверждение регистрации',
            message='Вы зарегистрировались на нашей платформе',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )

        return super().form_valid(form)


class UserUpdate(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm
    template_name = 'users/profile.html'

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_pass = ''.join([str(random.randint(0, 9)) for _ in range(5)])
    send_mail(
        subject='Новый пароль',
        message=f'Новый пароль {new_pass}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_pass)

    request.user.save()
    return redirect(reverse('users:login'))


