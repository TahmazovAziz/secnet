from django.urls import path
from . import views

urlpatterns = [
    path('' , views.profile_view, name='profile'),
    path('create/', views.create_avatar,name='create_avatar'),
    path('update_avatar/<int:pk>/', views.User_profileUpdate.as_view(),name='update_avatar')
]
