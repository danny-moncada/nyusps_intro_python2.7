#!/usr/bin/env python

sites_pages = {
	'example.com':	[
					    'index.html',
					    'about_us.html',
					    'contact_us.html'
					    ],
	'something.com': [
						'index2.html',
						'prize.html',
						'puppies.html',
						],
	'whateva.com':	[
						'main.html',
						'getting.html',
						'setting.html',
						],
}

for pages in sites_pages['whateva.com']:
	print pages