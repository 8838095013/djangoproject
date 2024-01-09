from django.urls import path
from . views import register,login,dashboard

urlpatterns = [
    path('register/',register, name='register'),
    path('login/',login, name='login'),
    path('success/',dashboard, name='success'),
]