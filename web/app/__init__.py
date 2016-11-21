#! -*- coding: utf-8 -*-

import random
import tornado.web

from jinja2 import Environment, FileSystemLoader, TemplateNotFound, Markup
from routes import routes

from app import settings
from app.dbs import db

from interfaces import file_refresh_data, \
    db_refresh_kpi, db_arrange_values


"""
    Jinja2 template environment
"""
jinja_env = Environment(loader=FileSystemLoader(settings.template_path), autoescape=True)
jinja_env.globals['random'] = random
jinja_env.globals['settings'] = settings
jinja_env.globals['static_url_root'] = settings.static_url
jinja_env.globals['include_raw'] = lambda filename : Markup(jinja_env.loader.get_source(jinja_env, filename)[0])


"""
    Переводим настройки в словарь
"""
dict_settings = dict((i, getattr(settings, i)) for i in settings.__dict__ if not i.startswith('__'))


class Application(tornado.web.Application):
    """
        Global Application
    """
    def __init__(self):
        self.db = db
        self.jinja_env = jinja_env
        tornado.web.Application.__init__(self, routes, **dict_settings)

        self.count_pull = 0
        print("Start server on: {0}".format(settings.site_url))

    def periodic_run(self):
        self.count_pull += 1
        print("tik tak: {0}".format(self.count_pull))
        #--
        file_refresh_data()
        #--
        db_refresh_kpi()
        db_arrange_values()

