from django.db import models

# Create your models here.

# Article
class Article (models.Model):
    # Title of the Article
    title = models.CharField(max_length=200)
    # Abstraction
    abstraction = models.TextField(null=True, max_length=2000)
    # Text of html
    text = models.TextField(null=True)
    # Writer
    writer = models.CharField(max_length=200)
    # When the article was added
    createdTime = models.DateTimeField(auto_now_add=True)
    # Last modified time of the article
    lastModifiedTime = models.DateTimeField(auto_now =True)
    # Number of views
    views = models.IntegerField(default=0)

# Songs
class Song (models.Model):
    # Title of the song
    title = models.CharField(max_length=200)
    #singer
    singer = models.CharField(null=True, max_length=200)
    # Path of the file
    file = models.FileField()
    # Remark
    remark = models.TextField(null=True, max_length=2000)
    # When the song was added
    createdTime = models.DateTimeField(auto_now_add=True)
    # Number of views
    views = models.IntegerField(default=0)


