# -*- coding: utf-8 -*-

import logging

#logging.basicConfig(filename='traverse.py',level=logging.DEBUG)
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')

class Logger:

    def __init__(self):
        logging.basicConfig(format='%(asctime)-6s: %(name)s - %(levelname)s - %(message)s')
        self.log = logging.getLogger('gramafon')
        self.log.setLevel("DEBUG")

    def message(self,message):
        self.log.debug(message)



