#! -*- coding: utf-8 -*-

from easysnmp import Session
from app import settings

class InterfaceSNMP(object):
    def __init__(self):
        self.session = Session(
            hostname=settings.SNMP_SESSION['host'], 
            community=settings.SNMP_SESSION['community'], 
            version=settings.SNMP_SESSION['version']
        )

    def get_results(self):
        response = []
        for res in settings.SNMP_RESOURCES:
            response.append([
                res['MIB'], 
                self.session.get(res['OID']).value
            ])
        return response

snmp_interface = InterfaceSNMP()