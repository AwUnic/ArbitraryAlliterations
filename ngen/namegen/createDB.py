#!/bin/python
import sqlite3 as lite
import sys
import os
import string
import re

def main(path,dbpath):
    #open the sqlite database with the appropiate scheme
    con = lite.connect(dbpath)
    words = open(path).readlines()

    match = re.search(r'type:\s*(?P<listtype>.+)\s*;.*\s*category:\s*(?P<category>.+)\s*;',words[0])

    if match is None:
        #the list file is expected to start with a line containing type and category
        #format is "type:[type_name]; ... category:[category_name];"
        print('broken file header')
        exit(1)
    #get category and type from list header
    listtype,category = match.groups()

    with con:
        cur = con.cursor()
        #check if type exists and get its id
        cur.execute("select id from types where name=?",(listtype,))
        type_id = cur.fetchone();
        #if not create it
        if type_id is None:
            print('creating type',listtype)
            cur.execute('insert into types(name) values(?)',(listtype,))
            cur.execute('select id from types where name=?',(listtype,))
            type_id = cur.fetchone()
        type_id = type_id[0]

        #check if category exists
        cur.execute("select id from categories where name=? and type_id=?",(category,type_id))
        cat_id = cur.fetchone()
        if cat_id is None:
            print('creating category',category)
            cur.execute('insert into categories(name,type_id) values (?,?)',(category,type_id))
            cur.execute('select id from categories where name=? and type_id=?',(category, type_id))
            cat_id = cur.fetchone()
        cat_id = cat_id[0]

        #insert words into table with appropiate type/category
        print('adding words of type',listtype,'to category',category)
        for word in words[1:]:
            if(word[0]!='#'):
                cur.execute('insert into words(word,cat_id,type_id) values(?,?,?)',(word.strip(),cat_id,type_id))


if __name__ == '__main__':
    if(len(sys.argv)==3):
        main(sys.argv[1],sys.argv[2])

    else:
        print('usage: createDB.py wordfile dbfile')
        exit(1)
    exit(0)
