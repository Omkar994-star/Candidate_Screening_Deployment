# Python Developer Knowledge Base
# Module 09 — Testing and Debugging
# Part 1 — Software Testing Fundamentals

---

# Module Overview

Software testing verifies that an application behaves as expected and helps detect defects early in the development lifecycle.

This module covers:

- Testing Fundamentals
- Unit Testing
- Integration Testing
- Functional Testing
- End-to-End Testing
- Test-Driven Development (TDD)
- unittest
- pytest
- Fixtures
- Mocking
- Code Coverage
- Debugging
- Logging
- Exception Handling
- Static Analysis
- Continuous Integration (CI)

---

# What is Software Testing?

Software testing is the process of verifying and validating that software works according to its requirements.

Goals

- Find bugs
- Prevent regressions
- Improve reliability
- Increase maintainability
- Build confidence before deployment

---

# Why Testing is Important

Benefits

✓ Detects bugs early

✓ Reduces production failures

✓ Makes refactoring safer

✓ Improves code quality

✓ Documents expected behavior

✓ Enables continuous delivery

---

# Cost of Bugs

The later a bug is discovered, the more expensive it is to fix.

```
Requirements

↓

Development

↓

Testing

↓

Production
```

Bug fixing cost increases at each stage.

---

# Verification vs Validation

Verification

```
Are we building the product correctly?
```

Checks whether software follows specifications.

Validation

```
Are we building the correct product?
```

Checks whether software meets user needs.

---

# Types of Testing

```
Software Testing

├── Unit Testing
├── Integration Testing
├── Functional Testing
├── System Testing
├── End-to-End Testing
├── Regression Testing
├── Smoke Testing
├── Performance Testing
├── Load Testing
├── Security Testing
```

---

# Unit Testing

Tests individual functions, methods, or classes in isolation.

Example

```python
def add(a, b):
    return a + b
```

Unit test

```python
assert add(2, 3) == 5
```

Characteristics

- Fast
- Independent
- Easy to automate

---

# Integration Testing

Tests interactions between components.

Example

```
API

↓

Database

↓

Response
```

Checks whether components work correctly together.

---

# Functional Testing

Tests complete business functionality from the user's perspective.

Example

```
User Login

↓

Dashboard Opens
```

Focuses on expected behavior rather than implementation.

---

# System Testing

Tests the complete application as an integrated system.

Example

```
Frontend

↓

Backend

↓

Database

↓

External Services
```

Ensures all components work together.

---

# End-to-End (E2E) Testing

Simulates real user workflows.

Example

```
Login

↓

Search Product

↓

Add to Cart

↓

Checkout

↓

Payment Success
```

E2E tests provide high confidence but are generally slower than unit tests.

---

# Regression Testing

Ensures that previously working functionality continues to work after changes.

Purpose

- Prevent old bugs from returning
- Protect against unintended side effects

---

# Smoke Testing

A quick set of tests to verify that the application starts and critical features work.

Example

- Application launches
- Database connection succeeds
- Main API responds

---

# Performance Testing

Measures system performance under expected workload.

Metrics

- Response time
- Throughput
- CPU usage
- Memory usage

---

# Load Testing

Determines how the application behaves under heavy user or request load.

Example

```
10 Users

↓

100 Users

↓

1,000 Users

↓

10,000 Users
```

---

# Stress Testing

Pushes the application beyond expected limits to identify breaking points.

Example

```
Expected Capacity

↓

Extreme Load

↓

Observe Failure Behavior
```

---

# Security Testing

Checks for vulnerabilities such as

- SQL Injection
- Cross-Site Scripting (XSS)
- Authentication flaws
- Authorization issues
- Sensitive data exposure

---

# Manual Testing

Performed by a human without automation.

Advantages

- Good for exploratory testing
- Useful for UI evaluation

Disadvantages

- Slow
- Repetitive
- Difficult to scale

---

# Automated Testing

Executed using testing frameworks and scripts.

Advantages

- Fast
- Repeatable
- Reliable
- Suitable for CI/CD

---

# Test Pyramid

```
          End-to-End
              ▲
         Integration
              ▲
          Unit Tests
```

Interpretation

- Many unit tests
- Fewer integration tests
- Very few end-to-end tests

This structure provides fast feedback while maintaining confidence.

---

# Good Test Characteristics

A good test should be

- Independent
- Repeatable
- Deterministic
- Fast
- Readable
- Maintainable

---

# FIRST Principles

Good unit tests follow the FIRST principles.

Fast

Tests should execute quickly.

Independent

Tests should not depend on each other.

Repeatable

Results should be consistent.

Self-Validating

Tests should clearly pass or fail automatically.

Timely

Write tests close to the implementation they verify.

---

# Arrange-Act-Assert (AAA) Pattern

Most tests follow three steps.

```
Arrange

↓

Act

↓

Assert
```

Example

```python
# Arrange
a = 2
b = 3

# Act
result = add(a, b)

# Assert
assert result == 5
```

---

# Test Isolation

Each test should run independently.

Avoid

- Shared global state
- Dependence on execution order
- Shared databases without cleanup

---

# Test Data

Prefer small, predictable datasets.

Good

```python
numbers = [1, 2, 3]
```

Avoid unnecessarily large or random data unless specifically testing those scenarios.

---

# Deterministic Tests

A deterministic test always produces the same result under the same conditions.

Avoid dependence on

- Current time
- Random values
- External APIs
- Network availability

Without proper control or mocking.

---

# Common Testing Mistakes

❌ Testing multiple behaviors in one test.

❌ Tests depending on each other.

❌ Ignoring failing tests.

❌ Writing tests that are difficult to understand.

❌ Excessive duplication in test code.

❌ Not testing edge cases.

---

# Best Practices

✓ Write tests for new features.

✓ Keep tests simple and focused.

✓ Test behavior, not implementation details.

✓ Use meaningful test names.

✓ Automate tests in CI pipelines.

