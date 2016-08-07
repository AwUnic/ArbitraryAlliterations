#!/bin/python
import sqlite3 as lite
import sys
import os
import string
import re

def main(path):
    con = lite.connect('namegen.db')
    words = open(path).readlines()

    match = re.search(r'type:\s*(?P<listtype>.+)\s*;.*\s*category:\s*(?P<category>.+)\s*;',words[0])

    if match is None:
        #the list file is expected to start with a line containing type and category
        #format is "type:[...]; ... category:[...];"
        print('broken file header')
        exit(1)

    print(match.groups())
    listtype,category = match.groups()

    with con:
        cur = con.cursor()
        print(listtype)
        #check if type exists and get its id
        cur.execute("select id from types where name=?",(listtype,))
        type_id = cur.fetchone();
        #if not create it
        if type_id is None:
            cur.execute('insert into types(name) values(?)',(listtype,))
            cur.execute('select id from types where name=?',(listtype,))
            type_id = cur.fetchone()
        print(type_id)
        type_id = type_id[0]
        #check if category exists
        cur.execute("select id from categories where name=? and type_id=?",(category,type_id))
        cat_id = cur.fetchone()
        if cat_id is None:
            cur.execute('insert into categories(name,type_id) values (?,?)',(category,type_id))
            cur.execute('select id from categories where name=? and type_id=?',(category, type_id))
            cat_id = cur.fetchone()
        cat_id = cat_id[0]
        #insert words into table with appropiate type/category
        for word in words[1:]:
            if(word[0]!='#'):
                cur.execute('insert into words(word,cat_id,type_id) values(?,?,?)',(word.strip(),cat_id,type_id))


if __name__ == '__main__':
    if(len(sys.argv)==2):
        main(sys.argv[1])

    else:
        print('invalid syntax: wordfile')
        exit(1)
    exit(0)
