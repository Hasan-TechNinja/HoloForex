from django.urls import path
from . import views

urlpatterns = [
    path('singUp/', views.RegistrationView, name='singup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
]