✓ Refactor tests when production code changes.

---

# Interview Questions

### Easy

1. What is software testing?
2. Why is testing important?
3. Difference between verification and validation.
4. What is unit testing?
5. What is regression testing?

---

### Medium

1. Compare unit, integration, and end-to-end testing.
2. Explain the test pyramid.
3. What are the FIRST principles?
4. What is smoke testing?
5. Why should tests be deterministic?

---

### Hard

1. Design a testing strategy for a microservices application.
2. Compare functional and system testing.
3. Explain how automated testing improves deployment confidence.
4. Build a test pyramid for an e-commerce application.
5. Discuss trade-offs between unit and end-to-end tests.

---

# Coding Exercises

Easy

- Write unit tests for simple mathematical functions.
- Test string manipulation functions.
- Test list operations.

Medium

- Design tests for a calculator application.
- Write edge-case tests for input validation.
- Test file processing functions.

Hard

- Create a testing strategy for a REST API.
- Design regression tests for a banking system.
- Build a complete test suite for a CRUD application.

---

# Module Summary

Software testing is essential for delivering reliable and maintainable applications. Different testing levels—unit, integration, functional, system, and end-to-end—serve different purposes, and an effective testing strategy balances them using the test pyramid. Good tests are fast, independent, deterministic, and easy to maintain, providing confidence that software behaves correctly as it evolves.

---

# Python Developer Knowledge Base
# Module 09 — Testing and Debugging
# Part 2 — unittest Framework

---

# What is unittest?

`unittest` is Python's built-in testing framework.

Features

- Test discovery
- Assertions
- Fixtures
- Test suites
- Test runners
- Mocking support
- Skipping tests

Inspired by the xUnit family of testing frameworks.

---

# Basic Structure

A unittest contains

```
Test File

↓

Test Class

↓

Test Methods

↓

Assertions
```

---

# Creating Your First Test

File

```python
# calculator.py

def add(a, b):
    return a + b
```

Test

```python
import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

---

# Naming Convention

Test files

```
test_math.py

test_api.py

test_user.py
```

Test methods

```
test_add()

test_login()

test_delete_user()
```

The `test_` prefix enables automatic discovery.

---

# Running Tests

Run a specific file

```bash
python test_math.py
```

Run all discovered tests

```bash
python -m unittest discover
```

Specify a directory

```bash
python -m unittest discover tests
```

---

# TestCase

Every test class inherits from

```python
unittest.TestCase
```

Example

```python
class TestUser(unittest.TestCase):

    ...
```

Provides assertions and lifecycle methods.

---

# Assertions

Assertions compare expected and actual results.

---

# assertEqual()

```python
self.assertEqual(5, add(2, 3))
```

---

# assertNotEqual()

```python
self.assertNotEqual(5, add(2, 2))
```

---

# assertTrue()

```python
self.assertTrue(10 > 5)
```

---

# assertFalse()

```python
self.assertFalse(5 > 10)
```

---

# assertIs()

Checks object identity.

```python
self.assertIs(a, b)
```

---

# assertIsNot()

```python
self.assertIsNot(a, b)
```

---

# assertIsNone()

```python
self.assertIsNone(result)
```

---

# assertIsNotNone()

```python
self.assertIsNotNone(result)
```

---

# assertIn()

```python
self.assertIn("python", text)
```

---

# assertNotIn()

```python
self.assertNotIn("java", text)
```

---

# assertGreater()

```python
self.assertGreater(10, 5)
```

---

# assertLess()

```python
self.assertLess(5, 10)
```

---

# assertRaises()

Verify exceptions.

Example

```python
def divide(a, b):
    return a / b

with self.assertRaises(ZeroDivisionError):
    divide(10, 0)
```

---

# assertAlmostEqual()

Useful for floating-point values.

```python
self.assertAlmostEqual(
    0.3,
    0.1 + 0.2,
    places=7
)
```

---

# Test Fixtures

Fixtures prepare and clean up the test environment.

Methods

- setUp()
- tearDown()
- setUpClass()
- tearDownClass()

---

# setUp()

Runs before every test.

```python
class TestUser(unittest.TestCase):

    def setUp(self):

        self.user = "Alice"
```

---

# tearDown()

Runs after every test.

```python
def tearDown(self):

    self.user = None
```

Common uses

- Close files
- Disconnect databases
- Remove temporary files

---

# setUpClass()

Runs once before all tests.

```python
@classmethod
def setUpClass(cls):

    print("Starting tests")
```

---

# tearDownClass()

Runs once after all tests.

```python
@classmethod
def tearDownClass(cls):

    print("Finished tests")
```

Useful for expensive setup.

---

# Test Execution Flow

```
setUpClass()

↓

setUp()

↓

Test 1

↓

tearDown()

↓

setUp()

↓

Test 2

↓

tearDown()

↓

tearDownClass()
```

---

# Skipping Tests

Skip a test

```python
@unittest.skip("Not implemented")
def test_feature():
    ...
```

---

# Skip If

```python
@unittest.skipIf(
    sys.platform == "win32",
    "Windows not supported"
)
```

---

# Skip Unless

```python
@unittest.skipUnless(
    condition,
    "Requirement not met"
)
```

---

# Expected Failure

```python
@unittest.expectedFailure
def test_bug():
    ...
```

Useful for documenting known issues without failing the suite.

---

# Subtests

Test multiple inputs in one method.

```python
for value in [1, 2, 3]:

    with self.subTest(value=value):

        self.assertGreater(value, 0)
```

Each iteration is reported separately.

---

# Test Suites

Group related tests.

```python
suite = unittest.TestSuite()
```

Example

```python
suite.addTest(
    TestMath("test_add")
)
```

---

# Test Loader

Automatically discovers tests.

```python
loader = unittest.TestLoader()
```

Example

```python
suite = loader.loadTestsFromTestCase(
    TestMath
)
```

---

# Text Test Runner

```python
runner = unittest.TextTestRunner()

