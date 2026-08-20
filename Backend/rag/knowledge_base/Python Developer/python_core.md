# Python Developer Knowledge Base
# Module 02 — Python Core

---

# 1. Introduction

Python is a high-level, interpreted, object-oriented, dynamically typed programming language. It is one of the most widely used languages due to its readability, simplicity, and rich ecosystem.

A strong understanding of Python Core is essential for backend development, automation, data science, AI/ML, DevOps, and scripting.

---

# 2. Python Architecture

## Overview

Python source code is not directly executed by the operating system.

Instead, it follows the execution pipeline:

```
Python Source Code (.py)

↓

Lexical Analysis

↓

Parser

↓

Abstract Syntax Tree (AST)

↓

Compiler

↓

Bytecode (.pyc)

↓

Python Virtual Machine (PVM)

↓

Operating System

↓

CPU
```

### Components

### 1. Source Code

The `.py` file written by the developer.

Example:

```python
print("Hello World")
```

---

### 2. Lexer (Tokenizer)

The lexer converts characters into **tokens**.

Example:

```python
x = 10
```

Tokens:

- Identifier → `x`
- Operator → `=`
- Integer → `10`

---

### 3. Parser

The parser checks whether the syntax is valid.

Correct:

```python
x = 10
```

Incorrect:

```python
if:
```

Produces:

```
SyntaxError
```

---

### 4. AST (Abstract Syntax Tree)

Python converts code into an internal tree representation.

Example:

```python
x = a + b
```

AST:

```
Assignment

├── Variable x

└── Addition

     ├── a

     └── b
```

---

### 5. Compiler

The compiler converts the AST into **Bytecode**.

Bytecode is platform independent.

Example file:

```
__pycache__/

main.cpython-312.pyc
```

---

### 6. Python Virtual Machine

The PVM reads bytecode instruction by instruction.

The operating system executes the instructions.

---

# 3. Installing Python

Official Website

https://python.org

Verify installation

```bash
python --version
```

or

```bash
python3 --version
```

---

# 4. Python Interactive Shell

Start the shell

```bash
python
```

Example

```python
>>> 10 + 20

30
```

Useful for

- Testing code
- Learning Python
- Debugging expressions

---

# 5. Variables

## Definition

A variable is a name that refers to an object stored in memory.

Example

```python
age = 25

name = "Alice"

salary = 50000
```

Variables in Python are references, not memory containers.

---

## Naming Rules

Valid

```python
user_name

employee1

total_salary
```

Invalid

```python
1name

user-name

class
```

---

## Naming Conventions

Use snake_case

Example

```python
student_name

employee_salary

total_marks
```

Constants

```python
PI = 3.14159

MAX_CONNECTIONS = 100
```

Private variables

```python
_internal
```

---

# 6. Memory Model

Python stores **objects** in memory.

Variables point to those objects.

Example

```python
a = 10

b = a
```

```
a ──┐

    │

    ▼

   10

    ▲

    │

b ──┘
```

Both variables reference the same integer object.

---

## Object Identity

Use

```python
id()
```

Example

```python
x = 100

y = x

print(id(x))

print(id(y))
```

Output

```
Same memory address
```

---

## Mutable vs Immutable

Immutable

- int
- float
- bool
- string
- tuple

Mutable

- list
- dictionary
- set

Example

```python
x = [1,2]

y = x

y.append(3)

print(x)
```

Output

```python
[1,2,3]
```

---

# 7. Comments

Single line

```python
# This is a comment
```

Multi-line

```python
"""
Documentation
"""
```

Use comments to explain *why*, not *what*.

---

# 8. Input and Output

Output

```python
print("Hello")
```

Multiple values

```python
name = "Alice"

age = 22

print(name, age)
```

Formatted strings

```python
print(f"{name} is {age} years old")
```

Input

```python
name = input("Enter name: ")
```

Input always returns a string.

Convert types when required.

```python
age = int(input("Age: "))
```

---

# 9. Python Data Types

## Numeric

```python
int

float

complex
```

Example

```python
x = 10

y = 5.5

z = 2 + 3j
```

---

## Boolean

```python
True

False
```

---

## String

```python
name = "Python"
```

Supports indexing, slicing, and many built-in methods.

---

## List

Ordered, mutable.

