import configparser
import json
from datetime import datetime
from pathlib import Path

import pytest

CONFIG_DATA_DIR = f'{Path(__file__).parent.parent.parent.resolve()}/Configurations/'
config = configparser.RawConfigParser()
config.read(f'{CONFIG_DATA_DIR}config.ini')

TEST_DATA_DIR = f'{Path(__file__).parent.parent.parent.resolve()}/TestData/'
ROOT = f'{Path(__file__).parent.parent.parent.resolve()}/'


def pytest_html_report_title(report):
    report.title = 'API Testing Report'


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # to remove environment section
    # config._metadata = None
    # set custom options only if none are provided from command line
    if not config.option.htmlpath:
        config.option.htmlpath = f'{ROOT}reports/' + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
        config.option.self_contained_html = True


@pytest.fixture()
def base_url():
    return config.get('common', 'baseURL')


@pytest.fixture()
def end_point():
    return config.get('common', 'endPoint')


@pytest.fixture()
def params():
    return config.get('common', 'params')


@pytest.fixture()
def headers():
    return config.get('common', 'headers')


@pytest.fixture()
def urls():
    with open(f'{TEST_DATA_DIR}api_data.json', 'r') as fp:
        urls = json.load(fp)
        urls = [tuple(item.values) for item in urls]
        return urls


def pytest_addoption(parser):
    parser.addoption("--configuration", action="store", default=f'{TEST_DATA_DIR}api_data.json')


@pytest.fixture(scope="session")
def configuration(request):
    configuration = None
    configuration = request.config.getoption("--configuration")
    with open(configuration, 'r') as f:
        configuration = json.load(f)
    return [tuple(item.values) for item in configuration]

# def pytest_configure(config):
#     """
#     it hooks for adding environment info to html report
#     """
#     config._metadata['Project Name'] = 'DexCom'
#     config._metadata['Module Name'] = 'ApiMonitor'
#     config._metadata['Tester'] = 'ver'
