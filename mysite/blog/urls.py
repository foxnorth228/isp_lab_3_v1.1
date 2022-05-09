from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.mainPage, name='main_page'),

    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]