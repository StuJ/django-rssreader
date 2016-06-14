from django.shortcuts import render

import feedparser

from .models import Favourite


def index(request):
    #Parse RSS feed from given URL and render view using index.html template
    feed = feedparser.parse('https://www.reddit.com/r/django/.rss')
    return render(request, 'reader_app/index.html', {'feed': feed})

def favourites_list(request):
    #Display list of favourite articles
    favourites = Favourite.objects.all
    return render(request, 'reader_app/favourites_list.html', {'favourites': favourites})



