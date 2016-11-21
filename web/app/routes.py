#! -*- coding: utf-8 -*-

import tornado.web

from app import settings
from handlers import IndexHandler, FileReadHandler, DatabaseReadHandler, SNMPReadHandler

routes = [
    (r'/(favicon.ico)', tornado.web.StaticFileHandler, {'path': settings.favicon_path}),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': settings.static_path}),
    (r'/', IndexHandler),
    (r'/interfaces/filedata', FileReadHandler),
    (r'/interfaces/database', DatabaseReadHandler),
    (r'/interfaces/snmp', SNMPReadHandler),
]
