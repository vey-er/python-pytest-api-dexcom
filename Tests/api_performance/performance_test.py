import logging


from locust import HttpUser, SequentialTaskSet, constant, events, tag, task
from pythonjsonlogger import jsonlogger

from Utilites.json_logger import CustomJsonFormatter
import logging

DEFAULT_LOGLEVEL = "INFO"

# Configure Logging
LOGGER=logging.getLogger()
LOGGER.setLevel(DEFAULT_LOGLEVEL)
HANDLER = logging.StreamHandler()
HANDLER.setFormatter(CustomJsonFormatter())
LOGGER.handlers.clear()
LOGGER.addHandler(HANDLER)


@events.test_start.add_listener
def on_test_start(**kwargs):
    LOGGER.info("......... Initiating Load Test .......")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    LOGGER.info("........ Load Test Completed ........")


class API(SequentialTaskSet):
    @tag('get')
    @task()
    def api_get(self):
        with self.client.get('/', catch_response=True) as response:
            if response.status_code != 200:
                response.failure('Failed, Text:' + response.text)
                LOGGER.error('Failed', extra={'response': response.text})
                self.parent.environment.runner.quit()

    @tag('post')
    @task()
    def api_post(self):
        with self.client.post('/', catch_response=True) as response:
            if response.status_code != 200:
                response.failure('Failed, Text:' + response.text)
                LOGGER.error('Failed', extra={'response': response.text})
                self.parent.environment.runner.quit()


class Users(HttpUser):
    wait_time = constant(1)
    tasks = [API]
