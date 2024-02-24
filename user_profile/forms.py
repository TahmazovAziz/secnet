from django import forms
from user_profile.models import User_profile

class User_profileForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ('avatar',)