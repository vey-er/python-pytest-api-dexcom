"""
Miscellaneous utilities
"""
from datetime import datetime
import logging

from pythonjsonlogger import jsonlogger
import pytz

LOGGER = logging.getLogger()


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            now = datetime.now(pytz.utc).isoformat()
            log_record['timestamp'] = now
        if not log_record.get('level'):
            log_record['level'] = record.levelname

