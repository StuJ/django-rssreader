from __future__ import unicode_literals

from django.db import models

class Favourite(models.Model):
    title = models.CharField(max_length= 200)
    description = models.CharField(max_length= 2000)
    link = models.URLField()
    pubDate = models.DateTimeField()
    
    def __str__(self):
        return self.title

