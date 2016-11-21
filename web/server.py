#! -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop

from tornado.options import define, options, parse_command_line
from app import settings
from app import Application


define("port", default=8888, help="run on the given port", type=int)

def main():
    parse_command_line()

    mainApplication = Application()
    server_loop = tornado.ioloop.IOLoop.instance()

    http_server = tornado.httpserver.HTTPServer(mainApplication)
    http_server.listen(options.port)

    periodic_pull = tornado.ioloop.PeriodicCallback(mainApplication.periodic_run, settings.POLL_TIMEOUT, server_loop)
    periodic_pull.start()

    server_loop.start()

if __name__ == '__main__':
    main()
