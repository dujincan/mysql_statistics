#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 3:01 下午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : main.py
# @Software: PyCharm

from mysqlFunction import MysqlFunc

host_ip = ''
username = ''
password = ''
dbname = ''
tbname = ''

# connection = MysqlFunc(host_ip, username, password)
# all_db = connection.get_all_database()
# print(all_db)

# connection = MysqlFunc(host_ip, username, password)
# all_tables_of_db = connection.get_all_tables_of_specified_db(dbname)
# print(all_tables_of_db)

# connection = MysqlFunc(host_ip, username, password)
# all_tables_of_all_db = connection.get_all_tables_of_all_db()
# print(all_tables_of_all_db)

# connection = MysqlFunc(host_ip, username, password)
# number_row = connection.get_number_row(dbname, tbname)
# print(number_row)

# connection = MysqlFunc(host_ip, username, password)
# number_row_of_db = connection.get_number_row_of_db(dbname)
# print(number_row_of_db)

# connection = MysqlFunc(host_ip, username, password)
# number_row_of_all_db = connection.get_number_row_of_all_db()
# print(number_row_of_all_db)

# connection = MysqlFunc(host_ip, username, password)
# column = connection.get_column_and_type(dbname, tbname)
# print(column)

# connection = MysqlFunc(host_ip, username, password)
# column_of_db = connection.get_column_and_type_of_db(dbname)
# print(column_of_db)

connection = MysqlFunc(host_ip, username, password)
column_of_all_db = connection.get_column_and_type_of_all_db()
print(column_of_all_db)