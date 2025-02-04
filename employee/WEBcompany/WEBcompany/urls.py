"""
URL configuration for WEBcompany project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('events/',views.create_events,name='create_events'),
    path('all_events/',views.all_events,name='all_events'),
    path('all_employee/',views.all_employee,name='all_employee'),
    path('employee_detail/<int:employee_id>',views.employee_detail,name='employee_detail'),







]
