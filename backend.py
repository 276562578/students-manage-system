#!/usr/bin/python
#coding:utf-8

import sqlite3

def newdb(filename):
    """this should create a new database in 'filename',
    with a empty table 'students' with two columns 'id' and 'name'."""
    conn=sqlite3.connect(filename)
    c=conn.cursor()
    c.execute("""CREATE TABLE students (id text, name text)""")
    conn.commit()
    conn.close()

def read(filename,key,val):
    """this should read 'val' of 'key' from db in 'filename'"""
    conn=sqlite3.connect(filename)
    c=conn.cursor()
    c.execute("""SELECT * FROM students WHERE id=?""", (key,))
    res=c.fetchmany()
    conn.close()
    return res
    
def write(filename,key,val):
    """this should update 'val' of 'key' from db in 'filename'"""
    conn=sqlite3.connect(filename)
    c=conn.cursor()
    c.execute("""INSERT INTO students (id, name) VALUES(?,?) ON DUPLICATE KEY UPDATE id=VALUES(id),name=VALUES(name)""",(key,val))
    conn.commit()
    conn.close()

def delete(filename,key):
    """this should delete 'key' from db in 'filename'"""
    conn=sqlite3.connect(filename)
    c=conn.cursor()
    c.execute("""DELETE FROM students WHERE id=?""", (key,))
    conn.commit()
    conn.close()
#__int__():
#       conn-sqlite3.connect()
#       c=conn.cursor()
#is that ok?
#TODO: alter table structure
#TODO: specify column to read and write
#TODO: maybe use a key-value store!!!