```python
numbers = [1,2,3]
```

---

## Tuple

Ordered, immutable.

```python
point = (10,20)
```

---

## Set

Unordered collection of unique values.

```python
items = {1,2,3}
```

---

## Dictionary

Key-value mapping.

```python
student = {

    "name":"Alice",

    "age":22

}
```

---

# 10. Type Conversion

Implicit

```python
5 + 5.5
```

Result

```
10.5
```

Explicit

```python
int("25")

float("4.5")

str(100)

list("abc")
```

---

# 11. Best Practices

- Use meaningful variable names.
- Avoid single-letter names except for loop counters.
- Keep functions small and focused.
- Follow PEP 8 naming conventions.
- Use f-strings for formatting.
- Prefer explicit type conversion.
- Avoid unnecessary global variables.

---

# 12. Common Interview Questions

### Easy

1. What is Python?
2. Is Python compiled or interpreted?
3. What is bytecode?
4. What is the Python Virtual Machine?
5. Difference between mutable and immutable objects?

### Medium

1. Explain Python's execution process.
2. What is object identity?
3. Explain `id()` and `is`.
4. Difference between `==` and `is`.
5. Why are strings immutable?

### Hard

1. Explain CPython architecture.
2. How does Python manage memory?
3. What are reference counts?
4. Explain garbage collection.
5. How does Python optimize small integers?

---

# Summary

This section introduced Python's architecture, execution model, variables, memory model, comments, input/output, and core data types. These concepts form the foundation for writing reliable and efficient Python programs.

---

# 13. Python Operators

Operators are special symbols used to perform operations on variables and values.

Python provides the following categories of operators:

- Arithmetic Operators
- Comparison Operators
- Assignment Operators
- Logical Operators
- Bitwise Operators
- Identity Operators
- Membership Operators

---

# 13.1 Arithmetic Operators

Used to perform mathematical calculations.

| Operator | Description | Example |
|----------|-------------|---------|
| + | Addition | a + b |
| - | Subtraction | a - b |
| * | Multiplication | a * b |
| / | Division | a / b |
| // | Floor Division | a // b |
| % | Modulus | a % b |
| ** | Exponent | a ** b |

Example

```python
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

Output

```
19
11
60
3.75
3
3
50625
```

---

# 13.2 Comparison Operators

Comparison operators return Boolean values.

| Operator | Meaning |
|----------|---------|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |

Example

```python
age = 20

print(age >= 18)
```

Output

```
True
```

---

# 13.3 Assignment Operators

Used for assigning values.

Example

```python
x = 10

x += 5

x -= 2

x *= 3

x /= 2
```

Supported operators

```
=
+=
-=
*=
/=
//=
%=
**=
&=
|=
^=
>>=
<<=
```

---

# 13.4 Logical Operators

| Operator | Meaning |
|----------|---------|
| and | Logical AND |
| or | Logical OR |
| not | Logical NOT |

Example

```python
age = 25
salary = 50000

print(age > 18 and salary > 30000)
```

Output

```
True
```

Example

```python
print(True or False)
```

Output

```
True
```

Example

```python
print(not True)
```

Output

```
False
```

---

# 13.5 Identity Operators

Identity operators compare object identities rather than values.

| Operator | Description |
|----------|-------------|
| is | Same object |
| is not | Different object |

Example

```python
a = [1,2]

b = a

print(a is b)
```

Output

```
True
```

Example

```python
a = [1,2]

b = [1,2]

print(a == b)
print(a is b)
```

Output

```
True
False
```

---

# 13.6 Membership Operators

Used to test whether an element exists in a sequence.

Operators

```
in
not in
```

Example

```python
numbers = [10,20,30]

print(20 in numbers)
```

Output

```
True
```

Example

```python
print(100 not in numbers)
```

Output

```
True
```

---

# 13.7 Bitwise Operators

Operate on binary values.

| Operator | Description |
|----------|-------------|
| & | AND |
| \| | OR |
| ^ | XOR |
| ~ | NOT |
| << | Left Shift |
| >> | Right Shift |

Example

```python
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b)
```

---

# 14. Operator Precedence

Python evaluates expressions based on precedence.

Highest to Lowest

```
()
**
+x -x
*, /, //, %
+, -
<< >>
&
^
|
Comparison
not
and
or
Assignment
```

Example

```python
print(2 + 3 * 4)
```

Output

```
14
```

Example

```python
print((2 + 3) * 4)
```

Output

```
20
```

---

# 15. Conditional Statements

Conditional statements execute code based on Boolean expressions.

---

## if Statement

Example

```python
age = 20

