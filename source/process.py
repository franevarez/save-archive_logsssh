# -*- coding: utf-8 *-*

import os
import sys
import datetime

os_path = ''

#principal object per getlogs
class log_listener():
    def __init__(self, name, configuration, generalRute):
        #add all configuration that need
        self.name       = name
        self.ip         = configuration['ip']
        self.user = configuration['user']
        self.password = configuration['password']
        self.rute = configuration['rute_log']

        if 'output' in configuration:
            self.output = configuration['output']
        else:
            self.output = generalRute
            
    def run(self):
        date = datetime.datetime.now()

        date_name = "\\%s-%s-%s" % (date.day, date.month, date.year)

        if not os.path.isdir(self.output+date_name):
            os.mkdir(self.output+date_name)
        else:
            c = 1
            while True:
                c += 1
                if not os.path.isdir(self.output+date_name+"_"+c):
                    os.mkdir(self.output+date_name+"_"+c)
                    break
        
