# pytest_tau_for_Testers

Hello 👋🏻

This is a new project with some tips about pytest which is a testing framework
and help testers to code ❤️

## Tips 

Pytest - [course](https://testautomationu.applitools.com/pytest-tutorial/) </br>
Asserts - [link here](https://docs.pytest.org/en/stable/how-to/assert.html) </br>
Parametrized fixtures - [link here](https://docs.pytest.org/en/stable/how-to/parametrize.html#parametrize-basics) </br>
Parametrizing Tests- [link here](https://docs.pytest.org/en/stable/example/parametrize.html#paramexamples)</br>
Python Decorators - [link here](https://realpython.com/primer-on-python-decorators/) </br>
Arrange-Act-Assert - [link here](https://jamescooke.info/arrange-act-assert-pattern-for-python-developers.html) </br>

## Commands

To run tests from the command line </br>
$ python -m pytest

To run particular test case 
$ pytest -k testCaseName 

To run with verbose and receive the output passed / failed 
$ python -m pytest -v 

to run and doesn't print the top banner like each status for each test module
$ python -m pytest -q

To run until one test case failure 
$ python -m pytest -x

To run until a certain number of failures 
$python -m pytest --maxfail=3

To run and generate report xml 
$ python -m pytest --junit-xml report.xml