if age >= 18:
    print("Eligible")
```

---

## if...else

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## if...elif...else

```python
marks = 82

if marks >= 90:
    grade = "A"

elif marks >= 75:
    grade = "B"

elif marks >= 60:
    grade = "C"

else:
    grade = "D"

print(grade)
```

---

## Nested if

```python
age = 25
citizen = True

if age >= 18:

    if citizen:

        print("Eligible")
```

---

# 16. Match Statement (Python 3.10+)

Used for structural pattern matching.

Example

```python
status = 200

match status:

    case 200:
        print("Success")

    case 404:
        print("Not Found")

    case _:
        print("Unknown")
```

Advantages

- Cleaner than long if-elif chains
- Better readability
- Useful for command processing

---

# 17. Loops

Python supports

- for loop
- while loop

---

## for Loop

Example

```python
for i in range(5):

    print(i)
```

Output

```
0
1
2
3
4
```

---

## Iterating Through a List

```python
fruits = ["Apple","Mango","Orange"]

for fruit in fruits:

    print(fruit)
```

---

## while Loop

```python
count = 1

while count <= 5:

    print(count)

    count += 1
```

---

# Infinite Loop

```python
while True:

    print("Running")
```

Always provide an exit condition unless intentionally creating a long-running service.

---

# 18. Loop Control Statements

## break

Stops loop execution.

```python
for i in range(10):

    if i == 5:

        break

    print(i)
```

---

## continue

Skips current iteration.

```python
for i in range(6):

    if i == 3:

        continue

    print(i)
```

---

## pass

Placeholder statement.

```python
if True:

    pass
```

Useful while designing program structure.

---

# 19. Loop else

The else block executes only if the loop completes normally.

Example

```python
for i in range(5):

    print(i)

else:

    print("Completed")
```

If break executes, else does not execute.

---

# 20. Nested Loops

Example

```python
for row in range(3):

    for col in range(3):

        print(row, col)
```

Applications

- Matrix traversal
- Pattern printing
- Graph algorithms

---

# 21. List Comprehensions

Provides a concise way to create lists.

Example

```python
numbers = [x*x for x in range(5)]
```

Output

```python
[0,1,4,9,16]
```

With condition

```python
even = [x for x in range(10) if x % 2 == 0]
```

Advantages

- Concise
- Faster than explicit loops
- Readable for simple transformations

Avoid overly complex comprehensions.

---

# 22. Generator Expressions

Similar to list comprehensions but produce values lazily.

Example

```python
squares = (x*x for x in range(1000000))
```

Advantages

- Lower memory usage
- Suitable for large datasets
- Iterates on demand

---

# 23. Best Practices

- Use meaningful condition names.
- Avoid deeply nested if statements.
- Prefer match for multiple fixed cases.
- Keep loops simple.
- Use comprehensions only when readability is maintained.
- Prefer generators for large datasets.
- Avoid unnecessary infinite loops.
- Use break and continue sparingly.

---

# 24. Common Interview Questions

### Easy

1. Difference between `=` and `==`.
2. Difference between `/` and `//`.
3. What does `%` return?
4. Difference between `is` and `==`.
5. What is the `in` operator?

### Medium

1. Explain operator precedence.
2. Difference between `break` and `continue`.
3. Explain loop `else`.
4. What are list comprehensions?
5. Difference between list comprehensions and generators.

### Hard

1. How does Python evaluate chained comparisons?
2. Explain short-circuit evaluation in `and` and `or`.
3. When should generator expressions be preferred over lists?
4. How does `match` differ from `if...elif` internally?
5. Discuss performance implications of nested loops.

---

# 25. Practical Scenarios

### Scenario 1

Filter valid email addresses from a list while skipping invalid entries.

Expected Concepts

- for loop
- continue
- condition checking
- string methods

---

### Scenario 2

Process a large log file line by line.

Expected Concepts

- generator expressions
- loops
- memory efficiency

