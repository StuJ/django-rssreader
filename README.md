# django-rssreader
Work in progress. A Django web app that enables users to read, search and favourite articles from an RSS feed.

Quick start
-----------

1. Add "reader_app" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'reader_app',
    ]

2. Include the reader_app URLconf in your project urls.py like this::

    url(r'^', include('reader_app.urls')),

3. Run `python manage.py migrate` to create models.

4. Start the development server and visit http://127.0.0.1:8000
