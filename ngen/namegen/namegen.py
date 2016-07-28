#!/bin/python
import sqlite3 as lite
import sys, random
import string

def gen(categoryA, catNlist, letter):
    con = lite.connect('namegen/namegen.db')
    #sanitize sql command parameters
    #letter = letter[:1]
    
    categoryN = "'%s'" % "','".join(s.lower() for s in catNlist)
    print(categoryN,catNlist)
	 
   #categoryA = categoryA[:1]
    #if not (letter.isalpha() and categoryA.isnumeric() and categoryN.isnumeric()):
    #    return "Invalid Input"
    cmdnoun="select noun from nouns join categories on nouns.category=categories.id where name in ("+categoryN+") and char='"+letter+"'"
      #cmdadj="select adjective from adjectives join categories on adjectives.category=categories.id  where name='feelings' and char='"+letter+"'"
    cmdadj="select adjective from adjectives where category=0 and char='"+letter+"'"
    print(cmdnoun,cmdadj)
    with con:
        cur = con.cursor()
        cur.execute(cmdnoun)
        rowsN = cur.fetchall()
        cur.execute(cmdadj)
        rowsA = cur.fetchall()
	print(rowsA,rowsN)
        if len(rowsN):
            return random.choice(rowsA)[0]+"<br>"+random.choice(rowsN)[0]
        else:
            return "Invalid<br>Input"

