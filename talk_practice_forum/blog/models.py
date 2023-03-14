from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

# The main model for all posts
class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    body = models.TextField()
    category = models.CharField(max_length=250, default='no-tag')
    post_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title + ' | ' + str(self.author)
    

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id))) 
        # # Sends user to single post view of post created
        return reverse('home') # Sends the user back home after publishing post
    

# A model for utilising tags/categories on posts
class Category(models.Model):
    name = models.CharField(max_length=250)


    def __str__(self):
        return self.name 
    

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id))) 
        # # Sends user to single post view of post created
        return reverse('home') # Sends the user back home after publishing post