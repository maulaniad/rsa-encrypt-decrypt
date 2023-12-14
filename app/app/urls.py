"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from app.views import SessionCorrector, Login, Register, Logout, Dashboard, NotFound


urlpatterns = [
    path("", SessionCorrector.as_view(), name="session_corrector"),
    path("admin/", admin.site.urls),

    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("logout/", Logout.as_view(), name="logout"),

    path("dashboard/", Dashboard.as_view(), name="dashboard"),
    path("decryption/", include("decryption.urls")),
    path("encryption/", include("encryption.urls")),

    path("<path:unknown_path>", NotFound.as_view(), name="catch_all")
]
