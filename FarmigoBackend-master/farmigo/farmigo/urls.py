"""farmigo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', users_views.home, name='hom'),
    path('admin/', admin.site.urls, name='admin'),
    path('home/', users_views.test, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('register/', users_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', users_views.profile, name='profile'),
    path('profile/edit/', users_views.edit_profile, name='edit_profile'),
    path('retailer/', users_views.farmer_retailer, name='retailer'),
    path('supplier/', users_views.farmer_supplier, name='supplier'),
    path('weather/', users_views.weather, name='weather'),
    path('livemandi/', users_views.mandi, name='mandi'),
    path('soil_testing/', users_views.soil_testing, name='soil'),
    path('blogs/1/', users_views.blog1, name='blog1'),
    path('blogs/2/', users_views.blog2, name='blog2'),
    path('users/', include('users.urls')),
]
