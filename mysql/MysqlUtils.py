import os
import sys
import json
import mysql.connector


class MysqlClass:
    def getMysqlClient( usr, pwd, url):
        client = mysql.connector.connect(user=usr, password=pwd, host=url)
        return client

class StudentService:

    def __init__(self, user, pwd, host):
        self.user = user
        self.pwd = pwd
        self.host = host

    def createPythonDb(self, databaseName):

        client = MysqlClass.getMysqlClient(self.user, self.pwd, self.host)
        cursor = client.cursor()
        cursor.execute("create database if not exists {} default charset 'utf8'".format(databaseName))


    def createStudentTable(self, databasename, tablesql):
        client = MysqlClass.getMysqlClient(self.user, self.pwd, self.host)
        cursor = client.cursor()
        cursor.execute("use {}".format(databasename))
        cursor.execute(tablesql)



if __name__ == '__main__':
    user = 'root'
    pwd = 'root'
    host = 'localhost'
    studentservice = StudentService(user, pwd, host)

    """创建DB"""
    databasename = 'python'
    studentservice.createPythonDb(databasename)

    """创建table"""
    tablesql = 'create table if not exists student(id int auto_increment primary key, name varchar(32), age int) engine=InnoDB default charset=utf8'
    studentservice.createStudentTable(databasename, tablesql)


