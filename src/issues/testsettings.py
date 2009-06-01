DEBUG = True
DEBUG_TEMPLATE = True
SITE_ID = 1
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/django-issues-devel.db'
INSTALLED_APPS = [
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admin',
	'django.contrib.comments',
	'django.contrib.admindocs',
	'django.contrib.comments',
	'issues',
]
ROOT_URLCONF = 'issues.testurls'