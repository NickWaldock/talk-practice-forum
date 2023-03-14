from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id))) 
        # # Sends user to single post view of post created
        return reverse('home') # Sends the user back home after publishing post