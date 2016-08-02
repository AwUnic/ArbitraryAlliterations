#!/usr/bin/env python
import sqlite3 as lite
import sys
import string
from namegen import namegen
from cgi import parse_qs, escape

def  application(env, start_response):
	parameters = parse_qs(env.get('QUERY_STRING', ''))
	start_response('200 OK', [('Content-Type', 'text/html')])
	categories = parameters['types[]']
	try:
		brkC = categories.index(':catbrk:')
		brkL = categories.index(':letbrk:')
	except:
		return ['Invalid Input'.encode('utf8')]
	catN = categories[:brkC]
	catA = categories[brkC+1:brkL]
	letters = categories[brkL+1:]
	resp = '<p>'+namegen.gen(catA,catN,letters)+'</p>\n'
	return [resp.encode('utf8')]
