#!/bin/python
import sqlite3 as lite
import sys, random
import string
import re

DB_PATH = 'namegen/namegen.db'
def gen(catAlist, catNlist, letter):
    con = lite.connect(DB_PATH)

    #query to get the ids of the requested categories
    getcat = "select id from categories where name in ("+"?,"*(len(catAlist)+len(catNlist)-1)+"?)"

    #query to select the pairs of words that match the requested criteria
    selectfromA ="select a.word,n.word from words a, words n where a.type_id=2 and n.type_id=1 and a.cat_id in ("
    selectfromB =") and n.cat_id in("
    selectfromC =") and substr(a.word,1,1) = substr(n.word,1,1) and substr(n.word,1,1) in("+"?,"*(len(letter)-1)+"?)"

    with con:
        cur = con.cursor()
        #get all category ids and put them in a comma separated string
        cur.execute(getcat,catAlist+catNlist)
        cat_ids = cur.fetchall()
        cat_ids = [item for sublist in cat_ids for item in sublist]
        cat_idstr = ','.join(map(str, cat_ids))

        #get all pairs
        cur.execute(selectfromA+cat_idstr+selectfromB+cat_idstr+selectfromC ,letter)
        words = cur.fetchall()

        if len(words):
            #print one of the pairs at random and put a <br>-tag between them
            return "<br>".join(random.choice(words))
        else:
            #if there was no combination of words that satisfied the criteria
            return "Impossible<br>Input"
