from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', views.PostsViewSet)

urlpatterns = [
    path('' , views.upload_post, name='create_post'),
    path('api/', include(router.urls))
]

urlpatterns += router.urls
