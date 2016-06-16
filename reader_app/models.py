from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=500)
    url = models.URLField()
    date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.title

class Favourite(models.Model):
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

