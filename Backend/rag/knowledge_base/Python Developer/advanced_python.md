# Python Developer Knowledge Base
# Module 03 — Advanced Python

---

# 1. Object-Oriented Programming (OOP)

## Definition

Object-Oriented Programming (OOP) is a programming paradigm that organizes software around **objects** instead of functions.

An object combines:

- State (Data)
- Behavior (Methods)

Example

```python
class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def display(self):

        print(self.name, self.salary)

emp = Employee("Alice", 60000)

emp.display()
```

Output

```
Alice 60000
```

---

# Why OOP?

Procedural Programming Problems

```
Thousands of functions

↓

Global Variables

↓

Code Duplication

↓

Poor Maintainability
```

OOP solves these problems by

- Encapsulation
- Reusability
- Maintainability
- Scalability
- Abstraction

---

# Real-world Analogy

Consider a Car.

Properties

```
Brand

Color

Engine

Speed
```

Behaviors

```
Start

Stop

Brake

Accelerate
```

In Python

```python
class Car:

    def start(self):

        print("Engine Started")

    def stop(self):

        print("Engine Stopped")
```

---

# Class

A class is a blueprint for creating objects.

Example

```python
class Student:

    pass
```

The class itself occupies memory only once.

---

# Object

An object is an instance of a class.

Example

```python
student1 = Student()

student2 = Student()
```

Memory

```
Student Class

↓

student1

↓

student2

↓

student3
```

Each object has independent data.

---

# Object Creation Process

When Python executes

```python
obj = Employee("John",50000)
```

Internally

```
Employee class located

↓

Memory allocated

↓

Object created

↓

__init__() called

↓

Reference returned
```

---

# Constructor

Constructor initializes object state.

Python constructor

```
__init__()
```

Example

```python
class Student:

    def __init__(self):

        print("Constructor Called")
```

Output

```
Constructor Called
```

---

# Parameterized Constructor

```python
class Student:

    def __init__(self,name,marks):

        self.name=name

        self.marks=marks
```

Creating object

```python
s=Student("Alice",90)
```

---

# self Keyword

self refers to the current object.

Example

```python
class Demo:

    def display(self):

        print(self)
```

Calling

```python
d=Demo()

d.display()
```

Equivalent

```python
Demo.display(d)
```

---

# Instance Variables

Belong to each object.

```python
class Employee:

    def __init__(self,name):

        self.name=name
```

Each object has its own copy.

---

# Class Variables

Shared by all objects.

```python
class Employee:

    company="ABC Pvt Ltd"
```

Memory

```
Employee.company

↓

Shared

↓

emp1

emp2

emp3
```

---

# Instance Methods

Operate on object data.

```python
class Student:

    def display(self):

        print(self.name)
```

---

# Class Methods

Operate on class variables.

Decorator

```python
@classmethod
```

Example

```python
class Employee:

    company="ABC"

    @classmethod

    def show_company(cls):

        print(cls.company)
```

Calling

```python
Employee.show_company()
```

---

# Static Methods

Don't use

```
self

or

cls
```

Decorator

```python
@staticmethod
```

Example

```python
class Math:

    @staticmethod

    def add(a,b):

        return a+b
```

Calling

```python
Math.add(10,20)
```

---

# Difference

Instance Method

```
Uses self

Works on object data
```

Class Method

```
Uses cls

Works on class data
```

Static Method

```
No self

No cls

Utility function
```

---

# Four Pillars of OOP

```
Encapsulation

↓

Inheritance

↓

Polymorphism

↓

Abstraction
```

---

# Encapsulation

Definition

Binding data and methods together while restricting direct access.

Example

```python
class Bank:

    def __init__(self):

        self.__balance=1000
```

Private variable

```
__balance
```

Access

```python
print(account.__balance)
```

Produces

```
AttributeError
```

---

# Getter Setter

```python
class Bank:

    def __init__(self):

        self.__balance=1000

    def get_balance(self):

        return self.__balance

    def deposit(self,amount):

        self.__balance+=amount
```

---

# Name Mangling

Python converts

```
__balance
```

into

```
_Bank__balance
```

Not true security.

Used to avoid accidental modification.

---

# Inheritance

Definition

One class acquires properties of another.

Parent

↓

Child

Example

```python
class Animal:

    def speak(self):

        print("Sound")

class Dog(Animal):

    pass
```

Dog automatically gets

```
speak()
```

---

# Types of Inheritance

Single

```
A

↓

B
```

Multiple

```
A

B

↓

C
```

Multilevel

```
A

↓

B

↓

C
```

Hierarchical

```
     A

   / | \

  B  C  D
```

Hybrid

Combination.

---

# super()

Calls parent methods.

Example

```python
class Animal:

    def __init__(self):

        print("Animal")

class Dog(Animal):

    def __init__(self):

        super().__init__()

        print("Dog")
```

Output

```
Animal

Dog
```

---

# Method Overriding

Child replaces parent implementation.

```python
class Animal:

    def sound(self):

        print("Animal")

class Dog(Animal):

    def sound(self):

        print("Bark")
```

Calling

```python
Dog().sound()
```

Output

```
Bark
```

---

# Polymorphism

One interface

↓

Many implementations

Example

```python
class Cat:

    def speak(self):

        print("Meow")

class Dog:

    def speak(self):

        print("Bark")
```

Both respond to

```
speak()
```

---

# Duck Typing

Python follows

```
"If it walks like a duck and quacks like a duck,

it is a duck."
```

Example

```python
class Bird:

    def fly(self):

        print("Flying")

class Plane:

    def fly(self):

        print("Flying")

def start(obj):

    obj.fly()
```

Works for both.

---

# Abstraction

Hide implementation details.

Expose only necessary functionality.

Example

```python
from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod

    def start(self):

        pass
```

Implementation

```python
class Car(Vehicle):

    def start(self):

        print("Started")
```

---

# Abstract Base Class

Cannot create object.

```python
Vehicle()
```

Produces

```
TypeError
```