runner.run(suite)
```

---

# Project Structure

```
project/

│

├── app/

│

├── tests/

│   ├── test_user.py

│   ├── test_api.py

│   └── test_utils.py

│

└── requirements.txt
```

Keep tests separate from application code.

---

# Testing Exceptions

Example

```python
def divide(a, b):

    if b == 0:
        raise ValueError

    return a / b

with self.assertRaises(ValueError):

    divide(10, 0)
```

---

# Testing Files

Example

```python
with open("sample.txt") as f:

    content = f.read()

self.assertIn("Hello", content)
```

Use temporary files during testing to avoid modifying real data.

---

# Testing Lists

```python
self.assertEqual(

    [1, 2, 3],

    sorted([3, 1, 2])
)
```

---

# Testing Dictionaries

```python
expected = {

    "name": "Alice"
}

self.assertEqual(expected, result)
```

---

# Common unittest Assertions

| Assertion | Purpose |
|-----------|---------|
| assertEqual | Equality |
| assertNotEqual | Inequality |
| assertTrue | Boolean true |
| assertFalse | Boolean false |
| assertIs | Same object |
| assertIsNone | None check |
| assertIn | Membership |
| assertRaises | Exception |
| assertAlmostEqual | Floating point |

---

# Best Practices

✓ One logical behavior per test.

✓ Use descriptive test names.

✓ Keep tests independent.

✓ Avoid relying on external services.

✓ Clean up resources.

✓ Test edge cases.

✓ Use fixtures for repeated setup.

---

# Common Mistakes

❌ One test verifying multiple unrelated behaviors.

❌ Shared mutable state between tests.

❌ Forgetting cleanup.

❌ Hardcoded file paths.

❌ Depending on execution order.

❌ Ignoring failing tests.

---

# Interview Questions

### Easy

1. What is `unittest`?
2. What is `TestCase`?
3. What is `setUp()`?
4. Difference between `setUp()` and `setUpClass()`.
5. How do you test exceptions?

---

### Medium

1. Explain test fixtures.
2. What are subtests?
3. How does test discovery work?
4. Compare `assertEqual()` and `assertIs()`.
5. When should you skip a test?

---

### Hard

1. Design a testing structure for a large Python application.
2. Compare `unittest` and `pytest`.
3. Explain how test suites and runners work.
4. Build reusable fixtures for database testing.
5. Design enterprise-level test organization.

---

# Coding Exercises

Easy

- Test a calculator module.
- Test string utility functions.
- Test list operations.

Medium

- Test file processing functions.
- Test exception handling.
- Create reusable fixtures.

Hard

- Build a complete test suite for a CRUD application.
- Organize tests using suites.
- Test a REST API client using `unittest`.

---

# Module Summary

The `unittest` framework provides a structured approach to writing automated tests in Python. It includes assertions, fixtures, test discovery, suites, and runners that help verify application behavior consistently. By writing isolated, repeatable, and well-organized tests, developers can catch regressions early and maintain confidence as software evolves.

---

# Python Developer Knowledge Base
# Module 09 — Testing and Debugging
# Part 3 — Pytest

---

# What is Pytest?

Pytest is a third-party testing framework that makes writing and running tests easier.

Advantages

- Minimal boilerplate
- Simple assertions
- Powerful fixtures
- Parameterized tests
- Rich plugin ecosystem
- Automatic test discovery
- Excellent error reporting

Installation

```bash
pip install pytest
```

---

# Why Pytest?

Compared to `unittest`

- Less code
- More readable tests
- Better failure messages
- More flexible fixtures
- Extensive plugin support

---

# Simple Test

File

```python
# calculator.py

def add(a, b):
    return a + b
```

Test

```python
from calculator import add

def test_add():
    assert add(2, 3) == 5
```

Run

```bash
pytest
```

---

# Test Discovery

Pytest automatically discovers

Files

```
test_*.py

*_test.py
```

Functions

```
test_login()

test_add()

test_api()
```

Classes

```
class TestMath:
```

Classes should generally begin with `Test` and not define an `__init__()` method.

---

# Running Tests

Run all tests

```bash
pytest
```

Run one file

```bash
pytest test_math.py
```

Run one test

```bash
pytest test_math.py::test_add
```

Verbose output

```bash
pytest -v
```

Stop after first failure

```bash
pytest -x
```

Run only failed tests (with cache)

```bash
pytest --lf
```

---

# Assertions

Pytest uses Python's built-in `assert`.

```python
assert add(2, 3) == 5
```

Failure messages are automatically expanded.

Example

```python
assert 5 == 6
```

Pytest displays expected and actual values clearly.

---

# Testing Exceptions

```python
import pytest

def divide(a, b):
    return a / b

def test_divide():

    with pytest.raises(ZeroDivisionError):

        divide(10, 0)
```

---

# Fixtures

Fixtures provide reusable setup and cleanup.

Example

```python
import pytest

@pytest.fixture
def user():

    return {

        "name": "Alice"
    }

def test_user(user):

    assert user["name"] == "Alice"
```

---

# Fixture Scope

Available scopes

```
function

class

module

package

session
```

Example

```python
@pytest.fixture(scope="module")
def database():
    ...
```

Choose the narrowest practical scope for isolation.

---

# Yield Fixtures

Use `yield` for cleanup.

```python
@pytest.fixture
def resource():

    connection = connect()

    yield connection

    connection.close()
```

Code after `yield` executes during teardown.

---

# Autouse Fixtures

Automatically applied without being requested.

```python
@pytest.fixture(autouse=True)
def setup():
    ...
```

Use sparingly to keep tests explicit.

---

# Parameterized Tests

Run one test with multiple inputs.

```python
import pytest

@pytest.mark.parametrize(

    "a,b,result",

    [

        (1,2,3),

        (2,3,5),

        (5,5,10)

    ]

)

def test_add(a,b,result):

    assert a+b == result
