#! -*- coding: utf-8 -*-

import importlib

from . import settings
import pymysql

__database__ = pymysql.connect(
    host=settings.mysql['DBHOST'], 
    user=settings.mysql['DBUSERNAME'], 
    password=settings.mysql['DBPASSWORD'], 
    db=settings.mysql['DBNAME']
)

sql_echo = True

class BaseModel(object):
    __table__   = ""
    __create__  = ""
    __columns__ = []

    def db_session(fun):
        def tmp(self, *args, **kwargs):
            self.cursor = __database__.cursor()
            result = fun(self, *args, **kwargs)
            __database__.commit()
            self.cursor.close()

            return result
        return tmp

    @classmethod
    @db_session
    def create_table(self):
        if '__create__'  in self.__dict__.keys():
            result = self.cursor.execute("select table_name from information_schema.tables where table_schema = database() and table_name = '{0}';".\
                format(self.__table__))
            if result == 0:
                self.cursor.execute(self.__dict__['__create__'])

    @classmethod
    @db_session
    def insert(self,**kwargs):
        cols = ''
        vals = ''
        for key in kwargs.keys():
            if key in self.__columns__:
                cols = '{0} `{1}`,'.format(cols, key)
                if type(kwargs[key]) == str:
                    vals = "{0} '{1}',".format(vals, kwargs[key])
                else:
                    vals = "{0} {1},".format(vals, kwargs[key])
        sql = "INSERT INTO {0} ({1}) VALUES ({2});".format(
                self.__table__, cols[:-1], vals[:-1])
        self.cursor.execute(sql)

    @classmethod
    @db_session
    def clear(self):
        result = self.cursor.execute("delete from {0}".format(self.__table__))

    @classmethod
    @db_session
    def select_all(self):
        result = []
        cols = ''
        for key in self.__columns__:
            cols = '{0} `{1}`,'.format(cols, key)
        sql = "select {0} from `{1}`;".format(cols[:-1],self.__table__)
        self.cursor.execute(sql)
        for vals in self.cursor:
            result.append(list(vals))
        return result


class dbClass(object):
    """
        PyMySQL configuration
    """
    def __init__(self):
        self.db = __database__
        self.cursor = self.db.cursor()
        self.Model = BaseModel

    def create_all(self):
        for item in settings.DATABASE_MODELS:
            mod = importlib.import_module(item[:item.rfind('.')])
            cls = getattr(mod,item[item.rfind('.')+1:])
            cls.create_table()

    def drop_all(self):
        for item in settings.DATABASE_MODELS:
            mod = importlib.import_module(item[:item.rfind('.')])
            cls = getattr(mod,item[item.rfind('.')+1:])
            result = self.cursor.execute("select table_name from information_schema.tables where table_schema = database() and table_name = '{0}';".\
                format(cls.__table__))
            if result == 0:
                continue
            self.cursor.execute('drop table {0};'.format(cls.__table__))

db = dbClass()


