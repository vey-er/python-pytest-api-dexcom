import json
import logging
from pathlib import Path

import requests
from pytest import mark

from Utilites.json_logger import CustomJsonFormatter

DEFAULT_LOGLEVEL = "INFO"
# Configure Logging
# LOGGER=LogGen.loggen()
LOGGER=logging.getLogger()
LOGGER.setLevel(DEFAULT_LOGLEVEL)
HANDLER = logging.StreamHandler()
HANDLER.setFormatter(CustomJsonFormatter())
LOGGER.handlers.clear()
LOGGER.addHandler(HANDLER)



TEST_DATA_DIR = f'{Path(__file__).parent.parent.parent.resolve()}/TestData/'
with open(f'{TEST_DATA_DIR}api_data.json', 'r') as fp:
    urls = json.load(fp)
    configuration = [tuple(item.values()) for item in urls]


# @mark.skip()
@mark.parametrize("base_url, end_point, params, headers", configuration)
def test_all_api(base_url, end_point, params, headers):
    """
        The Dexcom API’s “Info Endpoint” needs test automation! Create an automated test suite that
        tests the following:
        1. Verify that the endpoint responds with a 200 HTTP response status.
        2. Verify that the Content-Type header is returned as a valid json media type.
        3. From the list of items returned, find the item with the "Product Name" of "Dexcom API"
            and verify it has the following fields and values:
            a. "UDI / Device Identifier" is "00386270000668"
            b. ”Version" is "3.7.0.0"
            c. "Part Number (PN)" is "350-0019"
            d. Verify that the “Dexcom API” Sub-Components array includes an item with the a
            “name” of "api-gateway".
            e. Verify that the “Dexcom API” Sub-Components array includes an item with the a
            “name” of "insulin-service".
        4. Verify that the Content-Type header is returned as a valid xml media type.

    """
    extra = {
        "base_url": base_url,
        "end_point": end_point
    }
    LOGGER.info(f"Parametrize test started", extra=extra)
    response = requests.get(url=f'{base_url}{end_point}', params=params, headers=headers)
    try:
        # verify Status Code
        assert response.status_code == 200

        # verify Content-Type JSON
        assert response.headers['Content-Type'] == 'application/json'

        # response json to dict
        response_data = json.loads(response.text)

        # From the list of items returned, find the item with the "Product Name" of "Dexcom API"
        # and verify it has the following fields and values
        for item in response_data:
            if item.get("Product Name") == "Dexcom API":
                # a. "UDI / Device Identifier" is "00386270000668"
                assert item.get("UDI / Device Identifier") == "00386270000668"

                # verify  Version
                assert item["UDI / Production Identifier"]['Version'] == "3.1.1.0"  # 3.7.0.0"

                # verify Part Number
                assert item["UDI / Production Identifier"]["Part Number (PN)"] == "350-0019"

                # get sub components
                sub_comp = item["UDI / Production Identifier"]["Sub-Components"]

                # get sub component names to list
                sub_comp_names = [sub['Name'] for sub in sub_comp]

                # verify that sub comp has a “name” of "api-gateway".
                assert 'api-gateway' in sub_comp_names

                # verify that sub comp has a “name” of "insulin-service".
                assert 'insulin-service' in sub_comp_names

        # 4 verify Content-Type XML
        assert response.headers['Content-Type'] == 'application/xml'
    except AssertionError as e:
        extra = {"base_url": base_url, "end_point": end_point, "error": e.args}
        LOGGER.error(f"test failed extra={extra}")
        raise e

    LOGGER.info("Parametrize test successfully completed", extra={"base_url": base_url, "end_point": end_point})


def test_api(base_url, end_point, params, headers):
    """
        The Dexcom API’s “Info Endpoint” needs test automation! Create an automated test suite that
        tests the following:
        1. Verify that the endpoint responds with a 200 HTTP response status.
        2. Verify that the Content-Type header is returned as a valid json media type.
        3. From the list of items returned, find the item with the "Product Name" of "Dexcom API"
            and verify it has the following fields and values:
            a. "UDI / Device Identifier" is "00386270000668"
            b. ”Version" is "3.7.0.0"
            c. "Part Number (PN)" is "350-0019"
            d. Verify that the “Dexcom API” Sub-Components array includes an item with the a
            “name” of "api-gateway".
            e. Verify that the “Dexcom API” Sub-Components array includes an item with the a
            “name” of "insulin-service".
        4. Verify that the Content-Type header is returned as a valid xml media type.

    """
    LOGGER.info(
        "Api test started",
        extra={
            "base_url": base_url,
            "end_point": end_point
        }
    )
    response = requests.get(url=base_url + end_point, params=params, headers=headers)

    # verify Status Code
    assert response.status_code == 200

    # verify Content-Type JSON
    assert response.headers['Content-Type'] == 'application/json'

    # response json to dict
    response_data = json.loads(response.text)

    # From the list of items returned, find the item with the "Product Name" of "Dexcom API"
    # and verify it has the following fields and values
    for item in response_data:
        if item.get("Product Name") == "Dexcom API":
            # a. "UDI / Device Identifier" is "00386270000668"
            assert item.get("UDI / Device Identifier") == "00386270000668"

            # verify  Version
            assert item["UDI / Production Identifier"]['Version'] == "3.1.1.0"  # 3.7.0.0"

            # verify Part Number
            assert item["UDI / Production Identifier"]["Part Number (PN)"] == "350-0019"

            # get sub components
            sub_comp = item["UDI / Production Identifier"]["Sub-Components"]

            # get sub component names to list
            sub_comp_names = [sub['Name'] for sub in sub_comp]

            # verify that sub comp has a “name” of "api-gateway".
            assert 'api-gateway' in sub_comp_names

            # verify that sub comp has a “name” of "insulin-service".
            assert 'insulin-service' in sub_comp_names

    # 4 verify Content-Type XML
    assert response.headers['Content-Type'] == 'xml'
    LOGGER.info("API test successfully completed", extra={"base_url": base_url, "end_point": end_point, "NAME":"VEYIS"})
