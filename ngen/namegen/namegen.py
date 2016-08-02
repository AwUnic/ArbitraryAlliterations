#!/bin/python
import sqlite3 as lite
import sys, random
import string
import re
def gen(catAlist, catNlist, letters):
    con = lite.connect('namegen/namegen.db')

    cmdnoun="select noun from nouns join categories on category=id where name in ("+ '?,'*(len(catNlist)-1) +"?)  and char in(" + '?,'*(len(letters)-1)+"?)"
    cmdadj="select adjective from adjectives join adjcategories on category=id where name in ("+ '?,'*(len(catAlist)-1) +"?) and char in(" + '?,'*(len(letters)-1)+"?)"

    with con:
        cur = con.cursor()
        cmd = "select * from (("+cmdadj+") , ("+cmdnoun+")) where SUBSTR(noun,1,1)=SUBSTR(adjective,1,1)"
	cur.execute(cmd,(catAlist+letters+catNlist+letters))
        rows = cur.fetchall()
        if len(rows) :
		name = random.choice(rows)
        	return name[0]+"<br>"+name[1]
        else:
		return "Impossible<br>Input"
