#! -*- coding: utf-8 -*-

from app.dbs import db


class Kpi(db.Model):
    __table__ = "kpi"
    __create__ = """
    create table kpi (
        name varchar(255) not null, 
        value int unsigned not null, 
        UNIQUE KEY kpi (name)
    );"""

    __columns__ = ['name', 'value']

    # name  = Required(str)
    # value = Required(int, unsigned=True)


class Results(db.Model):
    __table__ = 'results'
    __create__ = """
    create table results (
        id int(10) unsigned NOT NULL AUTO_INCREMENT, 
        ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP, 
        name varchar(255) not null, 
        value int unsigned not null, PRIMARY KEY (`id`)
    );"""

    __columns__ = ['name', 'value']

    # ts = Required(datetime, sql_default='CURRENT_TIMESTAMP')
    # name  = Required(str)
    # value = Required(int, unsigned=True)
