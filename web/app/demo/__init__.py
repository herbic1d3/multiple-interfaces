#! -*- coding: utf-8 -*-

import datetime
from random import randint

def getCounterValue():
    return randint(1, 100000)+int((datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds())
           


