#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests
import os, sys, json
from pprint import pprint
import logging

class VeraModule:
    "Module generic"

    def  __init__(self,configParser=None):
        "Load configuration and start connexion"
        self._logger= logging.getLogger(__name__)
        self._logger.info("Plugin Munin start")
        self._configParser=configParser
        self._logfile = 'vera.log'

        self._DATAS = []
        self._INFOS = []
        self._veraData = {}
        self._parsedData = {}

        self._address = None

        if configParser:
            # Get logfile
            if self._configParser.has_option('VeraModule', 'address')\
                and self._configParser.get('VeraModule', 'address'):
                self._address = self._configParser.get('VeraModule', 'address')

            # Get devices
            if self._configParser.has_option('VeraModule', 'devices')\
                and self._configParser.get('VeraModule', 'devices'):
                self._devices = json.loads(self._configParser.get('VeraModule', 'devices'))

        # Get the data from Vera
        self._parseVERA()

    def _parseVERA(self):
        r = requests.get(self._address.join(['http://', '/data_request?id=user_data2&output_format=json']))
        self._veraData = r.json()

        for device in self._veraData['devices']:
            for device_searched in self._devices:
                if device['id'] == device_searched['id']:
                    if not device['room'] in self._parsedData:
                        self._parsedData[device['room']] = {}
                    if not device['name'] in self._parsedData[device['room']]:
                        variables = {}

                        for variable in device['states']:
                            for variable_searched in device_searched['variables']:
                                if variable['variable'] == variable_searched:
                                    variables[variable['variable']] = variable['value']
                        self._parsedData[device['room']][device['name']] = variables

    def _VeraPlugin(self,mode):
        "Vera plugin"
        now = time.strftime("%Y %m %d %H:%M", time.localtime())
        nowTimestamp = "%.0f" % time.mktime(time.strptime(now, '%Y %m %d %H:%M'))
        if mode == 'fetch': # DATAS
            for room in self._parsedData:
                for device in room:
                    self._DATAS.append({
                        'TimeStamp': nowTimestamp,
                        'Plugin': device['name'],
                        'Values': device['variables']
                    })

            return self._DATAS

        else: # INFOS
            for room in self._parsedData:
                for device in room:
                    dsInfos = {}
                    for variable_name,variable_value in device['variables'].items():
                        dsInfos[variable_name] = {
                            "type": "GAUGE",
                            "id": variable_name,
                            "draw": 'line',
                            "label": variable_name}
                    self._INFOS.append({
                        'Plugin': device['name'],
                        'Describ': '',
                        'Category': 'Vera',
                        'Base': '1000',
                        'Title': device['name'],
                        'Vlabel': '',
                        'Infos': dsInfos,
                    })
            return self._INFOS

    def getData(self):
        "get and return all data collected"
        # Refresh status
        self._VeraPlugin('fetch')
        return self._DATAS

    def getInfo(self):
        "Return plugins info for refresh"
        self._VeraPlugin('config')
        return self._INFOS

if __name__ == "__main__":
    _logger = logging.getLogger()
    ch = logging.StreamHandler(stream=sys.stdout)
    _logger.addHandler(ch)
    _logger.setLevel(logging.DEBUG)
    stats = VeraModule(None)
    print str(stats.getData())
    print str(stats.getInfo())
