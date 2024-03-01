from django.urls import path , include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'profile', views.User_profileVewSet)
urlpatterns = [
    path('' , views.profile_view, name='profile'),
    path('create/', views.create_avatar,name='create_avatar'),
    path('update_avatar/<int:pk>/', views.User_profileUpdate.as_view(),name='update_avatar'),
    path('api/' , include(router.urls))
]
urlpatterns+=router.urls