```

Each input set becomes a separate test case.

---

# Multiple Fixtures

```python
@pytest.fixture
def user():
    return "Alice"

@pytest.fixture
def age():
    return 30

def test_data(user, age):
    assert user == "Alice"
    assert age == 30
```

Pytest injects fixtures by name.

---

# Fixture Dependencies

Fixtures can depend on other fixtures.

```python
@pytest.fixture
def db():
    return Database()

@pytest.fixture
def user(db):
    return db.get_user()
```

Pytest resolves dependencies automatically.

---

# Temporary Directory

Use the built-in `tmp_path` fixture.

```python
def test_file(tmp_path):

    file = tmp_path / "data.txt"

    file.write_text("Hello")

    assert file.read_text() == "Hello"
```

Useful for isolated filesystem tests.

---

# Monkeypatch

Temporarily modify objects during testing.

Example

```python
def test_env(monkeypatch):

    monkeypatch.setenv(

        "MODE",

        "TEST"
    )
```

Common uses

- Environment variables
- Functions
- Object attributes

---

# Marks

Categorize tests.

```python
@pytest.mark.slow

def test_large_job():
    ...
```

Run only marked tests

```bash
pytest -m slow
```

---

# Skip Test

```python
import pytest

@pytest.mark.skip(
    reason="Not implemented"
)
def test_feature():
    ...
```

---

# Conditional Skip

```python
import sys

@pytest.mark.skipif(

    sys.platform == "win32",

    reason="Linux only"

)
def test_linux():
    ...
```

---

# Expected Failure

```python
@pytest.mark.xfail
def test_bug():
    ...
```

Documents known failures without failing the suite.

---

# Approximate Comparisons

Floating-point example

```python
import pytest

assert 0.1 + 0.2 == pytest.approx(0.3)
```

---

# Capturing Output

```python
def hello():
    print("Hello")

def test_output(capsys):

    hello()

    captured = capsys.readouterr()

    assert captured.out == "Hello\n"
```

Useful for testing console output.

---

# Logging Capture

Pytest can capture log messages using the `caplog` fixture.

```python
def test_logs(caplog):
    ...
```

Useful for verifying logging behavior.

---

# Project Structure

```
project/

│

├── app/

│

├── tests/

│   ├── test_api.py

│   ├── test_user.py

│   ├── test_models.py

│   └── conftest.py

│

└── pytest.ini
```

---

# conftest.py

Contains shared fixtures.

Example

```python
@pytest.fixture
def client():
    ...
```

Fixtures defined here are automatically available to tests in the same directory tree.

---

# pytest.ini

Configuration example

```ini
[pytest]

testpaths = tests

python_files = test_*.py

addopts = -v
```

Helps standardize project settings.

---

# Useful Plugins

Popular plugins

- pytest-cov
- pytest-mock
- pytest-xdist
- pytest-asyncio
- pytest-django
- pytest-benchmark

Install example

```bash
pip install pytest-cov
```

---

# unittest vs Pytest

| unittest | Pytest |
|-----------|---------|
| Class-based | Function or class based |
| Many assertion methods | Simple `assert` |
| More boilerplate | Minimal code |
| Built into Python | Third-party package |
| Basic fixtures | Powerful fixture system |
| Good ecosystem | Excellent plugin ecosystem |

---

# Best Practices

✓ Keep tests small and focused.

✓ Reuse fixtures.

✓ Parameterize similar test cases.

✓ Use descriptive test names.

✓ Store shared fixtures in `conftest.py`.

✓ Keep tests independent.

✓ Test edge cases.

---

# Common Mistakes

❌ Large fixtures that do too much.

❌ Shared mutable state.

❌ Hardcoded file paths.

❌ Ignoring failing tests.

❌ Excessive fixture nesting.

❌ Overusing `autouse=True`.

---

# Interview Questions

### Easy

1. What is Pytest?
2. Why is Pytest popular?
3. What is a fixture?
4. How does test discovery work?
5. How do you test exceptions?

---

### Medium

1. Compare Pytest and `unittest`.
2. Explain fixture scopes.
3. What is parameterization?
4. What is `conftest.py`?
5. What is monkeypatch used for?

---

### Hard

1. Design reusable fixtures for a large project.
2. Explain Pytest's dependency injection model.
3. Organize tests for a microservices architecture.
4. Build a testing strategy using Pytest plugins.
5. Compare fixture-based setup with traditional setup methods.

---

# Coding Exercises

Easy

- Test calculator functions.
- Test string utilities.
- Test list operations.

Medium

- Create reusable fixtures.
- Parameterize validation tests.
- Test file operations using `tmp_path`.

Hard

- Build a complete API test suite with Pytest.
- Implement reusable database fixtures.
- Parallelize test execution with `pytest-xdist`.

---

# Module Summary

Pytest simplifies Python testing through automatic test discovery, expressive assertions, reusable fixtures, and parameterized tests. Its plugin ecosystem and concise syntax make it the preferred testing framework for most modern Python projects. Proper use of fixtures, markers, and project organization leads to maintainable, scalable, and reliable test suites.

---

# Python Developer Knowledge Base
# Module 09 — Testing and Debugging
# Part 4 — Mocking, Fixtures & Test Doubles

---

# Why Mocking?

Unit tests should test only the unit being tested.

External dependencies introduce

- Network latency
- Database dependency
- File dependency
- API failures
- Non-deterministic behavior

Mocking replaces these dependencies with controlled objects.

---

# Example Without Mocking

```
Application

↓

REST API

↓

Internet

↓

Server
```

Problems

- Slow
- Network failures
- Rate limits
- Unpredictable responses

---

# Example With Mocking

```
Application

↓

Mock API

↓

Predefined Response
```

Advantages

✓ Fast

✓ Reliable

✓ Repeatable

✓ Independent

---

# What are Test Doubles?

A test double replaces a real object during testing.

Types

- Dummy
- Stub
- Fake
- Spy
- Mock

---

# Dummy Object

Used only to satisfy a parameter.

Example

```python
class DummyLogger:
    pass