---

# Method Resolution Order (MRO)

Python resolves methods using

```
C3 Linearization
```

View

```python
print(Dog.mro())
```

Useful in

- Multiple inheritance

- super()

---

# Composition vs Inheritance

Composition

```
Car

↓

Engine
```

Inheritance

```
Vehicle

↓

Car
```

Rule

Prefer

```
Composition

over

Inheritance
```

unless there is a genuine

"is-a"

relationship.

---

# Best Practices

✓ Prefer composition over deep inheritance.

✓ Keep classes focused.

✓ Follow Single Responsibility Principle.

✓ Avoid God classes.

✓ Use dataclasses where appropriate.

✓ Minimize mutable shared state.

✓ Encapsulate business logic.

---

# Common Mistakes

❌ Huge inheritance trees

❌ Misusing static methods

❌ Public mutable attributes

❌ Multiple inheritance without understanding MRO

❌ Circular object references

---

# Interview Questions

Easy

1. What is OOP?

2. Difference between class and object.

3. What is self?

4. Constructor vs Method.

5. What is encapsulation?

Medium

1. Explain inheritance.

2. Difference between class method and static method.

3. Explain method overriding.

4. Explain duck typing.

5. What is abstraction?

Hard

1. Explain Python MRO.

2. What is C3 Linearization?

3. Explain object creation internally.

4. Difference between composition and inheritance.

5. Explain name mangling.

---

# Coding Exercises

Easy

- Student class

- Bank Account

- Rectangle Area

Medium

- Employee Payroll

- Library Management

- Shopping Cart

Hard

- Mini ORM

- Inventory System

- Hotel Reservation

---

# Practical Scenario

Scenario

Design a Banking System.

Expected Classes

```
Customer

↓

Account

↓

SavingsAccount

↓

CurrentAccount

↓

Transaction
```

Discussion

- Encapsulation

- Inheritance

- Composition

- Exception Handling

- OOP Design

---

# Summary

Object-Oriented Programming is the foundation of scalable Python applications. Understanding classes, objects, encapsulation, inheritance, polymorphism, abstraction, method resolution order, and composition enables developers to design maintainable and extensible software. These concepts are frequently evaluated in Python interviews, especially for mid-level and senior roles.

---

---

# 2. Magic (Dunder) Methods

## Definition

Magic methods (also called **dunder methods**, short for "double underscore") are special methods provided by Python that allow developers to customize the behavior of objects.

They are automatically invoked by Python when specific operations are performed on an object.

Examples

```
__init__

__str__

__repr__

__len__

__eq__

__lt__

__add__

__iter__

__next__

__call__
```

---

# Why Magic Methods?

Without magic methods

```python
class Student:

    pass

s = Student()

print(s)
```

Output

```
<__main__.Student object at 0x...>
```

Not very informative.

With

```python
class Student:

    def __str__(self):

        return "Student Object"
```

Output

```
Student Object
```

---

# __init__()

Object constructor.

Called immediately after object creation.

```python
class Employee:

    def __init__(self,name):

        self.name = name
```

---

# __str__()

Human-readable representation.

```python
class Employee:

    def __init__(self,name):

        self.name = name

    def __str__(self):

        return self.name
```

Calling

```python
print(emp)
```

Output

```
Alice
```

---

# __repr__()

Developer-friendly representation.

Example

```python
class Employee:

    def __repr__(self):

        return "Employee('Alice')"
```

Calling

```python
emp
```

or

```python
repr(emp)
```

Output

```
Employee('Alice')
```

Best Practice

- `__str__()` → End users
- `__repr__()` → Developers

---

# __len__()

Controls `len()`.

```python
class Team:

    def __len__(self):

        return 25
```

Calling

```python
len(team)
```

Output

```
25
```

---

# __getitem__()

Supports indexing.

```python
class Numbers:

    def __init__(self):

        self.values = [10,20,30]

    def __getitem__(self,index):

        return self.values[index]
```

Calling

```python
obj[1]
```

Output

```
20
```

---

# __setitem__()

Supports assignment.

```python
obj[0] = 100
```

Internally

```
__setitem__()
```

---

# __delitem__()

```python
del obj[1]
```

---

# __contains__()

Supports

```python
10 in obj
```

---

# __call__()

Makes objects callable.

```python
class Greeting:

    def __call__(self):

        print("Hello")
```

Calling

```python
g = Greeting()

g()
```

Output

```
Hello
```

---

# __eq__()

Controls ==

```python
class Employee:

    def __eq__(self,other):

        return self.id == other.id
```

---

# __lt__()

Less than

```
<
```

---

# __gt__()

Greater than

```
>
```

---

# __hash__()

Allows objects to be dictionary keys.

Example

```python
class User:

    def __hash__(self):

        return hash(self.id)
```

---

# Operator Overloading

Python allows operators to work with custom objects.

Example

```python
class Vector:

    def __init__(self,x,y):

        self.x=x

        self.y=y

    def __add__(self,other):

        return Vector(

            self.x+other.x,

            self.y+other.y
        )
```

Usage

```python
v3 = v1 + v2
```

Internally

```
v1.__add__(v2)
```

---

# Common Operator Methods

```
+

↓

__add__

-

↓

__sub__

*

↓

__mul__

/

↓

__truediv__

//

↓

__floordiv__

%

↓

__mod__

**

↓

__pow__
```

---

# Iterator Protocol

An iterator is an object that returns values one at a time.

Python iterator protocol consists of

```
__iter__()

↓

__next__()
```

---

# Iterable

Objects like

- list
- tuple
- dictionary
- string
- set

are iterable.

Example

```python
numbers = [1,2,3]

for n in numbers:

    print(n)
```

Internally

```
iter()

↓

next()

↓

next()

↓

next()
```

---

# iter()

Returns iterator.

```python
numbers = [10,20,30]

it = iter(numbers)
```

---

# next()

Returns next value.

```python
print(next(it))
```

Output

```
10
```

Repeated

