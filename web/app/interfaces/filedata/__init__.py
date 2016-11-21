#! -*- coding: utf-8 -*-

import os
from random import randint

from app import settings
from app.demo import getCounterValue


class InterfaceFile(object):
    def get_file(fun):
        def tmp(self, *args, **kwargs):
            if 'filename' in kwargs.keys():
                if os.path.exists(kwargs['filename']):
                    self.file = open(kwargs['filename'], 'r')
                    result = {'response': True, 'data':  fun(self, *args, **kwargs)}
                    self.file.close()
                else:
                    result = {'response': False, 'data': [], 'error': 'file not found'}
            else:
                result = {'response': False, 'data': [], 'error': "not set 'filename=<data file name>'"}
            return result
        return tmp

    def refresh_values(self):
        if os.path.exists(settings.DATA_FILE):
            os.remove(settings.DATA_FILE)

        f = open(settings.DATA_FILE,'w');
        for i in range(1, 100):
            f.write('{0},{1}\n'.format(
                settings.COUNTERS[randint(0,settings.COUNTERS_LEN)], 
                getCounterValue()
            ))
        f.close()

    @get_file
    def read_from_file(self, *args, **kwargs):
        result = []
        for line in self.file:
            line
            result.append(line.rstrip("\n").split(','))
        return result


file_interface = InterfaceFile()