---

### Scenario 3

Implement a menu-driven application.

Expected Concepts

- match statement
- loops
- break
- functions

---

# Summary

This section covered Python operators, conditional statements, loops, comprehensions, generator expressions, and loop control statements. Mastery of these constructs is essential for writing efficient, readable, and maintainable Python code and forms the basis for solving algorithmic and real-world programming problems.


---

# 26. Functions

## Definition

A function is a reusable block of code designed to perform a specific task.

Functions improve:

- Code reusability
- Maintainability
- Readability
- Testing
- Modular programming

---

## Why Functions are Important

Without functions

```python
print((10 + 20) * 5)

print((30 + 40) * 5)

print((50 + 60) * 5)
```

Lots of duplicate code.

With functions

```python
def calculate(a, b):
    return (a + b) * 5

print(calculate(10,20))
print(calculate(30,40))
print(calculate(50,60))
```

Advantages

- Less duplication
- Easier debugging
- Reusable
- Cleaner architecture

---

# Function Syntax

```python
def function_name(parameters):
    """
    Docstring
    """
    statement
    return value
```

Example

```python
def greet():

    print("Hello")
```

Calling

```python
greet()
```

Output

```
Hello
```

---

# Function Components

```
def

↓

Function Name

↓

Parameters

↓

Function Body

↓

Return Statement
```

Example

```python
def add(a, b):

    result = a + b

    return result
```

---

# Function Execution Flow

```
Function Call

↓

Arguments Created

↓

Local Namespace Created

↓

Statements Execute

↓

Return Statement

↓

Local Namespace Destroyed

↓

Returned Value
```

---

# Creating Functions

Example

```python
def square(number):

    return number ** 2
```

Calling

```python
answer = square(8)

print(answer)
```

Output

```
64
```

---

# Parameters vs Arguments

Parameter

Variable inside function definition.

```python
def greet(name):
```

"name" is parameter.

Argument

Actual value passed.

```python
greet("Alice")
```

"Alice" is argument.

---

# Types of Parameters

Python supports

- Positional
- Keyword
- Default
- Variable Length
- Keyword Variable Length
- Positional Only
- Keyword Only

---

# Positional Arguments

Arguments are matched by position.

```python
def subtract(a, b):

    return a - b

print(subtract(10,5))
```

Output

```
5
```

---

# Keyword Arguments

Arguments specified using parameter names.

```python
def employee(name, age):

    print(name)

    print(age)

employee(age=25, name="John")
```

Advantages

- Order independent
- More readable

---

# Default Parameters

```python
def greet(name="Guest"):

    print(name)
```

Calling

```python
greet()
```

Output

```
Guest
```

Calling

```python
greet("Alice")
```

Output

```
Alice
```

---

# Variable Length Arguments (*args)

Accepts multiple positional arguments.

```python
def total(*numbers):

    print(numbers)
```

Calling

```python
total(10,20,30,40)
```

Output

```
(10,20,30,40)
```

Summation

```python
def total(*numbers):

    return sum(numbers)
```

---

# Keyword Variable Arguments (**kwargs)

Accepts unlimited keyword arguments.

```python
def profile(**details):

    print(details)
```

Calling

```python
profile(
    name="Alice",
    city="Pune",
    age=22
)
```

Output

```python
{
'name':'Alice',
'city':'Pune',
'age':22
}
```

---

# Combining Parameters

```python
def demo(a, b=5, *args, **kwargs):

    pass
```

Order

```
Positional

↓

Default

↓

*args

↓

**kwargs
```

---

# Return Statement

Returns value to caller.

```python
def cube(x):

    return x*x*x
```

Without return

```python
def hello():

    print("Hello")
```

Returns

```
None
```

Example

```python
result = hello()

print(result)
```

Output

```
Hello

None
```

---

# Returning Multiple Values

Python returns tuples.

```python
def calculate(a,b):

    return a+b, a-b
```

Calling

```python
sum_value, diff = calculate(10,5)
```

Output

```
15

5
```

---

# Scope

Variables exist within specific scopes.

Python follows LEGB Rule.

```
L

Local

↓

E

Enclosing

↓

G

Global

↓

B

Built-in
```

---

# Local Variables

```python
def demo():

    x = 10

    print(x)
```

