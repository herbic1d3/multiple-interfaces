#! -*- coding: utf-8 -*-

from app.interfaces.filedata import file_interface
from app.interfaces.database import database_interface
from app.interfaces.snmp import snmp_interface

"""
    file
"""
def file_refresh_data():
    return file_interface.refresh_values()

def file_read_data(*args, **kwargs):
    return file_interface.read_from_file(*args, **kwargs)

"""
    database
"""
def db_refresh_kpi():
    return database_interface.refresh_kpi_value()

def db_arrange_values():
    return database_interface.arrange()

def db_read_results():
    return database_interface.read_from_database()


"""
    snmp
"""
def snmp_get_data():
    return snmp_interface.get_results()
