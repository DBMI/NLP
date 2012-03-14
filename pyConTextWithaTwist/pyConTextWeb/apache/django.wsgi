import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'pyConTextWeb.settings'
sys.path.append("/usr/local/src/django")
sys.path.append("/usr/local/src/django/pyConTextWeb")
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
