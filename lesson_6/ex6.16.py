#!/usr/bin/env python

lod = [
	{
		'name': 'Apex Pharma',
		'city': 'Louisville',
		'state': 'KY',
	},
	{
		'name': 'Beta IT',
		'city': 'New York',
		'state': 'NY',
	},
	{
		'name': 'Gamma Husbandry',
		'city': 'Lancaster',
		'state': 'PA',
	},
	]

for mydict in lod:
	print mydict['name']
	print mydict['city'], mydict['state']
	print