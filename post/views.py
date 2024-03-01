from rest_framework import viewsets
from post.serializers import PostSerializers
from django.shortcuts import render, redirect
from .forms import PostForm
from post.models import Post
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.userid = request.user  # Присваиваем текущего пользователя полю userid
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'post/upload_post.html', {"form":form})

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() 
    serializer_class = PostSerializers
    