Accessible only inside function.

---

# Global Variables

```python
x = 100

def demo():

    print(x)
```

Output

```
100
```

---

# global Keyword

Modify global variable.

```python
count = 0

def increment():

    global count

    count += 1
```

---

# nonlocal Keyword

Used inside nested functions.

```python
def outer():

    count = 0

    def inner():

        nonlocal count

        count += 1

    inner()

    print(count)

outer()
```

Output

```
1
```

---

# Nested Functions

Functions inside functions.

```python
def outer():

    def inner():

        print("Inner")

    inner()
```

Applications

- Closures
- Decorators
- Encapsulation

---

# Anonymous Functions (lambda)

Syntax

```python
lambda parameters: expression
```

Example

```python
square = lambda x: x*x

print(square(5))
```

Output

```
25
```

Multiple arguments

```python
multiply = lambda x,y:x*y
```

Sorting

```python
students = [

("Alice",90),

("Bob",80),

("John",95)

]

students.sort(
key=lambda x:x[1]
)
```

---

# Recursion

Function calling itself.

```python
def factorial(n):

    if n==1:

        return 1

    return n*factorial(n-1)
```

Output

```
factorial(5)

120
```

Advantages

- Elegant
- Tree traversal
- Divide & Conquer

Disadvantages

- Stack usage
- Slower
- Recursion limit

---

# Docstrings

Documentation inside functions.

```python
def add(a,b):

    """
    Returns sum of two numbers.
    """

    return a+b
```

Read

```python
help(add)
```

---

# Type Hints

Example

```python
def add(a:int,b:int)->int:

    return a+b
```

Advantages

- Better readability

- IDE support

- Static analysis

---

# Function Annotations

```python
def greet(name:str)->str:

    return "Hello "+name
```

Annotations

```python
print(greet.__annotations__)
```

Output

```python
{
'name':str,

'return':str
}
```

---

# Best Practices

- One function should perform one task.
- Keep functions short.
- Use meaningful names.
- Document public functions.
- Avoid global variables.
- Prefer return values over print().
- Use type hints.
- Avoid deeply nested functions.

---

# Common Mistakes

❌ Large functions

❌ Too many parameters

❌ Using global everywhere

❌ Missing return

❌ Duplicate logic

❌ No documentation

---

# Interview Questions

Easy

1. What is a function?
2. Difference between parameter and argument.
3. What does return do?
4. What happens if return is omitted?
5. Difference between local and global variables.

Medium

1. Explain LEGB Rule.
2. Difference between *args and **kwargs.
3. What is recursion?
4. Explain lambda functions.
5. Difference between return and print.

Hard

1. How does Python create function objects?
2. Explain function namespaces.
3. How are default parameters stored?
4. Why are mutable default arguments dangerous?
5. Explain closures and free variables.

---

# Coding Exercises

Easy

- Reverse a string using a function.
- Find maximum of three numbers.
- Check palindrome.
- Find factorial.

Medium

- Fibonacci using recursion.
- Calculator using functions.
- Student grade calculator.
- Prime number checker.

Hard

- Implement memoized Fibonacci.
- Build recursive directory traversal.
- Implement custom map() function.
- Create function decorators manually.

---

# Practical Scenario

Scenario 1

Design reusable validation functions for a FastAPI application.

Expected Discussion

- Separation of concerns
- Reusable validation
- Exception handling
- Unit testing

---

Scenario 2

Create a payroll calculation module.

Expected Discussion

- Small reusable functions
- Type hints
- Modular design
- Testing strategy

---

# Summary

Functions are the foundation of modular programming in Python. Understanding parameters, arguments, scope, recursion, lambda expressions, and type hints enables developers to write reusable, maintainable, and testable code. Mastery of functions is essential for backend frameworks such as FastAPI and Django and is a core topic in Python technical interviews.


---

# 27. Modules

## Definition

A module is a Python file (`.py`) that contains reusable code such as variables, functions, classes, and constants.

Modules help organize code into logical units, making applications easier to maintain and scale.

Example

```
calculator.py
```

```python
PI = 3.14159

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

Using the module

```python
import calculator

