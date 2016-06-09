from django.shortcuts import render

import feedparser


def index(request):

    #Parse RSS feed from given URL and render view using index.html template

    feed = feedparser.parse('https://www.reddit.com/r/django/.rss')
    return render(request, 'reader_app/index.html', {'feed': feed})


