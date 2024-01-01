from django.contrib import admin
from django.urls import path , include
from users.views import LogoutView

urlpatterns = [
    path('users', include('django.contrib.auth.urls')),
    path('logout/' , LogoutView.as_view(), name="logout")
]