```
20

30
```

Then

```
StopIteration
```

---

# Creating Custom Iterator

```python
class Counter:

    def __init__(self):

        self.count = 1

    def __iter__(self):

        return self

    def __next__(self):

        if self.count > 5:

            raise StopIteration

        value = self.count

        self.count += 1

        return value
```

Using

```python
for i in Counter():

    print(i)
```

Output

```
1

2

3

4

5
```

---

# Generators

Generator is a function that produces values lazily.

Uses

```
yield
```

instead of

```
return
```

---

# Normal Function

```python
def numbers():

    return [1,2,3]
```

Entire list stored in memory.

---

# Generator Function

```python
def numbers():

    yield 1

    yield 2

    yield 3
```

Values produced one by one.

---

# Execution Flow

```
Call Generator

↓

Generator Object

↓

next()

↓

yield

↓

Pause

↓

Resume

↓

yield
```

---

# Example

```python
def square():

    for i in range(5):

        yield i*i
```

Calling

```python
g = square()

for value in g:

    print(value)
```

Output

```
0

1

4

9

16
```

---

# Generator Expression

List

```python
[x*x for x in range(100000)]
```

Generator

```python
(x*x for x in range(100000))
```

Advantages

- Low memory
- Faster for streaming
- Lazy evaluation

---

# Yield vs Return

Return

- Ends function

Yield

- Pauses function
- Saves state
- Continues later

---

# Lazy Evaluation

Generator computes values only when requested.

Applications

- Reading huge files
- API pagination
- Streaming data
- ML datasets
- ETL pipelines

---

# Memory Comparison

List

```
1 Million Objects

↓

Memory Allocated
```

Generator

```
One Object

↓

Process

↓

Discard

↓

Next Object
```

Huge memory savings.

---

# itertools Module

Useful iterator utilities.

Examples

```python
from itertools import count

from itertools import cycle

from itertools import repeat

from itertools import permutations

from itertools import combinations
```

---

# Best Practices

✓ Prefer generators for large datasets.

✓ Implement iterators when custom iteration is needed.

✓ Use __repr__ for debugging.

✓ Override comparison operators carefully.

✓ Keep operator overloading intuitive.

---

# Common Mistakes

❌ Confusing iterable with iterator

❌ Forgetting StopIteration

❌ Returning instead of yielding

❌ Using generators twice after exhaustion

❌ Incorrect __eq__ implementation

---

# Interview Questions

Easy

1. What are magic methods?
2. Difference between __str__ and __repr__.
3. What is an iterator?
4. What is a generator?
5. Difference between yield and return.

Medium

1. Explain iterator protocol.
2. Difference between iterable and iterator.
3. Explain operator overloading.
4. When should generators be used?
5. Explain lazy evaluation.

Hard

1. How does Python implement generators internally?
2. Explain frame objects in generators.
3. What happens after StopIteration?
4. Explain generator delegation using yield from.
5. How do async generators differ from regular generators?

---

# Coding Exercises

Easy

- Custom iterator
- Fibonacci generator
- Countdown iterator

Medium

- Infinite generator
- Custom collection class
- Matrix iterator

Hard

- Log file streaming generator
- CSV chunk reader
- Infinite prime number generator

---

# Practical Scenario

Scenario

A system processes a 50 GB log file.

Question

Should you use

```
readlines()

or

Generator?
```

Expected Discussion

- Memory efficiency
- Lazy loading
- Streaming
- Performance
- Scalability

---

# Summary

Magic methods enable Python objects to integrate seamlessly with built-in language features, while iterators and generators provide efficient mechanisms for processing data lazily. Mastering these concepts is essential for writing Pythonic, memory-efficient, and highly reusable code and is frequently assessed in mid-level and senior Python interviews.

---


---

# 3. Decorators, Closures, Higher-Order Functions, and Descriptors

## Definition

A decorator is a design pattern that allows developers to **modify or extend the behavior of a function or class without changing its source code**.

Decorators are heavily used in:

- FastAPI
- Flask
- Django
- Logging
- Authentication
- Authorization
- Caching
- Validation
- Performance Monitoring

---

# What is a First-Class Function?

In Python, functions are **first-class objects**, which means they can:

- Be assigned to variables
- Be passed as arguments
- Be returned from other functions
- Be stored in data structures

Example

```python
def greet():
    return "Hello"

message = greet

print(message())
```

Output

```
Hello
```

---

# Higher-Order Functions

A higher-order function is a function that:

- Accepts another function as an argument
- Returns another function

Example

```python
def calculate(operation, a, b):
    return operation(a, b)

def add(x, y):
    return x + y

print(calculate(add, 10, 20))
```

Output

```
30
```

---

# Nested Functions

Functions can be defined inside other functions.

Example

```python
def outer():

    def inner():
        print("Inner Function")

    inner()

outer()
```

---

# Closures

A closure is created when an inner function remembers variables from its enclosing scope, even after the outer function has finished execution.

Example

```python
def multiplier(x):

    def multiply(y):
        return x * y

    return multiply

double = multiplier(2)

print(double(5))
```

Output

```
10
```

---

# Why Closures?

Closures are useful for:

- Function factories
- Maintaining state
- Callbacks
- Decorators

---

# Basic Decorator

Without decorator

```python
def hello():
    print("Hello")
```

Decorator

```python
def logger(func):

    def wrapper():
        print("Function Started")
        func()
        print("Function Finished")

    return wrapper
```

Usage

```python
@logger
def hello():
    print("Hello")

hello()
```

Output

```
Function Started

Hello

Function Finished
```

---

# Decorator Execution Flow

```
hello()

↓

wrapper()

↓

Before Logic

↓

Original Function

↓

After Logic
```

---

# Decorator with Arguments

```python
def logger(func):

    def wrapper(*args, **kwargs):

        print("Calling Function")

        result = func(*args, **kwargs)

        print("Completed")

        return result

    return wrapper
```

Example

```python
@logger
def add(a, b):
    return a + b

print(add(10, 20))
```

