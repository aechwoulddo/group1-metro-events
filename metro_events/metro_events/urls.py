"""metro_events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# Date Started: March 20, 2021
# Author/s: Wylen Joan Lee

# References:
#    https://www.youtube.com/watch?v=dBctY3-Z5hY&ab_channel=PrettyPrinted

from django.contrib import admin
from django.urls import path, include
app_name = 'metro_events'
urlpatterns = [
    # For Django Admin
    path('admin/', admin.site.urls, name='admin'),
    path('homepage/', views.HomepageView.as_view(), name="homepage_view"),
    path('userdashboard/', views.UserDashboardView.as_view(), name='user_dashboard'),
    path('organizerdashboard/', views.OrganizerDashboardView.as_view(), name='organizer_dashboard'),
    path('administratordashboard/', views.AdministratorDashboardView.as_view(), name='administrator_dashboard')
    path('', include('app.urls'), name='dashboard'),
]
