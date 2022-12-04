"""
Miscellaneous utilities
"""
import logging
from datetime import datetime

import pytz
from pythonjsonlogger import jsonlogger

LOGGER = logging.getLogger()


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            now = datetime.now(pytz.utc).isoformat()
            log_record['timestamp'] = now
        if not log_record.get('level'):
            log_record['level'] = record.levelname

