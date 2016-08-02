#!/usr/bin/env python
import sqlite3 as lite
import sys, random
import string
from namegen import namegen
from cgi import parse_qs, escape

def  application(env, start_response):
	parameters = parse_qs(env.get('QUERY_STRING', ''))
	start_response('200 OK', [('Content-Type', 'text/html')])
	categories = parameters['types[]']
	try:
		brkC = categories.index(':catbrk:')
		brkL = len(categories)+1
	except:
		return ['Invalid Input'.encode('utf8')] 
	letter = random.choice(string.ascii_uppercase)
	catA = categories[brkC+1:]
	catN = categories[:brkC]
	resp = '<p>'+namegen.gen(catA,catN,letter)+'</p>\n'
	return [resp.encode('utf8')]
