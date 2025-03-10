from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/', null=True, blank=True)
    def __str__(self):
        return self.title