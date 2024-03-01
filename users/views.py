from django.shortcuts import render , redirect
from django.views import View
from django.views.generic.edit import UpdateView
from users.models import Users
from django.contrib.auth import logout
from users.forms import UsersForm
from users.serializers import UsersSerializers
from rest_framework import viewsets

class LogoutView(View):
    template_name = 'registration/logout.html'
    
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        if request.method == 'POST':
            logout(request)
            return redirect('/')
class UpdateUserName(UpdateView):
    model = Users
    template_name = 'change_name.html'
    form_class = UsersForm

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializers