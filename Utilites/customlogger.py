import logging

from datetime import datetime
import logging

from pythonjsonlogger import jsonlogger
import pytz

import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="./Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger



