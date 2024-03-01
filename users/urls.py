from django.contrib import admin
from django.urls import path , include
from users.views import LogoutView , UpdateUserName ,UsersViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',UsersViewSet)

urlpatterns = [
    path('users', include('django.contrib.auth.urls')),
    path('logout/' , LogoutView.as_view(), name="logout"),
    path('update_username/<int:pk>/', UpdateUserName.as_view(), name='update_username'),
    path('api/',include(router.urls))
]
urlpatterns+=router.urls
