"""
    mySQL - pymysql DATABASE MODEL 1/26/2018
"""

import pymysql


class MySQL_CRUD:
    def __init__(self, host, user, pw):
        self.db = self.connect_to_mysql(host, user, pw)
        self.cur = self.create_cursor()

    def connect_to_mysql(self, host, user, pw):
        db = pymysql.connect(host, user, pw)
        print('connected to mySQL')
        return db

    def drop_db_table(self, name):
        self.cur.execute('DROP TABLE {}'.format(name))
        print('{} table deleted'.format(name))

    def drop_db(self, name):
        self.cur.execute("DROP DATABASE {}".format(name))
        print('{} database deleted'.format(name))

    def commit_db(self):
        self.db.commit()

    def create_cursor(self):
        cur = self.db.cursor()
        return cur

    def create_db(self, name):
        try:
            (self.db.select_db(name))
            print('{} database already exists'.format(name))
        except:
            self.cur.execute('CREATE DATABASE {}'.format(name))
            print('{} database created'.format(name))

    def create_db_table(self, name, tup):
        sql = "CREATE TABLE {} ({})".format(name, (tup))

        try:
            self.cur.execute(sql)
        except pymysql.err.InternalError as ie:
            print(ie)

    # TODO:: need a method to return the column names
    # TODO:: need a method to return tables in db
    # returns number of columns
    def tb_columns(self, tb):
        sql = 'SHOW FIELDS FROM {}'.format(tb)
        return self.cur.execute(sql)

    def insert_into_db(self, tup, name):
        sql = "INSERT INTO {} VALUES {}".format(name, tup)
        try:
            self.cur.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def show_db_table(self, name, k):
        sql = ("SELECT * FROM {} ORDER BY {}".format(name, k))
        self.cur.execute(sql)

        for row in self.cur.fetchall():
            print(row)

    def delete_table_row(self, name, k, v):
        sql = "DELETE FROM {} WHERE {} = {}".format(name, k, v)
        print('{} by col {} deleted from {}'.format(v, k, name))

        self.cur.execute(sql)
        self.db.commit()

    def get_tables_in_db(self):
        self.cur.execute("SHOW TABLES")

        for k in self.cur.fetchall():
            print(k)