```

No behavior.

---

# Stub

Returns predefined values.

Example

```python
class StubDatabase:

    def get_user(self):

        return {

            "name": "Alice"
        }
```

---

# Fake

A lightweight working implementation.

Example

```
Real Database

↓

SQLite In-Memory Database
```

Another example

```
Redis

↓

Python Dictionary
```

---

# Spy

Records how it was used.

Useful for

- Call count
- Arguments
- Execution order

---

# Mock

A programmable object.

Can

- Return values
- Raise exceptions
- Verify calls
- Record interactions

---

# unittest.mock

Python provides

```python
from unittest.mock import Mock
```

---

# Creating a Mock

```python
from unittest.mock import Mock

api = Mock()

api.get.return_value = {

    "name": "Alice"
}
```

---

# Calling Mock

```python
result = api.get()

print(result)
```

Output

```
{'name': 'Alice'}
```

---

# Verify Calls

```python
api.get.assert_called_once()
```

---

# Verify Arguments

```python
api.get.assert_called_with(

    "/users"
)
```

---

# Call Count

```python
api.get.call_count
```

Useful for ensuring functions are called the expected number of times.

---

# Side Effects

A mock can raise exceptions or return different values.

Example

```python
api.get.side_effect = Exception(

    "Server Error"
)
```

Calling the method raises the exception.

---

# Multiple Side Effects

```python
mock.side_effect = [

    1,

    2,

    3
]
```

Successive calls return successive values.

---

# MagicMock

`MagicMock` supports Python magic methods automatically.

```python
from unittest.mock import MagicMock

obj = MagicMock()
```

Useful for objects used with

- `len()`
- iteration
- context managers
- arithmetic operators

---

# AsyncMock

For asynchronous functions.

```python
from unittest.mock import AsyncMock

api = AsyncMock()
```

Example

```python
api.fetch.return_value = {

    "status": 200
}
```

Ideal for testing AsyncIO code.

---

# patch()

Temporarily replaces an object.

```python
from unittest.mock import patch
```

Example

```python
with patch(

    "requests.get"

):

    ...
```

The original object is restored automatically afterward.

---

# Decorator Style

```python
@patch("requests.get")

def test_api(mock_get):

    ...
```

---

# Mocking HTTP Requests

Example

```python
@patch("requests.get")