---

# Multiple Decorators

```python
@decorator1
@decorator2
def function():
    pass
```

Execution Order

```
decorator1

↓

decorator2

↓

function

↓

decorator2

↓

decorator1
```

---

# functools.wraps

Without `wraps`, the original function metadata is lost.

Example

```python
from functools import wraps

def logger(func):

    @wraps(func)

    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper
```

Benefits

- Preserves function name
- Preserves docstring
- Preserves annotations

---

# Built-in Decorators

Python provides several built-in decorators.

Examples

```
@property

@staticmethod

@classmethod

@abstractmethod

@dataclass

@lru_cache
```

---

# @property

Used to access methods like attributes.

Example

```python
class Employee:

    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary
```

Usage

```python
emp = Employee(50000)

print(emp.salary)
```

Notice

```
emp.salary

NOT

emp.salary()
```

---

# Property Setter

```python
class Employee:

    def __init__(self):
        self._salary = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):

        if value < 0:
            raise ValueError("Invalid Salary")

        self._salary = value
```

---

# Property Deleter

```python
@salary.deleter

def salary(self):

    del self._salary
```

---

# functools.lru_cache

Caches expensive function calls.

Example

```python
from functools import lru_cache

@lru_cache(maxsize=128)

def fibonacci(n):

    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n-2)
```

Benefits

- Faster execution
- Avoids repeated computation

---

# functools.partial

Creates partially applied functions.

Example

```python
from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)

print(double(10))
```

Output

```
20
```

---

# map()

Applies a function to every element.

```python
numbers = [1,2,3]

result = map(lambda x: x*x, numbers)

print(list(result))
```

Output

```
[1,4,9]
```

---

# filter()

Filters data.

```python
numbers = [1,2,3,4,5]

even = filter(lambda x: x%2==0, numbers)

print(list(even))
```

Output

```
[2,4]
```

---

# reduce()

Reduces iterable into a single value.

```python
from functools import reduce

numbers = [1,2,3,4]

result = reduce(lambda x,y:x+y, numbers)

print(result)
```

Output

```
10
```

---

# Descriptors

Descriptors customize attribute access.

Methods

```
__get__()

__set__()

__delete__()
```

Example

```python
class Positive:

    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):

        if value < 0:
            raise ValueError("Positive values only")

        instance._value = value
```

Usage

```python
class Product:

    price = Positive()

p = Product()

p.price = 100
```

---

# Data Descriptor

Implements

```
__get__

+

__set__
```

---

# Non-Data Descriptor

Implements only

```
__get__
```

---

# Descriptor Use Cases

- ORM fields
- Validation
- Lazy loading
- Properties
- Framework internals

---

# Decorators in FastAPI

```python
@app.get("/users")
async def get_users():
    return []
```

`@app.get` is a decorator that registers the function as an HTTP GET endpoint.

---

# Decorators in Flask

```python
@app.route("/")
def home():
    return "Hello"
```

---

# Decorators in Django

```python
@login_required

def dashboard(request):
    ...
```

---

# Best Practices

✓ Keep decorators small.

✓ Use `functools.wraps`.

✓ Avoid deeply nested decorators.

✓ Document decorator behavior.

✓ Prefer `@property` over trivial getter methods.

---

# Common Mistakes

❌ Forgetting to return wrapper.

❌ Losing metadata by not using `wraps`.

❌ Modifying mutable closure variables incorrectly.

❌ Creating overly complex decorators.

❌ Using decorators when composition would be simpler.

---

# Interview Questions

### Easy

1. What is a decorator?
2. What is a closure?
3. What is a higher-order function?
4. What does `@property` do?
5. Difference between `map()` and `filter()`.

### Medium

1. Explain decorator execution.
2. Why use `functools.wraps`?
3. Explain closures with examples.
4. Difference between property and getter methods.
5. What is `lru_cache`?

### Hard

1. How are decorators implemented internally?
2. Explain descriptor protocol.
3. Difference between data and non-data descriptors.
4. How does FastAPI use decorators?
5. Explain function objects in CPython.

---

# Coding Exercises

Easy

- Logging decorator
- Timer decorator
- Authentication decorator

Medium

- Retry decorator
- Cache decorator
- Validation decorator

Hard

- Rate limiting decorator
- Role-based authorization decorator
- Descriptor-based ORM field validator

---

# Practical Scenario

Scenario

Design a logging system that automatically logs execution time for every API endpoint.

Expected Discussion

- Decorators
- `time.perf_counter()`
- `functools.wraps`
- Logging
- Exception handling

---

# Summary

Decorators, closures, higher-order functions, and descriptors are advanced Python features that enable clean, reusable, and extensible software design. They are fundamental to modern Python frameworks such as FastAPI, Django, and Flask, and are among the most frequently assessed topics in senior Python technical interviews.

---

# 4. Memory Management, Garbage Collection, Copying, and Python Internals

---

# Memory Management

## Definition

Memory management is the process by which Python allocates, tracks, and releases memory used by objects.

Unlike C/C++, Python automatically manages memory through:

- Object allocation
- Reference counting
- Garbage Collection
- Memory allocator (PyMalloc)

Developer does not explicitly allocate or free memory.

---

# Python Memory Architecture

```
Operating System

↓

Python Memory Manager

↓

PyMalloc

↓

Memory Pools

↓

Memory Blocks

↓

Python Objects
```

Python requests memory from the Operating System and manages it internally.

---

# Python Memory Manager

Python uses an internal memory manager.

Responsibilities

- Allocate memory
- Reuse memory
- Free unused objects
- Manage object lifecycle

---

# PyMalloc

CPython uses a specialized allocator called

```
PyMalloc
```

Optimized for

- Small objects
- Fast allocation
- Low fragmentation

Suitable for

- Integers
- Lists
- Dictionaries
- Tuples
- Strings

Large allocations are delegated to the operating system.

---

# Object Lifecycle