print(calculator.add(10, 20))
print(calculator.PI)
```

Output

```
30
3.14159
```

---

# Why Modules?

Without modules:

```
main.py
-------------------
5000+ lines of code
```

Problems

- Difficult to maintain
- Difficult to debug
- Difficult to test
- Poor readability

With modules

```
project/

database.py

models.py

api.py

services.py

utils.py

config.py
```

Advantages

- Reusability
- Separation of concerns
- Better testing
- Better collaboration
- Easier maintenance

---

# Module Search Path

When Python executes

```python
import math
```

Python searches in this order

1. Current directory
2. PYTHONPATH
3. Standard Library
4. site-packages

View search path

```python
import sys

print(sys.path)
```

---

# Import Statement

Basic import

```python
import math

print(math.sqrt(25))
```

Output

```
5.0
```

---

# Import Specific Functions

```python
from math import sqrt

print(sqrt(16))
```

---

# Import Multiple Objects

```python
from math import sqrt, factorial
```

---

# Import with Alias

```python
import numpy as np

array = np.array([1,2,3])
```

Another example

```python
import pandas as pd
```

Benefits

- Shorter names
- Cleaner code
- Industry standard

---

# Wildcard Import

```python
from math import *
```

Avoid this.

Problems

- Namespace pollution
- Hard to debug
- Lower readability

Preferred

```python
from math import sqrt
```

---

# Reloading Modules

Python loads a module only once.

To reload

```python
import importlib

import calculator

importlib.reload(calculator)
```

Useful during development.

---

# Built-in Modules

Python Standard Library includes hundreds of modules.

Examples

```
math

random

os

sys

datetime

json

collections

itertools

functools

pathlib

statistics

logging

threading

asyncio

sqlite3

re

csv

typing
```

---

# math Module

Example

```python
import math

print(math.pi)

print(math.sqrt(81))

print(math.factorial(6))
```

---

# random Module

Example

```python
import random

print(random.randint(1,10))

print(random.choice(["A","B","C"]))
```

---

# os Module

Interact with operating system.

```python
import os

print(os.getcwd())

print(os.listdir())
```

Create directory

```python
os.mkdir("Demo")
```

---

# sys Module

Access interpreter information.

```python
import sys

print(sys.version)

print(sys.platform)

print(sys.argv)
```

---

# datetime Module

```python
from datetime import datetime

print(datetime.now())
```

Current date

```python
from datetime import date

print(date.today())
```

---

# json Module

Convert between JSON and Python objects.

Dictionary → JSON

```python
import json

person = {

"name":"Alice",

"age":22

}

print(json.dumps(person))
```

JSON → Dictionary

```python
data = '{"name":"John"}'

print(json.loads(data))
```

---

# pathlib Module

Preferred over os.path

```python
from pathlib import Path

file = Path("data.txt")

print(file.exists())
```

---

# Packages

A package is a directory containing multiple modules.

Example

```
project/

employees/

    __init__.py

    payroll.py

    attendance.py

    leave.py
```

Import

```python
from employees import payroll
```

---

# __init__.py

Marks directory as package.

Can contain

- initialization code
- package metadata
- exports

Example

```python
from .payroll import *

from .attendance import *
```

---

# Relative Import

Example

```python
from .database import connect
```

---

# Absolute Import

Example

```python
from project.database.connection import connect
```

Preferred in larger projects.

---

# __name__ Variable

Every module has

```python
__name__
```

If file executed directly

```
__main__
```

Example

```python
print(__name__)
```

---

# __name__ == "__main__"

```python
def main():

    print("Application Started")

if __name__ == "__main__":

    main()
```

Benefits

- Testing
- Prevent accidental execution
- Reusable modules

---

# Virtual Environments

A virtual environment isolates project dependencies.

Create

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Deactivate

```bash
deactivate
```

---

# pip

Package manager for Python.

Install

```bash
pip install requests
```

Upgrade

```bash
pip install --upgrade requests
```

Uninstall

```bash
pip uninstall requests
```

List packages

```bash
pip list
```

Freeze dependencies

```bash
pip freeze > requirements.txt
```

Install from requirements

```bash
pip install -r requirements.txt
```

---

# Namespace

Namespace is a mapping between names and objects.

Python maintains namespaces for

- Built-in
- Global
- Local

Example

```python
x = 100

def demo():

    y = 20