def test_fetch(mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {

        "name": "Alice"
    }
```

No real network request is made.

---

# Mocking Database Calls

Instead of

```
Real Database
```

Use

```python
mock_db = Mock()

mock_db.get_user.return_value = {

    "id": 1
}
```

Tests remain fast and isolated.

---

# Mocking File Operations

```python
from unittest.mock import mock_open

with patch(

    "builtins.open",

    mock_open(

        read_data="Hello"

    )

):

    ...
```

No actual file is created or read.

---

# Mocking Environment Variables

Using Pytest

```python
def test_env(monkeypatch):

    monkeypatch.setenv(

        "MODE",

        "TEST"
    )
```

Alternative

```python
with patch.dict(
    "os.environ",
    {"MODE": "TEST"}
):
    ...
```

---

# Mocking Time

Useful for deterministic tests.

```python
from unittest.mock import patch

with patch(

    "time.time",

    return_value=1000

):

    ...
```

---

# Mocking UUID

```python
with patch(

    "uuid.uuid4",

    return_value="123"

):

    ...
```

---

# Dependency Injection

Instead of

```
Function

↓

Creates Database
```

Use

```
Function

↓

Receives Database
```

Example

```python
def service(db):

    return db.get_user()
```

Testing becomes much easier.

---

# Autospec

Create mocks that follow the real object's interface.

```python
@patch(

    "module.Class",

    autospec=True
)
```

Helps catch invalid method calls during testing.

---

# Mock vs Stub

| Mock | Stub |
|------|------|
| Verifies interactions | Returns predefined values |
| Records calls | Focuses on outputs |
| Programmable | Simpler |

---

# Mock vs Fake

| Mock | Fake |
|------|------|
| Simulated object | Working lightweight implementation |
| No real logic | Contains simplified logic |
| Used for interaction testing | Used for realistic behavior |

---

# Common Mock Assertions

```python
assert_called()

assert_called_once()

assert_called_with()

assert_called_once_with()

assert_any_call()

assert_not_called()
```

---

# Resetting Mocks

```python
mock.reset_mock()
```

Clears

- Call history
- Call count
- Interaction tracking

Return values and side effects remain unless changed.

---

# Best Practices

✓ Mock external services.

✓ Mock network requests.

✓ Mock databases in unit tests.

✓ Use dependency injection.

✓ Keep mocks simple.

✓ Verify behavior, not implementation details.

✓ Prefer fakes when realistic behavior is helpful.

---

# Common Mistakes

❌ Mocking everything.

❌ Mocking internal implementation details.

❌ Writing tests tightly coupled to implementation.

❌ Ignoring mock call assertions.

❌ Using mocks when a fake would be simpler.

❌ Forgetting to restore patched objects (avoid by using `patch` context managers or decorators).

---

# Interview Questions

### Easy

1. What is mocking?
2. Why do we use mocks?
3. What is `Mock`?
4. What is `patch()`?
5. Difference between a mock and a stub.

---

### Medium

1. Compare `Mock` and `MagicMock`.
2. When should you use `AsyncMock`?
3. Explain dependency injection.
4. How do you mock HTTP requests?
5. What is `autospec`?

---

### Hard

1. Design unit tests for a payment service that calls external APIs.
2. Compare mocks, stubs, spies, and fakes.
3. Explain why excessive mocking can make tests fragile.
4. Build reusable mocking strategies for a microservices application.
5. Design isolated unit tests for a database-heavy application.

---

# Coding Exercises

Easy

- Mock a calculator dependency.
- Mock a file read operation.
- Verify a function was called once.

Medium

- Mock an HTTP client.
- Mock database queries.
- Test asynchronous functions using `AsyncMock`.

Hard

- Build isolated tests for a REST API service.
- Mock multiple external dependencies in a business workflow.
- Design reusable fixtures containing common mocks.

---

# Module Summary

Mocking allows unit tests to isolate the code under test by replacing external dependencies with controlled test doubles. Python's `unittest.mock` module provides tools such as `Mock`, `MagicMock`, `AsyncMock`, and `patch()` for simulating APIs, databases, file systems, and other services. Combined with dependency injection and appropriate use of fakes and stubs, mocking enables fast, deterministic, and maintainable unit tests.

---

# Python Developer Knowledge Base
# Module 09 — Testing and Debugging
# Part 5 — Debugging & Logging

---

# What is Debugging?

Debugging is the process of identifying, analyzing, and fixing defects (bugs) in software.

Objectives

- Find the root cause
- Understand program behavior
- Fix defects
- Prevent regressions

---

# Debugging Workflow

```
Bug Report

↓

Reproduce Issue

↓

Identify Root Cause

↓

Fix Code

↓

Test Fix

↓

Deploy
```

Never fix a bug without first reproducing it.

---

# Types of Bugs

Common categories

- Syntax errors
- Runtime errors
- Logical errors
- Concurrency bugs
- Performance issues
- Memory leaks

---

# Syntax Errors

Detected before execution.

Example

```python
if True
    print("Hello")
```

Output

```
SyntaxError
```

---

# Runtime Errors

Occur during execution.

Example

```python
10 / 0
```

Output

```
ZeroDivisionError
```

---

# Logical Errors

Program runs but produces incorrect results.

Example

```python
def area(length, width):
    return length + width
```

No exception occurs, but the logic is incorrect.

---

# Reading a Stack Trace

Example

```python
def divide(a, b):
    return a / b

divide(10, 0)
```

Typical traceback

```text
Traceback (most recent call last):
  File "app.py", line 4, in <module>
    divide(10, 0)
  File "app.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
```

Read the traceback from **bottom to top** to locate the root exception.

---

# Common Python Exceptions

| Exception | Cause |
|-----------|-------|
| TypeError | Wrong data type |
| ValueError | Invalid value |
| KeyError | Missing dictionary key |
| IndexError | Invalid list index |
| AttributeError | Missing attribute |
| FileNotFoundError | Missing file |
| ZeroDivisionError | Division by zero |
| ImportError | Import failed |
| ModuleNotFoundError | Module not installed |
| PermissionError | Access denied |

---

# Print Debugging

Simplest debugging method.

```python
print(variable)
```

Advantages

- Easy
- Quick

Disadvantages

- Pollutes code
- Difficult to maintain
- Not suitable for production

---

# Using pprint

Pretty-print complex objects.

```python
from pprint import pprint

pprint(data)
```

Useful for dictionaries and nested structures.

---

# Assertions for Debugging

```python
assert age >= 0
```

If the condition fails

```
AssertionError
```

Assertions help detect invalid program states during development.

---

# Python Debugger (pdb)

Built-in interactive debugger.

```python
import pdb

pdb.set_trace()
```

Execution pauses at that line.

---

# Running with pdb

```bash
python -m pdb app.py
```

---

# Common pdb Commands

| Command | Purpose |
|---------|---------|
| n | Next line |
| s | Step into function |
| c | Continue execution |
| l | List source code |
| p variable | Print variable |
| q | Quit debugger |
| w | Show stack trace |
| b | Set breakpoint |

---

# Example

```python
import pdb

x = 10

pdb.set_trace()

y = x + 5
```

At the debugger prompt

```
(Pdb)
```

You can inspect variables before continuing.

---

# Breakpoints

A breakpoint pauses execution at a specific line.

```
Program

↓

Breakpoint

↓

Inspect Variables

↓

Continue
```

Supported by most IDEs and debuggers.

---

# IDE Debugging

Modern IDEs provide graphical debuggers.

Features

- Breakpoints
- Variable inspection
- Call stack
- Watches
- Step execution

Popular IDEs

- VS Code
- PyCharm

---

# Step Operations

Step Into

```
Enter function
```

Step Over

```
Execute current line
```

Step Out

```
Return from current function
```

Continue

```
Run until next breakpoint
```

---

# Variable Inspection

During debugging you can inspect

- Local variables
- Global variables
- Object attributes
- Function arguments

This helps verify program state.

---

# Logging

Logging records application events for debugging and monitoring.

Unlike `print()`, logging supports levels, formatting, and multiple outputs.

---

# Why Logging?

Benefits

✓ Persistent records

✓ Configurable output

✓ Severity levels

✓ File logging

✓ Production monitoring

✓ Easier troubleshooting

---

# Logging Module

```python
import logging
```

Basic example

```python
logging.warning("Low disk space")
```

---

# Basic Configuration

```python
import logging

logging.basicConfig(

    level=logging.INFO
)
```

---

# Log Levels

| Level | Purpose |
|-------|----------|
| DEBUG | Detailed diagnostic information |
| INFO | Normal application events |
| WARNING | Unexpected but recoverable situations |
| ERROR | Operation failed |
| CRITICAL | Serious failure requiring immediate attention |

---

# Example

```python
logging.debug("Debug message")

logging.info("Application started")

logging.warning("Disk almost full")

logging.error("Database unavailable")

logging.critical("System failure")
```

---

# Log Level Hierarchy

```
DEBUG

↓

INFO

↓

WARNING

↓

ERROR

↓

CRITICAL
```

Higher configured levels suppress lower-severity messages.

---

# Log Formatting

```python
logging.basicConfig(

    format="%(asctime)s %(levelname)s %(message)s"
)
```

Common fields

- asctime
- levelname
- message
- filename
- funcName
- lineno

---

# Logging to a File

```python
logging.basicConfig(

    filename="app.log",

    level=logging.INFO
)
```

Logs are written to `app.log`.

---

# Creating a Logger

```python
logger = logging.getLogger(__name__)
```

Recommended for libraries and larger applications.

---

# Using a Logger

```python
logger.info("Application started")
```

Avoid using the root logger throughout a large project.

---

# Handlers

Handlers determine where log messages are written.

Examples

- Console
- File
- Syslog
- HTTP
- Email

Architecture

```
Logger

↓

Handler

↓

Destination
```

---

# FileHandler

```python
handler = logging.FileHandler(

    "app.log"
)
```

---

# RotatingFileHandler

Automatically rotates log files.

```python
from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler(

    "app.log",

    maxBytes=1_000_000,

    backupCount=5
)
```

Prevents unlimited log growth.

---

# Formatters

Customize log appearance.

```python
formatter = logging.Formatter(

    "%(levelname)s: %(message)s"
)
```

Attach to handlers.

---

# Exception Logging

```python
try:

    10 / 0

except Exception:

    logger.exception(

        "Unexpected error"
    )
```

`logger.exception()` includes the stack trace automatically.

---

# Structured Logging

Instead of

```
User logged in
```

Prefer structured information

```
user_id=42 action=login status=success
```

Structured logs are easier to search and analyze.

---

# Sensitive Data

Never log

- Passwords
- API keys
- Authentication tokens
- Credit card numbers
- Personal identification numbers

Mask or omit sensitive information.

---

# Logging Best Practices

✓ Use appropriate log levels.

✓ Include useful context.

✓ Log exceptions with stack traces.

✓ Rotate log files.

✓ Use module-specific loggers.

✓ Avoid duplicate logging.

✓ Keep messages clear and actionable.

---

# Common Debugging Mistakes

❌ Ignoring stack traces.

❌ Swallowing exceptions silently.

❌ Using `print()` in production.

❌ Logging sensitive information.

❌ Writing vague log messages.

❌ Catching `Exception` everywhere without handling it properly.

---

# Common Logging Mistakes

❌ Logging everything as `ERROR`.

❌ Logging excessively inside tight loops.

❌ Creating multiple root logger configurations.

❌ Using inconsistent log formats.

❌ Forgetting timestamps.

---

# Interview Questions

### Easy

1. What is debugging?
2. What is a stack trace?
3. What is `pdb`?
4. Why use logging instead of `print()`?
5. Name the standard logging levels.

---

### Medium

1. Explain how to debug a failing application.
2. Compare breakpoints and print debugging.
3. What is `logger.exception()`?
4. Why use rotating log files?
5. How would you investigate an intermittent production bug?

---

### Hard

1. Design a logging strategy for a distributed microservices system.
2. Explain structured logging and its benefits.
3. Build a debugging workflow for a high-traffic API.
4. Compare local debugging with production debugging.
5. Design a centralized logging architecture.

---

# Coding Exercises

Easy

- Configure basic logging.
- Log messages at different severity levels.
- Use `pdb` to inspect variables.

Medium

- Create module-specific loggers.
- Write logs to rotating files.
- Log exceptions with stack traces.

Hard

- Implement structured logging for a REST API.
- Build a centralized logging configuration.
- Debug and resolve a multithreaded application issue.

---

# Module Summary

Debugging is the systematic process of locating and fixing defects, while logging provides a permanent record of application behavior for troubleshooting and monitoring. Python offers tools such as `pdb` for interactive debugging and the `logging` module for configurable, production-ready logging. Using appropriate log levels, structured messages, exception logging, and rotating log files helps developers diagnose issues efficiently while maintaining secure and maintainable applications.

---

# Python Developer Knowledge Base
# Module 09 — Testing and Debugging
# Part 6 (Final) — Code Coverage, Static Analysis & CI/CD

---

# Why Code Quality Matters

High-quality code is

- Reliable
- Maintainable
- Readable
- Testable
- Secure
- Easy to extend

Testing alone is not enough.

Combine

- Testing
- Static Analysis
- Code Review
- Continuous Integration

---

# Code Coverage

Code coverage measures how much of your code is executed during testing.

Example

```
Application

↓

Tests

↓

Coverage Report
```

Coverage indicates tested code, not necessarily correct code.

---

# Types of Coverage

- Line Coverage
- Statement Coverage
- Branch Coverage
- Function Coverage
- Path Coverage

---

# Line Coverage

Measures executed lines.

Example

```python
if age >= 18:
    print("Adult")
```

If only the true branch executes, line coverage may appear complete even though the false branch is untested.

---

# Branch Coverage

Ensures all decision branches are tested.

```
if condition

├── True Branch

└── False Branch
```

Branch coverage is generally more informative than line coverage.

---

# coverage.py

Most popular Python coverage tool.

Install

```bash
pip install coverage
```

Run tests

```bash
coverage run -m pytest
```

Generate report

```bash
coverage report
```

HTML report

```bash
coverage html
```

Open

```
htmlcov/index.html
```

---

# Example Coverage Report

```
Name              Stmts   Miss  Cover

app.py              50      2     96%

utils.py            80      5     94%
```

Investigate uncovered lines and determine whether additional tests are needed.

---

# Code Quality Tools

Popular tools

- Ruff
- Flake8
- Pylint
- MyPy
- Black
- isort
- Bandit

Each addresses a different aspect of code quality.

---

# Ruff

Modern, high-performance linter.

Install

```bash
pip install ruff
```

Run

```bash
ruff check .
```

Advantages

- Very fast
- Replaces many Flake8 plugins
- Can automatically fix many issues

---

# Flake8

Detects

- Style issues
- Syntax issues
- Unused imports
- Complexity warnings

Install

```bash
pip install flake8
```

Run

```bash
flake8 .
```

---

# Pylint

Performs deeper code analysis.

Install

```bash
pip install pylint
```

Run

```bash
pylint app.py
```

Checks

- Code quality
- Naming
- Design issues
- Potential bugs

---

# Ruff vs Flake8 vs Pylint

| Tool | Strength |
|------|----------|
| Ruff | Fast linting and auto-fixes |
| Flake8 | Style and basic checks |
| Pylint | Deep static analysis |

Many modern teams use Ruff as their primary linter.

---

# MyPy

Static type checker.

Install

```bash
pip install mypy
```

Example

```python
def add(a: int, b: int) -> int:
    return a + b
```

Run

```bash
mypy .
```

Helps detect type-related issues before runtime.

---

# Black

Automatic code formatter.

Install

```bash
pip install black
```

Format project

```bash
black .
```

Benefits

- Consistent formatting
- Reduced style debates
- Easy code reviews

---

# isort

Automatically sorts imports.

Install

```bash
pip install isort
```

Run

```bash
isort .
```

Example

Before

```python
import os
import requests
import sys
```

After

```python
import os
import sys

import requests
```

---

# Bandit

Security-focused static analyzer.

Install

```bash
pip install bandit
```

Run

```bash
bandit -r .
```

Detects

- Hardcoded passwords
- Unsafe function usage
- Insecure configurations

---

# Continuous Integration (CI)

CI automatically validates code changes.

Typical pipeline

```
Developer

↓

Git Push

↓

CI Pipeline

↓

Tests

↓

Lint

↓

Coverage

↓

Build

↓

Deploy
```

---

# CI Benefits

✓ Early bug detection

✓ Consistent quality

✓ Automatic testing

✓ Safer deployments

✓ Faster feedback

---

# GitHub Actions

Example workflow

```yaml
name: Python CI

on:
  push:
  pull_request:

jobs:

  test:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5

        with:
          python-version: "3.12"

      - run: pip install -r requirements.txt

      - run: pytest
```

---

# Typical CI Pipeline

```
Checkout Code

↓

Install Dependencies

↓

Lint

↓

Run Tests

↓

Coverage

↓

Build

↓

Deploy
```

---

# Pre-Commit Hooks

Run checks before allowing commits.

Popular checks

- Ruff
- Black
- isort
- MyPy
- Pytest

Prevents many issues from reaching the repository.

---

# Testing Strategy

```
Unit Tests

↓

Integration Tests

↓

API Tests

↓

End-to-End Tests

↓

Production Monitoring
```

Different test levels complement each other.

---

# Testing Checklist

Before merging code

✓ Tests pass

✓ Lint passes

✓ Type checking passes

✓ Coverage acceptable

✓ Documentation updated

✓ Code reviewed

---

# Production Debugging

Recommended workflow

```
Logs

↓

Metrics

↓

Tracing

↓

Root Cause Analysis

↓

Fix

↓

Regression Test
```

---

# Monitoring

Track

- Error rate
- Response time
- CPU
- Memory
- Throughput
- Database latency
- Queue depth

Useful observability tools

- Prometheus
- Grafana
- OpenTelemetry

---

# Real-World Project Structure

```
project/

│

├── app/

├── tests/

│   ├── unit/

│   ├── integration/

│   ├── e2e/

│   └── conftest.py

├── .github/

│   └── workflows/

├── pyproject.toml

├── pytest.ini

├── requirements.txt

└── README.md
```

---

# Best Practices

✓ Write tests for every new feature.

✓ Keep tests independent.

✓ Test edge cases.

✓ Measure code coverage.

✓ Use static analysis tools.

✓ Format code automatically.

✓ Integrate tests into CI.

✓ Monitor production systems.

---

# Common Mistakes

❌ Chasing 100% coverage without meaningful tests.

❌ Ignoring linter warnings.

❌ Skipping CI for "small" changes.

❌ Mixing unit and integration tests.

❌ Committing unformatted code.

❌ Depending on production services during unit tests.

---

# Python Testing Ecosystem

| Tool | Purpose |
|------|---------|
| unittest | Built-in testing framework |
| pytest | Modern testing framework |
| coverage.py | Code coverage |
| Ruff | Fast linting |
| Flake8 | Style checking |
| Pylint | Static analysis |
| MyPy | Type checking |
| Black | Formatting |
| isort | Import sorting |
| Bandit | Security analysis |

---

# Complete Development Workflow

```
Write Code

↓

Run Ruff

↓

Run Black

↓

Run MyPy

↓

Run Pytest

↓

Check Coverage

↓

Commit

↓

Push

↓

CI Pipeline

↓

Deploy
```

---

# Interview Questions

### Easy

1. What is code coverage?
2. Why use Black?
3. What is MyPy?
4. What is static analysis?
5. What is CI?

---

### Medium

1. Compare Ruff, Flake8, and Pylint.
2. Explain branch coverage.
3. How does GitHub Actions support CI?
4. Why use pre-commit hooks?
5. What should a production testing strategy include?

---

### Hard

1. Design a complete CI/CD pipeline for a Python backend.
2. Build a testing strategy for a microservices application.
3. Compare runtime testing and static analysis.
4. Explain how to balance coverage goals with test quality.
5. Design a quality gate for enterprise Python projects.

---

# Coding Exercises

Easy

- Generate a coverage report with `coverage.py`.
- Format a project with Black.
- Sort imports with isort.

Medium

- Configure Ruff and MyPy.
- Create a GitHub Actions workflow.
- Add Bandit security checks.

Hard

- Build a complete CI pipeline for a Python application.
- Configure pre-commit hooks with linting, formatting, and testing.
- Create a production-ready quality assurance workflow.

---

# Module Summary

High-quality Python software requires more than passing tests. Code coverage helps identify untested areas, while static analysis tools such as Ruff, Pylint, MyPy, and Bandit detect style, type, and security issues before runtime. Automated formatting with Black and isort ensures consistency, and CI pipelines enforce quality checks on every code change. Together, testing, static analysis, formatting, and continuous integration form a robust, production-ready software development workflow.

---