```
Object Created

↓

Reference Assigned

↓

Reference Count Increases

↓

References Removed

↓

Reference Count Becomes Zero

↓

Memory Released
```

---

# Reference Counting

Every object stores a reference count.

Example

```python
x = [1,2,3]

y = x

z = x
```

Reference count

```
Object

↓

x

↓

y

↓

z

Reference Count = 3
```

Deleting

```python
del y
```

Reference count

```
2
```

---

# Checking Reference Count

```python
import sys

x = []

print(sys.getrefcount(x))
```

Note

`getrefcount()` returns one additional reference because the object is temporarily passed to the function.

---

# Garbage Collection

Reference counting cannot clean cyclic references.

Example

```python
class A:
    pass

a = A()
b = A()

a.other = b
b.other = a
```

Even after

```python
del a
del b
```

Objects reference each other.

Garbage Collector detects and removes such cycles.

---

# gc Module

Python exposes garbage collection through the `gc` module.

Enable collection

```python
import gc

gc.enable()
```

Disable collection

```python
gc.disable()
```

Force collection

```python
gc.collect()
```

View statistics

```python
gc.get_stats()
```

---

# Generational Garbage Collection

Python groups objects into generations.

```
Generation 0

↓

Generation 1

↓

Generation 2
```

Most objects die young.

Frequently surviving objects move to older generations.

Benefits

- Faster cleanup
- Better performance

---

# Memory Leaks

Python reduces memory leaks but they can still occur.

Common causes

- Global variables
- Circular references involving external resources
- C extensions
- Large caches
- Objects retained in lists or dictionaries

Example

```python
cache = []

while True:

    cache.append([0]*100000)
```

Memory usage continuously grows.

---

# Weak References

Weak references do not increase the reference count.

Module

```python
import weakref
```

Example

```python
import weakref

class Employee:
    pass

emp = Employee()

ref = weakref.ref(emp)

print(ref())
```

After deleting

```python
del emp
```

```python
print(ref())
```

Output

```
None
```

Applications

- Object caches
- Observer pattern
- GUI frameworks

---

# Object Interning

Python reuses certain immutable objects.

Example

```python
a = 10
b = 10

print(a is b)
```

Output

```
True
```

Similarly

```python
x = "hello"
y = "hello"

print(x is y)
```

Often returns

```
True
```

Interning improves memory efficiency.

---

# Identity vs Equality

Identity

```python
is
```

Checks

```
Same Object
```

Equality

```python
==
```

Checks

```
Same Value
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

# Copying Objects

Assignment

```python
a = [1,2]

b = a
```

Both variables reference the same object.

---

# Shallow Copy

Module

```python
import copy
```

Example

```python
a = [[1],[2]]

b = copy.copy(a)
```

Memory

```
Outer List

Copied

↓

Inner Lists

Shared
```

Changing inner list affects both.

---

# Deep Copy

```python
import copy

b = copy.deepcopy(a)
```

Entire object hierarchy is copied.

Memory

```
Outer List

Copied

↓

Inner Lists

Copied
```

Independent objects.

---

# Example

```python
import copy

a = [[1],[2]]

b = copy.deepcopy(a)

b[0].append(99)

print(a)

print(b)
```

Output

```
[[1],[2]]

[[1,99],[2]]
```

---

# Mutable vs Immutable Objects

Immutable

```
int

float

bool

str

tuple

frozenset
```

Mutable

```
list

dict

set

bytearray
```

Understanding mutability is essential for avoiding bugs.

---

# Slots

Normally

```python
class Employee:

    pass
```

Every object stores

```
__dict__
```

Using

```python
class Employee:

    __slots__ = ("name","salary")
```

Benefits

- Lower memory usage
- Faster attribute access

Limitations

- Cannot dynamically add attributes

---

# Memory Optimization Tips

✓ Use generators instead of large lists.

✓ Use `__slots__` for millions of objects.

✓ Prefer tuples for immutable data.

✓ Remove unused references.

✓ Avoid unnecessary global variables.

✓ Stream large files instead of loading them entirely.

✓ Use `array` or `numpy` for large numeric datasets.

---

# Python Object Model

Everything in Python is an object.

Examples

```
Integers

Strings

Functions

Classes

Modules

Exceptions
```

Example

```python
print(type(10))

print(type(print))

print(type(len))
```

---

# CPython Object Structure

Each object contains

```
Reference Count

↓

Type Pointer

↓

Value
```

Conceptually

```
PyObject

↓

Reference Count

↓

Type

↓

Object Data
```

---

# Performance Considerations

Avoid

```python
result = ""

for word in words:

    result += word
```

Use

```python
result = "".join(words)
```

Reason

- Strings are immutable
- `join()` minimizes intermediate objects

---

# Profiling Memory

Useful modules

```python
tracemalloc

memory_profiler

objgraph

gc
```

Example

```python
import tracemalloc

