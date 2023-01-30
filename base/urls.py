from django.urls import path
from . import views


urlpatterns = [
        path('login/', views.loginUser, name="login"),
        path('logout/', views.logoutUser, name="logout"),
        path('register/', views.registerUser, name="register"),

        path('', views.home, name="home"),
        path('campaign/', views.campaign, name="campaign"),
        path('wallet/', views.wallet, name="wallet"),
        path('settings/', views.settings, name="settings"),
        
        path('files/', views.files, name="files"),
        path('texts/', views.texts, name="texts"),
        path('videos/', views.videos, name="videos"),
        path('success/', views.success, name="success"),
]