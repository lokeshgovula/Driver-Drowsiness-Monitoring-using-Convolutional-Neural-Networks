"""FatigueDetection URL Configuration

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
from django.urls import path,include
from DriverDrowsiness import views as mainView
from users import views as usr
from admins import views as admins

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mainView.index, name='index'),
    path("index/", mainView.index, name="index"),
    path("logout/", mainView.logout, name="logout"),
    path("AutoistLogin/", mainView.AutoistLogin, name="AutoistLogin"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path("AutoistRegister/", mainView.AutoistRegister, name="AutoistRegister"),


    ## User side
    path("DriverRegisterActions/", usr.DriverRegisterActions, name='DriverRegisterActions'),
    path("AutoistLoginCheck/", usr.AutoistLoginCheck, name="AutoistLoginCheck"),
    path("AutoistHome/", usr.AutoistHome, name="AutoistHome"),
    path("DetectFatigueDriver/", usr.DetectFatigueDriver, name="DetectFatigueDriver"),
    path("StartTraining/", usr.StartTraining, name="StartTraining"),
    path("Autoisthistory/", usr.Autoisthistory, name="Autoisthistory"),

    ##Admin Side
    path('AdminLoginCheck/', admins.AdminLoginCheck, name='AdminLoginCheck'),
    path('AdminHome/', admins.AdminHome, name='AdminHome'),
    path('ViewRegisteredAutoists/', admins.ViewRegisteredAutoists, name='ViewRegisteredAutoists'),
    path('AdminActivaAutoists/', admins.AdminActivaAutoists, name='AdminActivaAutoists'),
    path('AdminDeleteAutoists/', admins.AdminDeleteAutoists, name='AdminDeleteAutoists'),
    path('AdminViewFatigueHistory/', admins.AdminViewFatigueHistory, name='AdminViewFatigueHistory'),

]