tracemalloc.start()
```

---

# Best Practices

✓ Understand reference counting.

✓ Prefer deep copy for nested mutable structures.

✓ Profile before optimizing.

✓ Release unused resources.

✓ Use weak references when appropriate.

✓ Avoid circular references.

---

# Common Mistakes

❌ Confusing assignment with copying.

❌ Using shallow copy for nested objects.

❌ Forgetting mutable default arguments.

❌ Assuming `is` checks value equality.

❌ Creating unnecessary large lists.

---

# Interview Questions

Easy

1. What is garbage collection?

2. Difference between `is` and `==`.

3. What is shallow copy?

4. What is deep copy?

5. What is reference counting?

Medium

1. Explain Python memory management.

2. How does the `gc` module work?

3. What are weak references?

4. What is object interning?

5. Explain `__slots__`.

Hard

1. Explain PyMalloc.

2. How does CPython represent objects?

3. Why can't reference counting alone handle cyclic references?

4. Explain generational garbage collection.

5. Discuss memory optimization techniques for large-scale Python applications.

---

# Coding Exercises

Easy

- Compare shallow and deep copy.

- Demonstrate `is` vs `==`.

- Use `gc.collect()`.

Medium

- Build an object cache using `weakref`.

- Measure memory usage with `tracemalloc`.

- Compare list vs generator memory consumption.

Hard

- Implement a custom object pool.

- Optimize a large in-memory dataset.

- Analyze memory leaks in a simulated application.

---

# Practical Scenario

Scenario

A FastAPI service gradually consumes more memory over several days.

Expected Discussion

- Memory profiling

- Garbage collection

- Weak references

- Caching strategy

- Resource cleanup

- Detecting reference cycles

---

# Summary

Understanding Python's memory model is essential for writing efficient and scalable applications. Knowledge of reference counting, garbage collection, object copying, weak references, and CPython internals helps developers avoid memory leaks, optimize performance, and design robust systems. These concepts are commonly assessed in senior-level Python interviews and performance-focused roles.

---


# 5. Concurrency, Parallelism, Threading, Multiprocessing, and Async Programming

---

# Introduction

Modern applications must handle multiple tasks efficiently.

Examples

- API Servers
- Web Crawlers
- Chat Applications
- AI Inference Services
- File Processing
- Background Jobs

Python provides multiple approaches:

- Threading
- Multiprocessing
- Async Programming
- Concurrent Futures

Understanding when to use each is a key interview topic.

---

# Concurrency vs Parallelism

## Concurrency

Concurrency means multiple tasks make progress during overlapping time periods.

Tasks are interleaved.

```
Task A

↓

Task B

↓

Task A

↓

Task C

↓

Task B
```

Useful for

- Waiting for APIs
- Database queries
- File operations

---

## Parallelism

Parallelism means multiple tasks execute at the same time on different CPU cores.

```
Core 1 → Task A

Core 2 → Task B

Core 3 → Task C
```

Useful for

- Machine Learning
- Image Processing
- Scientific Computing
- Video Encoding

---

# Processes vs Threads

## Process

A process is an independent program execution.

Characteristics

- Separate memory
- Separate resources
- More expensive to create
- Better isolation

Example

```
Chrome

↓

Tab 1

↓

Tab 2
```

---

## Thread

A thread is a lightweight execution unit inside a process.

Threads share

- Memory
- Variables
- File descriptors

Example

```
Web Server Process

↓

Thread 1

↓

Thread 2

↓

Thread 3
```

---

# Threading

Python provides

```python
threading
```

module.

Example

```python
import threading

def worker():

    print("Working")

t = threading.Thread(target=worker)

t.start()

t.join()
```

---

# Thread Lifecycle

```
Created

↓

Started

↓

Running

↓

Waiting

↓

Finished
```

---

# Multiple Threads

```python
import threading

def task(name):

    print(name)

threads = []

for i in range(5):

    t = threading.Thread(

        target=task,

        args=(i,)
    )

    threads.append(t)

    t.start()

for t in threads:

    t.join()
```

---

# Advantages of Threading

✓ Low memory usage

✓ Fast creation

✓ Good for I/O-bound tasks

✓ Shared memory

---

# Limitations

❌ Shared state

❌ Synchronization required

❌ GIL limitations

---

# Global Interpreter Lock (GIL)

## Definition

The Global Interpreter Lock (GIL) is a mutex in CPython that allows only **one thread to execute Python bytecode at a time**.

Even if multiple threads exist, only one can run Python bytecode simultaneously.

```
CPU

↓

Thread A

↓

GIL

↓

Execute

↓

Release

↓

Thread B
```

---

# Why GIL Exists

Benefits

- Simpler memory management
- Prevents race conditions in reference counting
- Easier implementation

Trade-offs

- CPU-bound threads cannot run in parallel
- Limits multi-threaded performance

---

# CPU-bound vs I/O-bound

## CPU-bound

Tasks spend most time using the CPU.

Examples

- Matrix multiplication
- Prime number calculation
- Encryption
- Image processing

Recommendation

```
Multiprocessing
```

---

## I/O-bound

Tasks spend most time waiting.

Examples

- API requests
- Reading files
- Database queries
- Network communication

Recommendation

```
Threading

or

Asyncio
```

---

# Race Condition

Occurs when multiple threads modify shared data simultaneously.

Example

```python
counter = 0

def increment():

    global counter

    for _ in range(100000):

        counter += 1
```

Expected

```
200000
```

Actual

May vary due to race conditions.

---

# Lock

Prevent simultaneous access.

```python
import threading

lock = threading.Lock()

counter = 0

def increment():

    global counter

    for _ in range(100000):

        with lock:

            counter += 1
```

---

# RLock

Reentrant Lock.

Allows the same thread to acquire the lock multiple times.

```python
lock = threading.RLock()
```

---

# Semaphore

Controls access to limited resources.

Example

```
Database Connections

↓

Maximum = 10
```

```python
sem = threading.Semaphore(10)
```

---

# Event

Used for signaling.

```
Producer

↓

Event Set

↓

Consumer Continues
```

Example

```python
event = threading.Event()

event.set()

event.wait()
```

---

# Condition

Used for producer-consumer coordination.

Methods

```
wait()

notify()

notify_all()
```

---

# Deadlock

Occurs when two threads wait indefinitely.

Example

```
Thread A

↓

Lock 1

↓

Waiting Lock 2

Thread B

↓

Lock 2

↓

Waiting Lock 1
```

Avoid

- Consistent lock ordering
- Timeouts
- Minimize lock scope

---

# Multiprocessing

Uses

```python
multiprocessing
```

Each process has

- Separate memory
- Separate Python interpreter
- Independent GIL

---

# Example

```python
from multiprocessing import Process

def worker():

    print("Working")

p = Process(target=worker)

p.start()

p.join()
```

---

# Process Pool

```python
from multiprocessing import Pool

def square(x):

    return x*x

with Pool(4) as pool:

    result = pool.map(square,

                      [1,2,3,4])

