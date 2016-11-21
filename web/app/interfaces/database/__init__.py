#! -*- coding: utf-8 -*-

from app import settings
from app.dbs import db
from app.demo import getCounterValue
from app.interfaces.database.models import Kpi, Results

class InterfaceDatabase(object):
    def arrange(self):
        for item in Kpi.select_all():
            Results.insert(
                name=item[0],
                value=item[1]
            )

    def refresh_kpi_value(self):
        Kpi.clear()
        for counter in settings.COUNTERS:
            Kpi.insert(
                name=counter,
                value=getCounterValue()  
            )

    def read_from_database(self):
        return Results.select_all()

database_interface = InterfaceDatabase()