from django.urls import path

from users.apps import UsersConfig

from users.views import LoginView, LogoutView, RegisterView, UserUpdate, generate_new_password, CodeView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdate.as_view(), name='profile'),
    path('profile/genpassword', generate_new_password, name='generate_new_password'),
    path('code/', CodeView.as_view(), name='code'),
]