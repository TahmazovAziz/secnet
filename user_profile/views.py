from django.shortcuts import render ,redirect
from user_profile.models import User_profile
from user_profile.forms import User_profileForm
from django.views.generic.edit import UpdateView
from post.models import Post
from users.models import Users

def profile_view(request):
    user_avatar = User_profile.objects.all()
    user_post = Post.objects.filter(userid=request.user)
    user_name = Users.objects.filter(username=request.user)
    context = {
        "user_avatar":user_avatar,
        "user_post":user_post,
        "user_name":user_name
    }
    return render(request,'profile.html',context)

def create_avatar(request):

    if request.method == 'POST':
        form = User_profileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = User_profileForm()
        return render(request , 'change_avatar.html',{'form':form})

class User_profileUpdate(UpdateView):
    model = User_profile
    template_name = 'change_avatar.html'
    form_class = User_profileForm

