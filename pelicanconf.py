#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals
import os

AUTHOR = u'Kristen M. Thyng'
SITENAME = u'Kristen M. Thyng, Ph.D.'
SITEURL = ''

DEFAULT_LANG = u'en'

# Times and dates
DEFAULT_DATE_FORMAT = "%b %d, %Y"
TIMEZONE = 'US/Central'

# Article URL generation
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
MENUITEMS = [('Archives', '/archives.html'),
             ('Home', 'http://www.kristenthyng.com'),
             ('Research', 'http://www.kristenthyng.com/research.html')]
NEWEST_FIRST_ARCHIVES = False

#Github include settings
GITHUB_USER = 'kthyng'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Theme
THEME = "./theme"
CSS_FILE = "styles.css"

# Plugins
PLUGIN_PATHS = [os.path.join(os.environ.get('HOME'), 'src', 'pelican-plugins')]
PLUGINS = []

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Sharing
TWITTER_USER = 'thyngkm'
GOOGLE_PLUS_USER = 'kthyng'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = False
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'


# RSS/Atom feeds
# FEED_DOMAIN = SITEURL
# FEED_ATOM = 'atom.xml'

# Search
SEARCH_BOX = True

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Tag cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
