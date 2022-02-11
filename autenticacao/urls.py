import django.urls
from django.urls.conf import path
from . import views

urlpatterns = [
    path('registro/', views.cadastrar, name='user.registro'),
    path('login/', views.logar, name='user.login'),
    path('logout/', views.logout, name='user.logout'),
]