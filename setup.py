import os

from setuptools import setup, find_packages

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = 'django-issues',
	version = '0.1',
	url = 'http://github.com/myles/django-issuees',
	license = 'BSD License',
	description = 'A Django issue application.',
	long_description = read('README'),
	
	author = 'Myles Braithwaite',
	author_email = 'me@mylesbraithwaite.com',
	
	packages = find_packages('src'),
	package_dir = {'': 'src'},
	
	install_requires = [
		'setuptools',
	],
	
	classifiers = [
		'Development Status :: 4 - Beta',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Topic :: Internet :: WWW/HTTP',
	],
)
