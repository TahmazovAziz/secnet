from django import forms
from users.models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username',]
    
