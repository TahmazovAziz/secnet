from django.db import models
from users.models import Users
class User_profile(models.Model):
    avatar = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True , null=True)
    def get_absolute_url(self):
        return f"/profile/"
    