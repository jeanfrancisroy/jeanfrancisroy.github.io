#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jean-Francis Roy'
SITENAME = 'Jean-Francis Roy'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Static home
# DISPLAY_PAGES_ON_MENU = False
# DISPLAY_CATEGORIES_ON_MENU = False
# MENUITEMS = [('Home', '/')]
PAGE_ORDER_BY = 'order'

THEME = '/home/jf/dev/git/pelican/pelican-themes/gum'
PLUGIN_PATHS = ['/home/jf/dev/git/pelican']
PLUGINS = ['render_math', 'pelican-bibtex']

PUBLICATIONS_SRC = 'content/jf.bib'
# DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'publications']

STATIC_PATHS = ['extra/CNAME', 'pdfs']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
