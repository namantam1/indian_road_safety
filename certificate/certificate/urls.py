"""certificate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth.views import TemplateView,PasswordResetView,LoginView,LogoutView
from certificate_app.views import signup,useractivation

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('registration.backends.default.urls')),
    path('',TemplateView.as_view(template_name='certificate_app/index.html'),name='home'),
    path('signup',signup,name='signup'),
    path('activate/<uibd64>/<token>',useractivation,name='activate'),
    path('login',LoginView.as_view(template_name='certificate_app/usercreation.html'),name='login'),
    path('logout',LogoutView.as_view(),name='logout')
]
