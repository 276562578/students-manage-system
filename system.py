#!/usr/bin/python
#coding:utf-8
import sqlite3
import xlrd
import time
import getpass
import backend
#程序大体是先输出功能列表，然后按照序号选择功能
#数据库中提取的数据以excel表格的形式输出
#后期加上各种计算功能

i=2 #密码验证
while i<=2:
    print "注意！输入密码时不会有任何显示......"
    passwd=getpass.getpass("请输入密码：")
    if passwd=='passwd':
        break
    elif passwd=='':
        print "密码不可为空"
    elif i==0:
        exit()
    else:
        i=i-1
        print "密码错误，请重新输入！"+'\n'+"剩余输入次数："+str(i)


#首先是欢迎界面啦
def welcome():
    print ''
    print "============================================="
    print "============================================="
    print "欢迎使用学生管理系统"
    print ''
    print "License:GNU GENERAL PUBLIC LICENSE"
    print "         Version 3, 29 June 2007"+'\n\n'
    print "============================================="
    print "============================================="
    db_student=sqlite3.connect("./student.db")
welcome()



#查询信息的菜单(未完成)
def searchdb():
    print '\n'+"================================"
    print "||姓名查找请直接回车||"
    print "||学号输入后两位即可||"+'\n'
    while 1:
        id=raw_input('请输入学号：')
        if id=='':
            name=raw_input('请输入姓名：')
            pass
        elif len(id)!=8 or len(id)!=2 :
            print "学号输入有误，请重新输入！"
        else:
            if len(id)==2:
                pass
            backend.read(student,)
            pass


#提取信息的菜单-未完成
def getdb():
    print '\n'+"================================"
    print ""
    print ""
    while 1:
        list=raw_input("请选择想要输出的项目(以,分隔)：").split(",")
        if len(list)<=1:
            print "请输入至少两个项目！(是否以半角符号\",\"为分割符？)"
        elif:
            pass


#修改信息的菜单-未完成
def updatedb():
    print '\n'+"================================"
    print "1.新增一个项目"
    print "2.新增一位学生"
    print "3.修改一个项目"
    print "4.修改一位学生"
    print "5.删除一个项目"
    print "6.删除一位学生"


#列出功能列表吧
def mainmenu():
    print "功能列表："+'\n'
    print "1.查询学生信息"
    print "2.提取学生信息"
    print "3.修改学生信息"+'\n'
    while 1:   #判断输入    
        i=raw_input("请输入操作序号:")
        if i=='1':
            searchdb()
        if i=='2':
            getdb()
        if i=='3':
            updatedb()
        elif i==''
            print "参数不能为空"
        else:
            print '\n'+"===================="+'\n'+"参数错误，请重新输入"+'\n'+"===================="+'\n'




