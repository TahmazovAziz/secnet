from rest_framework import serializers
from post.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','text','image','userid']