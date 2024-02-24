from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from chat.views import chatbox

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,include('main.urls')),
    path('users/' , include('users.urls') , name='users'),
    path('accounts/', include('allauth.urls')),
    path('post/', include('post.urls')),
    path('chat/<str:chat_box_name>' ,chatbox, name='chatbox'),
    path('profile/',include('user_profile.urls'),name='profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)