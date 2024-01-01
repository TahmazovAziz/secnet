from django.db import models
from users.models import Users

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True , null=True)
    userid = models.ForeignKey(Users , on_delete=models.CASCADE)
    def __str__(self):
        return self.title