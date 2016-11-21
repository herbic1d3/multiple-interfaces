#! -*- coding: utf-8 -*-

import os
import datetime


debug = True

session_lifetime = datetime.timedelta(minutes=30)

# root path for project
project_path = os.path.abspath(os.path.dirname(__file__))

# папка для хранения статических файлов
static_path = os.path.join(project_path, 'static')
favicon_path = os.path.join(static_path, 'favicon.ico')

site_url = '127.0.0.1:8888'

# url для статики
static_url = '/static/'

datetime_format = "%d.%m.%Y %H:%M:%S"
date_format = "%d.%m.%Y"

template_path = os.path.join(project_path, "templates"),

"""
    MySQL 
"""
mysql = {
    'DBNAME': 'multiple-interfaces',
    'DBUSERNAME': '',
    'DBPASSWORD': '',
    'DBHOST': '127.0.0.1'
}

DATABASE_MODELS = [
    'app.interfaces.database.models.Kpi',
    'app.interfaces.database.models.Results',
]

"""
    Additional settings for interfaces
"""

POLL_TIMEOUT = 1000 * 60 * 5 # 5 минут

DATA_FILE =  os.path.join(project_path, 'demo/datafile.txt') # файл с данным для задания 2.


"""
    Demo settings for counters
"""

COUNTERS = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG']
COUNTERS_LEN = len(COUNTERS)-1


"""
    SNMP
"""
SNMP_SESSION = {
    'host': '127.0.0.1',
    'community': 'public',
    'version': 2
}

SNMP_RESOURCES = [
    {'OID': '.1.3.6.1.2.1.25.1.6.0', 'MIB': 'hrSystemProcesses.0'},
    {'OID': '.1.3.6.1.2.1.25.1.3.0', 'MIB': 'hrSystemInitialLoadDevice.0'},
    # {'OID': '.1.3.6.1.4.1.2021.11.10.0', 'MIB': 'private.enterprises.ucdavis.systemStats.ssCpuSystem'},
    # {'OID': '.1.3.6.1.4.1.2021.11.9.0', 'MIB': 'private.enterprises.ucdavis.systemStats.ssCpuUser'},
]


"""
    Developers settings
"""
try:
    from local_settings import *
except ImportError:
    pass

