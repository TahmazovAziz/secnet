from django.shortcuts import render
from post.models import Post

def data_view(request):
    post_data = Post.objects.all().select_related()
    return render(request, 'main/home.html', {"post_data":post_data})