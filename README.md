# Automation

## Introduction

Hello, 

Your assignment is to create a test framework for testing a dockerized application and its API.
The framework should allow developers to add new tests in a simple way.

In addition, you should create documentation that will allow any user to take the code and run the tests.

## Tasks

### About the Application
The application is a Python HTTP server application that provides 2 REST APIs on port 5001:

API 1: `/reverse`  
The API receives as string via "in" query parameter using GET HTTP request, and returns a response JSON with a field named "result" and its value should be the string provided with the words in reverse order.

For example:
Where in value of:
```
The quick brown fox jumps over the lazy dog"
```
Result value should be:
```
dog lazy the over jumps fox brown quick The
```

API 2: `/restore`  
The API returns the last result from API 1.

The application source code is under the app directory and included as a reference.

The built docker is available as neurealityai/automation-excercise:latest and can be run via:
```
docker run -d --rm -p 5001:5001 neurealityai/automation-excercise:latest
```

### Testing framework
Create a testing framework in Python using pytest which:

* Starts the application container created above
* Run tests to ensure the API conforms to the Application requirements listed above.
* Shuts down the application container when test is completed or on error.

The framework should be designed in a way that allows developers to easily add additional API tests on their own.

## Deliverables
A zip or .tar.gz file containing this git repository with:

* Tests written using pytest
* A TESTS.md readme file with instructions about this assignment, how to setup and run tests and what should be a successful test result.
