from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth import logout

class LogoutView(View):
    template_name = 'registration/logout.html'
    
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        if request.method == 'POST':
            logout(request)
            return redirect('/')