```

Global namespace

```
x
```

Local namespace

```
y
```

---

# dir()

Shows names available inside namespace.

```python
print(dir())
```

---

# globals()

Returns global namespace.

```python
print(globals())
```

---

# locals()

Returns local namespace.

```python
def demo():

    x = 10

    print(locals())
```

---

# Best Practices

✓ Organize code into modules

✓ Prefer absolute imports

✓ Avoid wildcard imports

✓ Keep modules focused

✓ Use virtual environments

✓ Maintain requirements.txt

✓ Use pathlib over os.path

✓ Follow package structure

---

# Common Mistakes

❌ Circular imports

❌ Wildcard imports

❌ Huge utility modules

❌ Mixing unrelated functionality

❌ Not using virtual environments

❌ Hardcoded paths

❌ Importing inside loops unnecessarily

---

# Interview Questions

Easy

1. What is a module?
2. What is a package?
3. Difference between module and package.
4. What is pip?
5. What is requirements.txt?

Medium

1. Explain Python import system.
2. Difference between relative and absolute imports.
3. What is __name__?
4. Explain __main__.
5. Why use virtual environments?

Hard

1. Explain Python's module search path.
2. What happens during import internally?
3. Explain circular imports.
4. How does import caching work?
5. Explain namespace packages.

---

# Coding Exercises

Easy

- Create calculator module
- Import custom module
- Read current directory

Medium

- Build package for student management
- Create reusable utility module
- JSON parser

Hard

- Build CLI package
- Custom logging package
- Package with plugin architecture

---

# Practical Scenario

Scenario 1

A FastAPI project contains 300 files.

How should modules be organized?

Expected Discussion

- Routers
- Services
- Models
- Schemas
- Database
- Utilities
- Config
- Dependency Injection

---

Scenario 2

Different projects require different package versions.

Expected Solution

- Virtual environments
- requirements.txt
- Dependency isolation

---

# Summary

Modules and packages are fundamental to writing scalable Python applications. Understanding Python's import system, package organization, virtual environments, and dependency management is essential for professional software development and is frequently evaluated during technical interviews.


---

# 28. Exception Handling

## Definition

An exception is a runtime error that interrupts the normal flow of program execution.

Python provides structured exception handling to prevent program crashes and handle unexpected situations gracefully.

Example

```python
print(10 / 0)
```

Output

```
ZeroDivisionError: division by zero
```

---

# Why Exception Handling?

Without exception handling

```python
num = int(input("Enter number: "))
result = 100 / num
print(result)
```

If the user enters `0` or a non-numeric value, the program crashes.

With exception handling

```python
try:
    num = int(input("Enter number: "))
    print(100 / num)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter a valid integer.")
```

---

# try / except

Basic syntax

```python
try:
    # Code that may raise an exception
except ExceptionType:
    # Handle the exception
```

Example

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid integer.")
```

---

# Multiple Exceptions

```python
try:
    value = int(input())
    print(10 / value)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# Catching Multiple Exceptions Together

```python
try:
    ...
except (ValueError, TypeError):
    print("Handled")
```

---

# else Block

Executed only if no exception occurs.

```python
try:
    print("Success")
except:
    print("Error")
else:
    print("No exception")
```

---

# finally Block

Always executes, whether an exception occurs or not.

```python
file = None

try:
    file = open("data.txt")
finally:
    if file:
        file.close()
```

Use for:

- Closing files
- Closing database connections
- Releasing locks
- Cleaning resources

---

# Raising Exceptions

```python
age = -1

if age < 0:
    raise ValueError("Age cannot be negative")
```

---

# Custom Exceptions

```python
class InvalidAgeError(Exception):
    pass

age = -5

if age < 0:
    raise InvalidAgeError("Invalid age")
```

---

# 29. File Handling

Python provides built-in support for reading and writing files.

---

# Opening Files

```python
file = open("sample.txt", "r")
```

Modes

| Mode | Description |
|------|-------------|
| r | Read |
| w | Write |
| a | Append |
| x | Create |
| b | Binary |
| t | Text |

---

# Reading Files

```python
with open("sample.txt", "r") as file:
    content = file.read()

print(content)
```

Read line by line

```python
with open("sample.txt") as file:
    for line in file:
        print(line.strip())
