# Python-Pytest-API `requests`
 
[![API Tests with Pytest](https://github.com/vey-er/python-pytest-api-dexcom/actions/workflows/pytest.yml/badge.svg)](https://github.com/vey-er/python-pytest-api-dexcom/actions/workflows/pytest.yml)

#### Pytest is a mature full-featured Python testing frame that helps you write and run tests in Python.

#### The `requests` module allows you to send HTTP requests using Python.

## Getting started

* To download and install `pytest`, run this command from the terminal : `pipenv install pytest`
* To download and install `requests`, run this command from the terminal : `pipenv install requests`
* All the dependencies are in pipfile and when you clone the project, 
  * pip install pipenv
  * pipenv install
  
By default pytest only identifies the file names starting with `test_` or ending with `_test` as the test files.

Pytest requires the test method names to start with `test`. All other method names will be ignored even if we explicitly ask to run those methods.

A sample test below :

```python
def test_api_get_status(base_url, end_point, params, headers) :
    response = requests.get(url=base_url+end_point, params=params, headers=headers)
    assert response.status_code == 200
    
    # you may have more than one assertions in a test method
    response_data = json.loads(response.text)
    assert expected_key in response_data

```
## Running tests

If your tests are contained inside a folder 'Tests', then run the following command : `pytest Tests` 

To generate xml results, run the following command : `pytest Tests --junitxml="result.xml"`

For more on Pytest, go [here.](https://docs.pytest.org/en/stable/)