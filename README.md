# Roman Numeral Converter

This application can be used to convert integers between 0 and 4000 to Roman Numerals.
The application provides users and interface to enter integers and view the Roman Numeral equivalent of the integers

- [Description of application](##Description)
- [Folder Structure](##folder-structure)
- [Running the application](##running-the-application)
- [Running tests](##running-tests)

## Description

The application was built in [Python 3](https://www.python.org/download/releases/3.0/). The interface is served with the help of [Python Flask](https://palletsprojects.com/p/flask/) library.

The tests are written using the [pytest](https://docs.pytest.org/en/latest/) library for python.

The application supports the conversion of integers to roman numerals between 0 and 4000.

## Folder Structure
Description of various files and folders contained in the application:
`requirements.txt` This file contains the python libraries required for running the application. Incase any new libraries are added, please add it to this file with the help of

``` bash
pip freeze > requirements.txt
```

`converter/converter.py` This is the file which implements the logic to convert integers to roman numerals.

`test/` This folder contains all the test cases for this application.

`app/app.py` This file helps to provide the interface for the application with the help of HTML files in the `app/templates/` folder.

`run.py` Runs the flask server

## Running the application

Before running the application please ensure you have `Python3` and `virtualenv` installed
The application can be run in the following steps:

```bash
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
python run.py
```

The application will be available on 
` http://127.0.0.1:5000/ `

## Running tests

Before running tests, please ensure you have all requirements in the `requirements.txt` file installed.

The tests can be run in the following way

```bash
pytest
```
