from rest_framework import serializers
from user_profile.models import User_profile

class User_profile_serializers(serializers.ModelSerializer):
    avatar = serializers.ImageField()
    class Meta:
        model = User_profile
        fields = ['avatar']
