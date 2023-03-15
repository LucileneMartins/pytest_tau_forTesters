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
Report HTML - [link here](https://github.com/pytest-dev/pytest-html)</br>
Parallel tests - [link here](https://pytest-xdist.readthedocs.io/en/stable/)


## Commands

:bulb: To run tests from the command line </br>
$ python -m pytest </br>

:bulb: To run particular test Module </br>
$ python -m pytest tests/nameModule.py </br>

:bulb: To run particular test case </br>
$ python -m pytest tests/nameModule.py::test_scenario_name </br>

:bulb: To run test case that contains the name a substring ( in this case one is the substring) </br>
$ python -m pytest -k one </br>

:bulb: To run with verbose and receive the output passed / failed  </br>
$ python -m pytest -v </br>

:bulb: to run and doesn't print the top banner like each status for each test module </br>
$ python -m pytest -q </br>

:bulb: To run until one test case failure  </br>
$ python -m pytest -x </br>

:bulb: To run until a certain number of failures </br>
$python -m pytest --maxfail=3 </br>
 
:bulb: To run and generate report xml  </br>
$ python -m pytest --junit-xml report.xml </br>

:bulb: To run and generate report html  </br>
first you need to install the report html pluggin : pip install pytest-html </br> 
$ python -m pytest --html=report.html </br>

:bulb: To run and check the modules coverage </br>
first you need to install the pluggin : pip install pytest-cov </br>
$ python -m pytest --cov=stuff </br>

:bulb: To run the coverage and generate report html </br>
$ python -m pytest --cov=src/stuff --cov-report html </br>

:bulb: To run parallel tests </br>
First you will need to install the pluggin : pip install pytest-xdist </br>
$ python -m pytest -n 3  </br>
