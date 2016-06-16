from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

import feedparser

from reader_app import models


def index(request):
    #Parse RSS feed from given URL and render view using index.html template
    feed = feedparser.parse('https://www.reddit.com/r/django/.rss')

    for article in feed.entries:
	# if the article exists, it will be put in the "article" variable and created will be false.
	# if the article doesn't exist, it will be created and added as "article" and the created var will be true
	article, created = models.Article.objects.get_or_create(
			url=article.link,
			defaults={'description': article.summary, 'title': article.title}
		)

	articles = models.Article.objects.all()

    return render(request, 'reader_app/index.html', {'articles': articles})

@login_required
def add_favourite(request, article_id):
	article = get_object_or_404(models.Article, pk=article_id)

	fave, created = models.Favourite.objects.get_or_create(user=request.user, article=article)

	if created:
		print 'This object was created'
	else:
		print 'This object already exists'

	return redirect(reverse('favourites'))

def favourites_list(request):
    #Display list of favourite articles
    favourites = Favourite.objects.all()
    return render(request, 'reader_app/favourites_list.html', {'favourites': favourites})



