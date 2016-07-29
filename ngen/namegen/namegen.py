#!/bin/python
import sqlite3 as lite
import sys, random
import string
import re
def gen(catAlist, catNlist, letter):
    con = lite.connect('namegen/namegen.db')

    cmdnoun="select noun from nouns join categories on category=id where name in ("+ '?,'*(len(catNlist)-1) +"?)  and char=?"
    cmdadj="select adjective from adjectives join adjcategories on category=id where name in ("+ '?,'*(len(catAlist)-1) +"?) and char=?"

    with con:
        cur = con.cursor()
        cur.execute(cmdnoun,(tuple(catNlist+[letter])))
        rowsN = cur.fetchall()
        cur.execute(cmdadj,(tuple(catAlist+[letter])))
        rowsA = cur.fetchall()
        if len(rowsN) and len(rowsA):
            return random.choice(rowsA)[0]+"<br>"+random.choice(rowsN)[0]
        else:
            return "Impossible<br>Input"
