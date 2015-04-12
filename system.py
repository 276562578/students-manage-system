#!/usr/bin/python
#coding:utf-8
import sqlite3
import xlrd
import time
#程序大体是先输出功能列表，然后按照序号选择功能
#数据库中提取的数据以excel表格的形式输出
#后期加上各种计算功能

#首先是欢迎界面啦
def welcome():
    i=2 #密码验证
    while i<=2:
        passwd=raw_input("请输入密码：")
        if passwd=='passwd':
            break
        elif passwd=='':
            print "密码不可为空"
        elif i==0:
            exit()
        else:
            i=i-1
            print "密码错误，请重新输入！"+'\n'+"剩余输入次数："+str(i)
    print ''
    print "============================================="
    print "============================================="
    print "欢迎使用学生管理系统"
    print ''
    print "License:GNU GENERAL PUBLIC LICENSE"
    print "         Version 3, 29 June 2007"+'\n\n'
    print "============================================="
    print "============================================="
welcome()


#列出功能列表吧
print "功能列表："+'\n'
print "1.查询学生信息"
print "2.提取学生信息"
print "3.修改学生信息"+'\n'
while 1:   #判断输入    
    i=raw_input("请输入操作序号:")
    if i in ['1','2','3']:
        break
    elif i=='':
        print "参数不能为空"
        continue
    else:
        print '\n'+"===================="+'\n'+"参数错误，请重新输入"+'\n'+"===================="+'\n'
        continue




if i==1:
    searchdb()
elif i==2:
    getdb()
elif i==3:
    updatedb()


#查询信息的菜单(未完成)
def searchdb():
    print "================================"
    print "||姓名查找请直接回车||"
    print "||学号输入后两位即可||"
    while 1:
        id=raw_input('请输入学号：')
        if id=='':
            name()
            break
            #name=raw_input('请输入姓名：')
        elif len(id)>>8:
            print "学号输入有误，请重新输入！"
            continue
        elif 2<<len(id)<<8:
            print "学号输入有误，请重新输入！"
        else:
            print " "
#判断选择的功能
def name():
    print "ok"




#程序启动先连接数据库
db_student=sqlite3.connect("./student.db")

#先定义个功能选择的