```

---

# Writing Files

```python
with open("output.txt", "w") as file:
    file.write("Hello World")
```

---

# Appending

```python
with open("log.txt", "a") as file:
    file.write("New Entry\n")
```

---

# 30. Context Managers

A context manager automatically manages resources.

Example

```python
with open("sample.txt") as file:
    data = file.read()
```

Benefits

- Automatically closes resources
- Cleaner syntax
- Prevents resource leaks

Custom context manager

```python
from contextlib import contextmanager

@contextmanager
def managed():
    print("Start")
    yield
    print("End")

with managed():
    print("Working")
```

---

# 31. PEP 8

PEP 8 is the official Python style guide.

Guidelines

- Use 4 spaces for indentation.
- Maximum line length: 79–88 characters.
- Use `snake_case` for variables and functions.
- Use `PascalCase` for classes.
- Constants in `UPPER_CASE`.
- Add blank lines between functions/classes.
- Group imports (standard, third-party, local).

Example

```python
def calculate_total(price, tax):
    return price + tax
```

---

# 32. Logging

Use logging instead of `print()` for production applications.

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application started")
logging.warning("Low disk space")
logging.error("Database connection failed")
```

Levels

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

---

# 33. Debugging

Common techniques

- Use breakpoints in an IDE.
- Use `pdb`.
- Read stack traces carefully.
- Log important events.
- Reproduce bugs consistently.

Example

```python
import pdb

pdb.set_trace()
```

---

# 34. Performance Tips

- Use list comprehensions where appropriate.
- Prefer generators for large datasets.
- Avoid repeated string concatenation in loops.
- Use sets for fast membership checks.
- Use dictionaries for O(1) average lookups.
- Profile before optimizing.

---

# 35. Pythonic Coding Practices

Good

```python
if items:
    print("Not empty")
```

Avoid

```python
if len(items) > 0:
    print("Not empty")
```

Use

```python
name = user.get("name", "Guest")
```

Instead of

```python
if "name" in user:
    name = user["name"]
else:
    name = "Guest"
```

---

# 36. Candidate Evaluation Guidelines

Evaluate candidates on:

### Python Fundamentals
- Variables
- Data types
- Functions
- Modules
- Exceptions

### Code Quality
- Readability
- Naming
- Modularity
- Error handling

### Problem Solving
- Correctness
- Efficiency
- Edge cases

### Professional Practices
- Logging
- Testing
- PEP 8
- Dependency management

---

# 37. Common Interview Questions

### Easy

1. Difference between `try` and `finally`.
2. Why use `with`?
3. What is PEP 8?
4. Difference between `read()` and `readline()`.
5. What is logging?

### Medium

1. Explain exception propagation.
2. How does `with` work internally?
3. Why avoid bare `except`?
4. Difference between logging and print.
5. Explain context managers.

### Hard

1. Implement a custom context manager.
2. Explain Python's exception hierarchy.
3. Discuss resource leaks.
4. How does exception chaining work?
5. Design a robust logging strategy for a microservice.

---

# 38. Coding Exercises

Easy

- Read a file and count words.
- Handle invalid user input.
- Write logs to a file.

Medium

- Build a CSV reader.
- Create a custom exception.
- Implement file copy utility.

Hard

- Build a configurable logging system.
- Implement a custom context manager.
- Design an error-handling framework for an API.

---

# 39. Practical Scenarios

### Scenario 1

A production API crashes due to unexpected input.

Expected Discussion

- Input validation
- Exception handling
- Logging
- Monitoring
- User-friendly error responses

---

### Scenario 2

A batch process leaves files open.

Expected Discussion

- Use `with`
- Context managers
- Resource cleanup
- Error handling

---

### Scenario 3

Application logs are difficult to analyze.

Expected Discussion

- Structured logging
- Log levels
- Centralized logging
- Correlation IDs

---

# 40. Python Core Summary

By mastering Python Core, a developer gains the foundation required for professional software development.

Core competencies include:

- Python execution model
- Variables and data types
- Operators
- Control flow
- Functions
- Scope and namespaces
- Modules and packages
- Virtual environments
- Exception handling
- File handling
- Context managers
- Logging
- Debugging
- Pythonic coding practices

These topics are essential for backend frameworks such as FastAPI and Django and are heavily assessed in technical interviews.

---