print(result)
```

---

# Thread vs Process

| Feature | Thread | Process |
|----------|--------|----------|
| Memory | Shared | Separate |
| Creation | Fast | Slower |
| Communication | Easy | IPC |
| GIL | Shared | Independent |
| Best For | I/O | CPU |

---

# Async Programming

Async programming enables efficient handling of many waiting operations using a single thread.

Useful for

- APIs
- Chat Servers
- Streaming
- WebSockets

---

# Coroutine

Coroutine is an async function.

```python
async def hello():

    print("Hello")
```

---

# await

Pauses execution until an awaited task completes.

```python
async def fetch():

    await asyncio.sleep(1)
```

---

# Event Loop

The event loop schedules coroutines.

```
Coroutine A

↓

Pause

↓

Coroutine B

↓

Pause

↓

Coroutine C

↓

Resume A
```

---

# asyncio

Python async framework.

Example

```python
import asyncio

async def hello():

    print("Hello")

asyncio.run(hello())
```

---

# Running Multiple Coroutines

```python
import asyncio

async def task(n):

    await asyncio.sleep(1)

    print(n)

async def main():

    await asyncio.gather(

        task(1),

        task(2),

        task(3)

    )

asyncio.run(main())
```

---

# asyncio.create_task()

Schedules concurrent execution.

```python
task = asyncio.create_task(fetch())
```

---

# Future

Represents a value available later.

Commonly used internally by asyncio.

---

# Async Context Manager

```python
async with session.get(url):

    ...
```

---

# Async Iterator

```python
async for row in stream:

    print(row)
```

---

# concurrent.futures

Provides high-level concurrency.

Thread Pool

```python
from concurrent.futures import ThreadPoolExecutor
```

Process Pool

```python
from concurrent.futures import ProcessPoolExecutor
```

---

# Example

```python
from concurrent.futures import ThreadPoolExecutor

def square(x):

    return x*x

with ThreadPoolExecutor() as executor:

    results = executor.map(square,

                           [1,2,3])

print(list(results))
```

---

# FastAPI Async

Example

```python
@app.get("/users")

async def users():

    return {"status":"ok"}
```

FastAPI uses

- Asyncio
- Event Loop
- ASGI

to handle many concurrent requests efficiently.

---

# Choosing the Right Approach

| Scenario | Recommended |
|----------|-------------|
| API Calls | Asyncio |
| Database Queries | Asyncio |
| File Reading | Threading |
| Image Processing | Multiprocessing |
| ML Training | Multiprocessing |
| Web Server | Asyncio |
| Batch Jobs | Process Pool |

---

# Best Practices

✓ Use asyncio for network I/O.

✓ Use multiprocessing for CPU-heavy work.

✓ Protect shared data with locks.

✓ Avoid blocking operations inside async functions.

✓ Minimize lock duration.

✓ Prefer thread pools for simple I/O tasks.

---

# Common Mistakes

❌ Blocking the event loop.

❌ Using threading for CPU-bound work.

❌ Forgetting `await`.

❌ Creating too many threads.

❌ Holding locks unnecessarily.

❌ Mixing sync and async incorrectly.

---

# Interview Questions

## Easy

1. Difference between process and thread.
2. What is concurrency?
3. What is parallelism?
4. What is GIL?
5. What is asyncio?

---

## Medium

1. Explain race conditions.
2. Difference between Lock and RLock.
3. When should multiprocessing be used?
4. Explain event loop.
5. Difference between `asyncio.gather()` and `create_task()`.

---

## Hard

1. Why does CPython have a GIL?
2. How does FastAPI achieve high concurrency?
3. Explain cooperative multitasking.
4. How do async context managers work?
5. Compare threading, multiprocessing, and asyncio for a high-throughput API.

---

# Coding Exercises

Easy

- Create two threads printing numbers.
- Use a lock to protect a counter.
- Write an async sleep example.

Medium

- Build a producer-consumer queue.
- Download multiple URLs concurrently.
- Process images using multiprocessing.

Hard

- Build an asynchronous web crawler.
- Implement a thread-safe cache.
- Design a concurrent task scheduler.

---

# Practical Scenario

Scenario

An AI service receives 5,000 requests per minute.

Requirements

- Low latency
- High throughput
- Background model inference
- Database logging

Expected Discussion

- FastAPI async endpoints
- Async database drivers
- Background tasks
- Multiprocessing for CPU-intensive inference
- Thread pools for blocking I/O
- Monitoring and graceful error handling

---

# Summary

Concurrency and parallelism are fundamental to building scalable Python applications. Understanding threading, multiprocessing, the GIL, asyncio, synchronization primitives, and execution models enables developers to choose the right approach for different workloads. These topics are among the most important in backend, FastAPI, and senior Python interviews.

---

# 6. Advanced Python Features, Design Patterns, and Best Practices

---

# Metaclasses

## Definition

In Python, **classes are objects**.

Just as objects are created from classes, classes themselves are created from **metaclasses**.

```
Object

↓

Created from Class

↓

Created from Metaclass
```

The default metaclass in Python is:

```python
type
```

Example

```python
class Employee:
    pass

print(type(Employee))
```

Output

```
<class 'type'>
```

---

# Creating Classes Dynamically

Classes can be created at runtime.

Example

```python
Employee = type(
    "Employee",
    (),
    {
        "company": "ABC Ltd"
    }
)

emp = Employee()

print(emp.company)
```

Applications

- ORMs
- Plugin systems
- Dynamic API generation

---

# Custom Metaclass

```python
class Meta(type):

    def __new__(cls, name, bases, attrs):

        print(f"Creating class {name}")

        return super().__new__(
            cls,
            name,
            bases,
            attrs
        )

class Employee(
    metaclass=Meta
):
    pass
```

---

# Introspection

Introspection allows inspection of objects at runtime.

Useful functions

```python
type()

isinstance()

issubclass()

dir()

vars()

hasattr()

getattr()

setattr()

callable()

id()
```

Example

```python
class User:

    def greet(self):
        pass

