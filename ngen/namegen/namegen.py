#!/bin/python
import sqlite3 as lite
import sys, random
import string
import re
def gen(catAlist, catNlist, letter):
    con = lite.connect('namegen/namegen.db')
    getcat = "select id from categories where name in ("+"?,"*(len(catAlist)+len(catNlist)-1)+"?)"
    selectfromA ="select a.word,n.word from words a, words n where a.type_id=2 and n.type_id=1 and a.cat_id in ("
    selectfromB =") and n.cat_id in("
    selectfromC =") and substr(a.word,1,1) = substr(n.word,1,1) and substr(n.word,1,1)=?"
    with con:
        cur = con.cursor()
    #    print(getcat,catAlist,catNlist)
        cur.execute(getcat,catAlist+catNlist)
        cat_ids = cur.fetchall()
        cat_ids = [item for sublist in cat_ids for item in sublist]
        cat_idstr = ','.join(map(str, cat_ids))
    #    print(cat_ids)
    #    print(selectfromA+cat_idstr+selectfromB+cat_idstr+selectfromC )
        cur.execute(selectfromA+cat_idstr+selectfromB+cat_idstr+selectfromC ,[letter])
        words = cur.fetchall()
    #    print(words)
        if len(words):
            return "<br>".join(random.choice(words))
        else:
            return "Impossible<br>Input"
