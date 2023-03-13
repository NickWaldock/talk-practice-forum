from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)