#! -*- coding: utf-8 -*-
import tornado.web
import tornado.escape

from app import settings

from app.interfaces import file_read_data, db_read_results, snmp_get_data


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        template = self.application.jinja_env.get_template('index.html')
        self.write(template.render(title="My title"))

class FileReadHandler(tornado.web.RequestHandler):
    def get(self):
        data     = file_read_data(filename=settings.DATA_FILE);
        message  = 'Not file data'
        template = 'interfaces/table.html'

        if data['response']:
            template = self.application.jinja_env.get_template('interfaces/table.html')
            render = template.render(data=data['data'])
        else:
            template = self.application.jinja_env.get_template('interfaces/error.html')
            render =  template.render(message=message)
        self.write(render)

class DatabaseReadHandler(tornado.web.RequestHandler):
    def get(self):
        data = db_read_results()
        message = "Can't data from database"
        if len(data):
            template = self.application.jinja_env.get_template('interfaces/table.html')
            render = template.render(data=data)
        else:
            template = self.application.jinja_env.get_template('interfaces/error.html')
            render =  template.render(message=message)
        self.write(render)

class SNMPReadHandler(tornado.web.RequestHandler):
    def get(self):
        data = snmp_get_data()
        message = 'Not SNMP web-interface'
        if len(data):
            template = self.application.jinja_env.get_template('interfaces/table.html')
            render = template.render(data=data)
        else:
            template = self.application.jinja_env.get_template('interfaces/error.html')
            render =  template.render(message=message)
        self.write(render)