print(dir(User))
```

---

# Reflection

Reflection means modifying program behavior at runtime.

Example

```python
class Employee:

    pass

emp = Employee()

setattr(emp, "name", "Alice")

print(getattr(emp, "name"))
```

---

# Type Hints

Introduced to improve readability and static analysis.

Example

```python
def add(
    a: int,
    b: int
) -> int:

    return a + b
```

Benefits

- Better IDE support
- Static type checking
- Easier maintenance

---

# typing Module

Frequently used types

```python
List

Dict

Tuple

Set

Optional

Union

Any

Callable

Iterable

Generator

TypeVar

Generic

Literal

Protocol
```

Example

```python
from typing import List

def average(
    values: List[int]
) -> float:

    return sum(values)/len(values)
```

---

# Optional

```python
from typing import Optional

def find_user(
    name: str
) -> Optional[str]:

    ...
```

Means

```
str

or

None
```

---

# Union

```python
from typing import Union

def process(
    value: Union[int, str]
):

    ...
```

Python 3.10+

```python
int | str
```

---

# Generic Programming

Example

```python
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]
```

---

# Protocols (PEP 544)

Protocols support **structural typing**.

Example

```python
from typing import Protocol

class Printable(Protocol):

    def print(self) -> None:
        ...
```

Any object implementing `print()` satisfies the protocol.

---

# Dataclasses

Simplify data container classes.

Without dataclass

```python
class Employee:

    def __init__(
        self,
        name,
        salary
    ):

        self.name = name

        self.salary = salary
```

With dataclass

```python
from dataclasses import dataclass

@dataclass
class Employee:

    name: str

    salary: int
```

Automatically generates

- __init__
- __repr__
- __eq__

---

# Frozen Dataclass

```python
@dataclass(
    frozen=True
)
class Point:

    x: int

    y: int
```

Immutable object.

---

# Enum

Represents fixed constants.

```python
from enum import Enum

class Status(Enum):

    ACTIVE = 1

    INACTIVE = 2
```

Usage

```python
Status.ACTIVE
```

---

# Context Managers (Advanced)

Context managers ensure proper resource cleanup.

Custom implementation

```python
class Database:

    def __enter__(self):

        print("Connected")

        return self

    def __exit__(
        self,
        exc_type,
        exc,
        traceback
    ):

        print("Closed")
```

Usage

```python
with Database():

    print("Query")
```

---

# Python Design Patterns

Common patterns

- Singleton
- Factory
- Builder
- Strategy
- Observer
- Adapter
- Decorator
- Command

---

# Singleton Example

```python
class Singleton:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

        return cls._instance
```

---

# Factory Pattern

```python
class Dog:

    pass

class Cat:

    pass

class AnimalFactory:

    @staticmethod

    def create(name):

        if name == "dog":
            return Dog()

        return Cat()
```

---

# Strategy Pattern

Useful for interchangeable algorithms.

Examples

- Payment gateways
- Sorting algorithms
- Discount calculation

---

# SOLID Principles

## S

Single Responsibility Principle

One class should have one reason to change.

---

## O

Open/Closed Principle

Open for extension.

Closed for modification.

---

## L

Liskov Substitution Principle

Derived classes should replace base classes without breaking behavior.

---

## I

Interface Segregation Principle

Small focused interfaces.

---

## D

Dependency Inversion Principle

Depend on abstractions.

Not concrete implementations.

---

# Pythonic Best Practices

✓ Follow PEP 8

✓ Prefer composition over inheritance

✓ Use dataclasses for DTOs

✓ Prefer generators for large datasets

✓ Use context managers

✓ Use type hints

✓ Keep functions short

✓ Write unit tests

✓ Handle exceptions specifically

✓ Avoid mutable default arguments

---

# Common Mistakes

❌ Overusing inheritance

❌ Ignoring type hints

❌ Catching all exceptions

❌ Deeply nested logic

❌ Misusing globals

❌ Excessive metaclass usage

❌ Writing overly clever code

---

# Senior Interview Questions

## Easy

1. What is a dataclass?
2. Difference between Enum and constants.
3. What is introspection?
4. What is reflection?
5. What is a protocol?

---

## Medium

1. Explain metaclasses.
2. Difference between ABC and Protocol.
3. Explain `TypeVar`.
4. Why use design patterns?
5. Explain context managers internally.

---

## Hard

1. How does Python create classes?
2. Explain descriptor vs property.
3. When should metaclasses be avoided?
4. Compare composition and inheritance with examples.
5. Design a plugin architecture using dynamic imports and protocols.

---

# Coding Exercises

Easy

- Create a dataclass
- Create an Enum
- Implement a context manager

Medium

- Build a factory pattern
- Implement a strategy pattern
- Use protocols for dependency injection

Hard

- Create a plugin framework
- Implement a lightweight ORM model
- Build a dependency injection container

---

# Practical Scenario

Scenario

Design a scalable notification system supporting:

- Email
- SMS
- Push Notifications

Expected Discussion

- Strategy Pattern
- Factory Pattern
- Protocols
- Dependency Inversion
- Testing
- Extensibility

---

# Candidate Evaluation Rubric

Evaluate candidates on:

### Language Fundamentals

- Strong understanding of Python syntax
- OOP concepts
- Advanced language features

### Problem Solving

- Correctness
- Efficiency
- Edge case handling

### Code Quality

- Readability
- Maintainability
- Modularity
- Documentation

### Software Design

- SOLID principles
- Appropriate design patterns
- Separation of concerns

### Performance Awareness

- Memory optimization
- Concurrency choices
- Appropriate data structures

### Professional Practices

- Type hints
- Logging
- Testing
- Dependency management

---

# Module Summary

Advanced Python extends core language concepts into professional software engineering practices. Mastery of OOP, decorators, generators, concurrency, memory management, typing, metaclasses, and design patterns enables developers to build scalable, maintainable, and high-performance applications.

These topics are heavily assessed in mid-level and senior Python interviews, especially for backend development with FastAPI, Django, and large-scale distributed systems.

---


