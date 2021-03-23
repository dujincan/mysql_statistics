#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 8:49 上午
# @Author  : Du Jincan
# @Email   : jincan.du@gmail.com
# @File    : mysqlFunction.py
# @Software: PyCharm

import pymysql.cursors


class MysqlFunc:
    """
    统计mysql信息的类
    """

    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd

    def getConnect(self):
        """
        获取数据库连接
        """
        connection = pymysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.passwd,
                                     charset='utf8')
        return connection

    def get_all_database(self):
        """
        获得所有的库名
        :return 列表
        """
        connection = self.getConnect()
        databases = []

        with connection:
            sql = "show databases;"
            with connection.cursor() as cursor:
                cursor.execute(sql)
                # 获得指定mysql server的所有库
                results = cursor.fetchall()
                # print(results)
                for result in results:
                    database = result[0]
                    if database not in ('information_schema', 'mysql', 'performance_schema', 'sys'):
                        databases.append(database)
        return databases

    def get_all_tables_of_specified_db(self,dbname):
        """
        获取指定库的所有表
        :return: 列表
        """
        connection = self.getConnect()
        tables = []
        with connection:
            with connection.cursor() as cursor:
                # 获取指定库的所有表
                sql = "select table_name from information_schema.tables where TABLE_SCHEMA = %s"
                cursor.execute(sql, (dbname,))
                results = cursor.fetchall()
                for result in results:
                    tables.append(result[0])
        return tables

    def get_all_tables_of_all_db(self):
        """
        获取所有库的所有表
        :return: 返回字典
        """
        databases = self.get_all_database()
        tb_dict = {}

        for database in databases:
            # 获取指定库的所有表
            tables = self.get_all_tables_of_specified_db(database)
            tb_dict[database] = tables

        return tb_dict

    def get_column_and_type(self, dbname, tbname):
        """
        获取指定库指定表的字段和字段类型
        :param dbname: 指定库
        :param tbname: 指定表
        :return: 字典
        """
        connection = self.getConnect()

        with connection:
            # 获取指定库中指定表的字段和字段类型，返回字典
            with connection.cursor() as cursor:
                columns_dict = {}
                sql = "select column_name, data_type from information_schema.`COLUMNS` where TABLE_SCHEMA = %s " \
                      "and TABLE_NAME = %s "
                cursor.execute(sql, (dbname, tbname))
                # 获得字段和字段类型
                columns = cursor.fetchall()
                for column in columns:
                    # 将字段作为key，字段类型作为value，加入字典中
                    columns_dict[column[0]] = column[1]

        return columns_dict

    def get_column_and_type_of_db(self, dbname):
        """
        获得指定库中所有表所有字段和字段类型
        :param dbname: 指定库
        :return: 字典
        """
        db_column_dict = {}
        tables = self.get_all_tables_of_specified_db(dbname)
        for table in tables:
            # 获取指定库中指定表的字段和字段类型
            column_dict = self.get_column_and_type(dbname, table)
            db_column_dict[table] = column_dict

        return db_column_dict

    def get_column_and_type_of_all_db(self):
        """
        获得指定server中所有库中表的字段和字段类型
        :return: 字典
        """
        all_db_column_dict = {}

        databases = self.get_all_database()
        for database in databases:
            # 获取指定库中所有表的字段和字段类型
            db_column_dict = self.get_column_and_type_of_db(database)
            all_db_column_dict[database] = db_column_dict

        return all_db_column_dict

    def get_number_row(self, dbname, tbname):
        """
        统计指定库指定表的行数
        :return: 行数
        """
        connection = self.getConnect()

        with connection:
            connection.select_db(dbname)
            # 获取指定库指定表的行数
            with connection.cursor() as cursor:
                sql = 'SELECT COUNT(1) from `%s`;' % tbname
                cursor.execute(sql)
                result = cursor.fetchall()
                number = result[0][0]
                
        return number

    def get_number_row_of_db(self, dbname):
        """
        统计指定库中所有表的行数
        :return: 字典
        """

        tables = self.get_all_tables_of_specified_db(dbname)
        numbers = {}
        for table in tables:
            # 获取指定库指定表的行数
            number = self.get_number_row(dbname, table)
            numbers[table] = number

        return numbers

    def get_number_row_of_all_db(self):
        """
        统计所有库中所有表的行数
        :return: 字典
        """

        databases = self.get_all_database()
        all_db_numbers = {}
        for database in databases:
            # 获取指定库中所有表的行数的字典
            numbers = self.get_number_row_of_db(database)
            all_db_numbers[database] = numbers

        return all_db_numbers


