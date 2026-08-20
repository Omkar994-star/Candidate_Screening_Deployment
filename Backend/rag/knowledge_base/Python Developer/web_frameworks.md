# Python Developer Knowledge Base
# Module 06 — Web Frameworks
# Part 1 — Web Fundamentals

---

# Module Overview

Modern Python backend development revolves around building web applications and APIs. Understanding how the web works is essential before learning Flask, Django, or FastAPI.

This module covers:

- Web Fundamentals
- HTTP & HTTPS
- Client-Server Architecture
- DNS
- URLs
- HTTP Methods
- Status Codes
- Headers
- Cookies
- Sessions
- REST Architecture
- JSON
- WSGI & ASGI
- Flask
- Django
- FastAPI
- Authentication
- Middleware
- Deployment
- Security Best Practices

---

# 1. Introduction to Web Development

A web application consists of:

- Client
- Server
- Network
- Database

Example

```
Browser

↓

Internet

↓

Web Server

↓

Application

↓

Database
```

Example

```
Chrome

↓

FastAPI

↓

PostgreSQL
```

---

# Client-Server Architecture

## Client

The client requests information.

Examples

- Browser
- Mobile App
- Desktop App

Responsibilities

- Send requests
- Display responses
- Handle user interaction

---

## Server

The server processes requests.

Responsibilities

- Execute business logic
- Authenticate users
- Query databases
- Return responses

Examples

- FastAPI
- Django
- Flask

---

# Request-Response Cycle

```
Browser

↓

HTTP Request

↓

Server

↓

Business Logic

↓

Database

↓

Response

↓

Browser
```

Example

User opens

```
https://example.com/profile
```

Steps

1. Browser sends request
2. Server receives request
3. Database queried
4. Response generated
5. HTML or JSON returned

---

# DNS (Domain Name System)

Humans remember

```
google.com
```

Computers use

```
142.250.xxx.xxx
```

DNS converts

```
Domain

↓

IP Address
```

Example

```
example.com

↓

93.184.216.34
```

---

# URL (Uniform Resource Locator)

Structure

```
https://example.com:443/users/123?active=true
```

Components

Protocol

```
https
```

Domain

```
example.com
```

Port

```
443
```

Path

```
/users/123
```

Query Parameters

```
active=true
```

---

# URI vs URL

URI

General resource identifier.

URL

Specific location of a resource.

Every URL is a URI.

Not every URI is a URL.

---

# HTTP

HyperText Transfer Protocol

A stateless application-layer protocol used for communication between clients and servers.

Characteristics

- Stateless
- Text-based
- Request-Response
- Runs over TCP/IP

---

# HTTPS

HTTP Secure

Uses

```
TLS/SSL
```

Provides

✓ Encryption

✓ Authentication

✓ Integrity

Benefits

- Prevents eavesdropping
- Protects passwords
- Secures APIs

---

# HTTP Request Structure

```
GET /users HTTP/1.1

Host: example.com

Authorization: Bearer token

Content-Type: application/json
```

Contains

- Method
- URL
- Headers
- Body (optional)

---

# HTTP Response Structure

```
HTTP/1.1 200 OK

Content-Type: application/json

{
   "name":"Alice"
}
```

Contains

- Status Code
- Headers
- Body

---

# HTTP Methods

## GET

Retrieve data.

Safe

✓ Yes

Idempotent

✓ Yes

Example

```
GET /users
```

---

## POST

Create new resource.

Safe

❌ No

Idempotent

❌ No

Example

```
POST /users
```

---

## PUT

Replace an existing resource.

Idempotent

✓ Yes

Example

```
PUT /users/10
```

---

## PATCH

Partially update a resource.

Example

```
PATCH /users/10
```

---

## DELETE

Remove a resource.

Example

```
DELETE /users/10
```

Idempotent

✓ Yes

---

## HEAD

Returns only headers.

Useful for

- Health checks
- Metadata

---

## OPTIONS

Returns supported methods.

Used by

- Browsers
- CORS

---

# Safe vs Idempotent Methods

| Method | Safe | Idempotent |
|----------|------|------------|
| GET | ✓ | ✓ |
| HEAD | ✓ | ✓ |
| OPTIONS | ✓ | ✓ |
| POST | ❌ | ❌ |
| PUT | ❌ | ✓ |
| PATCH | ❌ | Usually No |
| DELETE | ❌ | ✓ |

---

# HTTP Status Codes

## 1xx

Informational

Example

```
100 Continue
```

---

## 2xx

Success

```
200 OK

201 Created

202 Accepted

204 No Content
```

---

## 3xx

Redirection

```
301 Moved Permanently

302 Found

304 Not Modified
```

---

## 4xx

Client Errors

```
400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

405 Method Not Allowed

409 Conflict

422 Unprocessable Entity

429 Too Many Requests
```

---

## 5xx

Server Errors

```
500 Internal Server Error

502 Bad Gateway

503 Service Unavailable

504 Gateway Timeout
```

---

# HTTP Headers

Provide metadata.

Common Request Headers

```
Authorization

Content-Type

Accept

User-Agent

Host
```

Common Response Headers

```
Content-Type

Cache-Control

Set-Cookie

Location

Content-Length
```

---

# Content Types (MIME Types)

Common values

```
application/json

text/html

text/plain

multipart/form-data

application/xml

image/png
```

---

# JSON

JavaScript Object Notation

The standard format for APIs.

Example

```json
{
    "id": 1,
    "name": "Alice",
    "skills": [
        "Python",
        "FastAPI"
    ]
}
```

Advantages

✓ Lightweight

✓ Human readable

✓ Language independent

---

# Cookies

Small pieces of data stored by the browser.

Used for

- Authentication
- Preferences
- Tracking

Example

```
Set-Cookie:

session=abc123
```

---

# Sessions

Store user-specific data across requests.

Typical Flow

```
Browser

↓

Session Cookie

↓

Server

↓

Session Store
```

---

# Stateless vs Stateful

Stateless

Each request contains all required information.

Example

REST APIs using JWT.

Stateful

Server stores session information.

Example

Traditional web applications using server-side sessions.

---

# REST

Representational State Transfer

Architectural style for web APIs.

Principles

- Client-Server
- Stateless
- Uniform Interface
- Cacheable
- Layered System

Example

```
GET /users

POST /users

GET /users/1

PUT /users/1

DELETE /users/1
```

---

# REST Resource Naming

Good

```
/users

/orders

/products
```

Avoid

```
/getUsers

/createOrder

/deleteUser
```

Resources should be nouns, while HTTP methods define the action.

---

# REST Best Practices

✓ Use nouns in URLs.

✓ Use HTTP status codes correctly.

✓ Return JSON for APIs.

✓ Keep endpoints consistent.

✓ Version APIs.

Example

```
/api/v1/users
```

---

# Common Web Security Concepts

- HTTPS everywhere
- Input validation
- Authentication
- Authorization
- CSRF protection
- XSS prevention
- SQL injection prevention
- Rate limiting
- Secure cookies

---

# Best Practices

✓ Use HTTPS in production.

✓ Return meaningful status codes.

✓ Validate user input.

✓ Use JSON for APIs.

✓ Design RESTful URLs.

✓ Keep APIs stateless where appropriate.

---

# Common Mistakes

❌ Using GET for data modification.

❌ Returning `200 OK` for every response.

❌ Exposing sensitive information in URLs.

❌ Ignoring HTTP status codes.

❌ Using inconsistent API naming conventions.

---

# Interview Questions

### Easy

1. What is HTTP?
2. Difference between HTTP and HTTPS.
3. What is DNS?
4. What is a URL?
5. Explain the request-response cycle.

---

### Medium

1. Difference between PUT and PATCH.
2. Explain statelessness.
3. What is REST?
4. Difference between cookies and sessions.
5. Explain idempotent HTTP methods.

---

### Hard

1. Design a RESTful API for an e-commerce application.
2. Explain how HTTPS works at a high level.
3. Discuss API versioning strategies.
4. Compare REST and GraphQL.
5. Design a scalable client-server architecture.

---

# Coding Exercises

Easy

- Create a simple HTTP server.
- Parse JSON requests.
- Return different status codes.

Medium

- Design REST endpoints for a blogging application.
- Implement CRUD operations.
- Validate incoming JSON payloads.

Hard

- Build a REST API following REST principles.
- Design versioned APIs.
- Implement pagination, filtering, and sorting.

---

# Module Summary

Web development is built on client-server communication using HTTP/HTTPS. Understanding requests, responses, URLs, DNS, HTTP methods, status codes, cookies, sessions, JSON, and REST principles provides the foundation for building secure, scalable, and maintainable backend applications with Flask, Django, and FastAPI.

---

# Python Developer Knowledge Base
# Module 06 — Web Frameworks
# Part 2 — WSGI, ASGI & Python Concurrency

---

# Why Web Servers Need Interfaces

A Python application cannot communicate directly with a web server.

Example

```
Browser

↓

Nginx

↓

Python Application
```

A standard interface is required.

Python provides

- WSGI
- ASGI

---

# WSGI

## Web Server Gateway Interface

PEP 3333 defines WSGI as the standard interface between web servers and synchronous Python web applications.

Architecture

```
Browser

↓

Nginx

↓

Gunicorn

↓

WSGI

↓

Flask / Django

↓

Database
```

Characteristics

- Synchronous
- Request per worker
- Mature ecosystem
- Excellent for traditional web applications

Supported Frameworks

- Flask
- Django (traditional mode)
- Pyramid

---

# WSGI Request Flow

```
HTTP Request

↓

Web Server

↓

WSGI Server

↓

Python Application

↓

HTTP Response
```

Each request occupies one worker until the response is completed.

---

# WSGI Limitations

Problems with

- WebSockets
- Long-lived connections
- Streaming
- High-concurrency I/O workloads

Worker remains occupied while waiting for I/O.

---

# ASGI

## Asynchronous Server Gateway Interface

ASGI extends WSGI to support asynchronous communication.

Supports

- HTTP
- WebSockets
- Server-Sent Events (SSE)
- Background tasks
- Long-lived connections

Architecture

```
Browser

↓

Nginx

↓

Uvicorn

↓

ASGI

↓

FastAPI

↓

Database
```

---

# ASGI Request Flow

```
Client

↓

ASGI Server

↓

Event Loop

↓

Coroutine

↓

Response
```

While one coroutine waits for I/O, the event loop can schedule another.

---

# WSGI vs ASGI

| Feature | WSGI | ASGI |
|----------|------|------|
| Programming Model | Synchronous | Sync + Async |
| HTTP | Yes | Yes |
| WebSockets | No | Yes |
| Server-Sent Events | Limited | Yes |
| Long-lived Connections | Poor | Excellent |
| Streaming | Limited | Excellent |
| High Concurrency | Moderate | High |
| Frameworks | Flask, Django | FastAPI, Starlette, Django ASGI |

---

# Synchronous Programming

Definition

Tasks execute one after another.

Example

```
Task A

↓

Task B

↓

Task C
```

Python

```python
def fetch_data():

    data = database.query()

    return data
```

Advantages

✓ Simple

✓ Easy debugging

Disadvantages

❌ Blocks while waiting for I/O.

---

# Asynchronous Programming

Definition

Tasks voluntarily yield control while waiting for I/O, allowing other tasks to run.

Example

```
Task A

↓

Waiting...

↓

Task B Executes

↓

Task C Executes

↓

Task A Resumes
```

Python

```python
import asyncio

async def fetch_data():

    await asyncio.sleep(1)

    return "Done"
```

---

# Coroutine

A coroutine is a special function defined with `async def` that can suspend execution with `await`.

Example

```python
async def hello():

    return "Hello"
```

---

# await

`await` pauses the current coroutine until the awaited operation completes.

Example

```python
async def main():

    result = await fetch_data()

    print(result)
```

Only valid inside an `async def` function.

---

# Event Loop

The event loop schedules and runs asynchronous tasks.

Concept

```
Coroutine A

↓

Waiting

↓

Coroutine B Runs

↓

Coroutine C Runs

↓

Coroutine A Continues
```

The event loop enables efficient handling of many I/O-bound operations.

---

# asyncio

Python's standard asynchronous library.

Example

```python
import asyncio

async def greet():

    print("Hello")

asyncio.run(greet())
```

---

# Concurrent Tasks

```python
import asyncio

async def task(name):

    await asyncio.sleep(1)

    print(name)

async def main():

    await asyncio.gather(

        task("A"),

        task("B"),

        task("C")

    )

asyncio.run(main())
```

All three tasks are scheduled concurrently.

---

# Blocking vs Non-Blocking

Blocking

```
Read File

↓

Wait

↓

Continue
```

Non-Blocking

```
Read File

↓

Continue Other Work

↓

Resume When Ready
```

---

# I/O-bound vs CPU-bound

## I/O-bound

Examples

- Database queries
- API calls
- File access
- Network requests

Async programming performs very well here.

---

## CPU-bound

Examples

- Image processing
- Encryption
- Scientific computing
- Machine learning training

Async alone does not speed up CPU-heavy computation.

---

# Threads

Definition

Multiple threads execute within one process.

Advantages

- Shared memory
- Good for many I/O-bound tasks

Disadvantages

- Synchronization complexity
- Global Interpreter Lock (GIL) affects CPU-bound threading in CPython

---

# Processes

Each process has independent memory.

Advantages

- True parallel execution
- Good for CPU-bound work

Disadvantages

- Higher memory usage
- More expensive process creation

---

# Async vs Threads vs Processes

| Feature | Async | Threads | Processes |
|----------|--------|----------|------------|
| I/O-bound | Excellent | Good | Good |
| CPU-bound | Poor | Limited by GIL | Excellent |
| Memory Usage | Low | Medium | High |
| Parallel CPU Execution | No | Limited | Yes |
| Context Switch Cost | Very Low | Medium | High |

---

# Choosing the Right Model

Use Async

- API calls
- Database access
- WebSockets
- Chat applications

Use Threads

- Blocking libraries without async support
- Moderate I/O workloads

Use Processes

- Data science
- Image processing
- Video encoding
- Numerical computation

---

# Uvicorn

ASGI server.

Designed for

- FastAPI
- Starlette
- Django ASGI

Run application

```bash
uvicorn main:app --reload
```

---

# Gunicorn

Production WSGI server.

Example

```bash
gunicorn app:app
```

Can also manage ASGI workers when paired with an ASGI worker class (e.g., Uvicorn workers).

---

# Hypercorn

Supports

- ASGI
- HTTP/2
- WebSockets

Alternative to Uvicorn for ASGI applications.

---

# Daphne

ASGI server maintained by the Django Channels project.

Often used with

- Django Channels
- WebSockets

---

# FastAPI Async Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def home():

    return {

        "message": "Hello"
    }
```

---

# Flask Example

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():

    return "Hello"
```

Traditional Flask request handlers are synchronous.

---

# Django

Supports

- WSGI
- ASGI

Modern Django allows asynchronous views and ASGI deployment while still supporting synchronous code.

---

# Production Architecture

```
Client

↓

Nginx

↓

Load Balancer

↓

Uvicorn Workers

↓

FastAPI

↓

Redis

↓

PostgreSQL
```

---

# Performance Considerations

WSGI

Best for

- Traditional websites
- CRUD applications
- Lower concurrency

ASGI

Best for

- APIs
- Real-time systems
- Chat applications
- Streaming
- High-concurrency services

---

# Common Mistakes

❌ Using async for CPU-intensive tasks expecting speedups.

❌ Blocking the event loop with synchronous I/O.

❌ Forgetting to `await` asynchronous functions.

❌ Mixing blocking database drivers in async applications.

❌ Creating unnecessary threads in async code.

---

# Best Practices

✓ Use async primarily for I/O-bound workloads.

✓ Use asynchronous database and HTTP libraries in async applications.

✓ Offload CPU-intensive work to worker processes or task queues.

✓ Keep coroutines small and focused.

✓ Measure performance before optimizing.

---

# Interview Questions

### Easy

1. What is WSGI?
2. What is ASGI?
3. Difference between sync and async programming.
4. What is a coroutine?
5. What is an event loop?

---

### Medium

1. Compare WSGI and ASGI.
2. Explain `async` and `await`.
3. When should you use threads instead of async?
4. Explain asyncio.
5. Compare threads and processes.

---

### Hard

1. Design a high-concurrency chat application.
2. Explain how the event loop schedules coroutines.
3. Why is async unsuitable for CPU-bound work?
4. Compare Gunicorn, Uvicorn, Hypercorn, and Daphne.
5. Design a scalable FastAPI deployment architecture.

---

# Coding Exercises

Easy

- Write an async function using `asyncio.sleep()`.
- Run multiple coroutines with `asyncio.gather()`.

Medium

- Build an asynchronous HTTP endpoint.
- Compare synchronous and asynchronous API performance.

Hard

- Build a WebSocket server.
- Integrate async database access with FastAPI.
- Design a real-time notification service.

---

# Module Summary

WSGI and ASGI define how Python web applications communicate with web servers. WSGI powers traditional synchronous frameworks, while ASGI enables asynchronous applications with support for WebSockets, streaming, and high-concurrency I/O. Understanding coroutines, the event loop, threads, processes, and async programming is essential for building scalable modern Python backend systems using FastAPI and contemporary versions of Django.

---


# Python Developer Knowledge Base
# Module 06 — Web Frameworks
# Part 3 — Flask Framework

---

# Introduction to Flask

Flask is a lightweight Python web framework based on the WSGI standard.

Official Features

- Lightweight
- Extensible
- Minimal
- Flexible
- Easy to learn

Unlike Django, Flask provides only the core components. Developers choose additional libraries based on project requirements.

---

# Why Flask?

Advantages

✓ Simple syntax

✓ Flexible architecture

✓ Minimal boilerplate

✓ Excellent for REST APIs

✓ Large extension ecosystem

✓ Easy integration with SQLAlchemy

Common Use Cases

- REST APIs
- Microservices
- Backend services
- Internal tools
- Machine Learning APIs

---

# Flask Architecture

Flask follows a microframework architecture.

```
Browser

↓

Flask Application

↓

Business Logic

↓

Database

↓

Response
```

Main Components

- Routes
- Views
- Templates
- Extensions
- Configuration
- WSGI Server

---

# Installation

```bash
pip install flask
```

Verify

```python
import flask

print(flask.__version__)
```

---

# Creating a Flask Application

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():

    return "Hello Flask"

if __name__ == "__main__":

    app.run(debug=True)
```

Run

```bash
python app.py
```

---

# Flask Request Lifecycle

```
Browser

↓

WSGI Server

↓

Flask

↓

Route

↓

View Function

↓

Response

↓

Browser
```

---

# Routing

Routes map URLs to Python functions.

```python
@app.route("/about")

def about():

    return "About Page"
```

---

# Dynamic Routes

```python
@app.route("/user/<name>")

def user(name):

    return f"Hello {name}"
```

Example

```
/user/Alice
```

Output

```
Hello Alice
```

---

# Route Converters

```python
@app.route("/user/<int:id>")
```

Available Converters

- string
- int
- float
- path
- uuid

---

# HTTP Methods

```python
@app.route("/users", methods=["GET"])
```

Multiple Methods

```python
@app.route(

    "/users",

    methods=["GET", "POST"]
)
```

---

# Request Object

Provides access to incoming request data.

```python
from flask import request

@app.route("/login", methods=["POST"])

def login():

    username = request.form["username"]

    return username
```

Useful Attributes

- request.args
- request.form
- request.json
- request.files
- request.headers
- request.cookies

---

# Query Parameters

Example

```
/search?q=python
```

```python
query = request.args.get("q")
```

---

# JSON Requests

```python
data = request.get_json()

name = data["name"]
```

---

# Response Object

```python
from flask import jsonify

@app.route("/api")

def api():

    return jsonify(

        {

            "status":"success"

        }

    )
```

---

# Returning Status Codes

```python
return jsonify(

    {"error":"Not Found"}

),404
```

---

# Redirects

```python
from flask import redirect

return redirect("/home")
```

---

# URL Generation

```python
from flask import url_for

url_for("home")
```

Benefits

- Avoid hardcoded URLs
- Easier refactoring

---

# Templates

Flask uses

Jinja2

Example

```python
return render_template(

    "index.html",

    username="Alice"
)
```

---

# Jinja2 Variables

HTML

```html
<h1>{{ username }}</h1>
```

---

# Loops

```html
{% for user in users %}

<p>{{ user }}</p>

{% endfor %}
```

---

# Conditions

```html
{% if logged_in %}

Welcome

{% endif %}
```

---

# Template Inheritance

Base Template

```html
{% block content %}

{% endblock %}
```

Child Template

```html
{% extends "base.html" %}
```

---

# Static Files

Directory

```
static/

CSS

JS

Images
```

Example

```html
<link

rel="stylesheet"

href="{{ url_for('static',

filename='style.css') }}"
>
```

---

# Blueprints

Large applications should organize routes into Blueprints.

Example

```python
from flask import Blueprint

users = Blueprint(

    "users",

    __name__
)
```

Register

```python
app.register_blueprint(users)
```

Benefits

- Modular code
- Better maintainability
- Easier testing

---

# Application Factory Pattern

Instead of creating a global app instance, use a factory.

```python
from flask import Flask

def create_app():

    app = Flask(__name__)

    return app
```

Benefits

- Easier testing
- Multiple configurations
- Improved scalability

---

# Configuration

```python
app.config["SECRET_KEY"]="secret"

app.config["DEBUG"]=True
```

Environment Variables

```python
import os

app.config["SECRET_KEY"]=os.getenv(

    "SECRET_KEY"
)
```

Avoid hardcoding secrets in source code.

---

# Error Handling

```python
@app.errorhandler(404)

def not_found(error):

    return "Page Not Found",404
```

---

# Logging

```python
import logging

app.logger.info(

    "Application Started"
)
```

Use structured logging in production.

---

# Database Integration

Common Choices

- SQLAlchemy
- Flask-SQLAlchemy
- SQLite
- PostgreSQL
- MySQL

Example

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

---

# Flask Extensions

Popular Extensions

- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-JWT-Extended
- Flask-CORS
- Flask-Mail
- Flask-WTF

Extensions keep the core framework lightweight.

---

# Authentication

Session-based

```
Login

↓

Cookie

↓

Session
```

Token-based

```
JWT

↓

Authorization Header
```

---

# Middleware

Flask provides request hooks.

Before Request

```python
@app.before_request

def before():

    pass
```

After Request

```python
@app.after_request

def after(response):

    return response
```

Useful for

- Logging
- Authentication
- Metrics

---

# File Upload

```python
file=request.files["image"]

file.save("uploads/image.png")
```

Always validate file type and size.

---

# Testing Flask

Install

```bash
pip install pytest
```

Example

```python
def test_home(client):

    response=client.get("/")

    assert response.status_code==200
```

---

# Production Deployment

Development

```
flask run
```

Production

```
Nginx

↓

Gunicorn

↓

Flask

↓

Database
```

Never use the built-in development server in production.

---

# Project Structure

```
project/

│

├── app/

│   ├── __init__.py

│   ├── routes.py

│   ├── models.py

│   ├── services.py

│   ├── templates/

│   ├── static/

│

├── migrations/

├── tests/

├── config.py

├── requirements.txt

└── run.py
```

---

# Best Practices

✓ Use the Application Factory pattern.

✓ Organize code with Blueprints.

✓ Keep business logic separate from routes.

✓ Validate user input.

✓ Use environment variables for configuration.

✓ Return JSON for APIs.

✓ Add automated tests.

✓ Use Gunicorn behind Nginx in production.

---

# Common Mistakes

❌ Putting all routes in a single file.

❌ Hardcoding secrets.

❌ Mixing database logic with view functions.

❌ Using the development server in production.

❌ Not handling exceptions gracefully.

❌ Trusting uploaded files without validation.

---

# Interview Questions

### Easy

1. What is Flask?
2. Why is Flask called a microframework?
3. What is routing?
4. What is Jinja2?
5. What are Blueprints?

---

### Medium

1. Explain the Flask request lifecycle.
2. What is the Application Factory pattern?
3. Difference between `request.args` and `request.form`.
4. How do you organize a large Flask application?
5. Explain Flask extensions.

---

### Hard

1. Design a production-ready Flask application.
2. Compare Flask and Django.
3. Explain WSGI in the context of Flask.
4. Implement JWT authentication in Flask.
5. Optimize a Flask application handling high traffic.

---

# Coding Exercises

Easy

- Create routes for CRUD operations.
- Accept query parameters.
- Return JSON responses.

Medium

- Build a simple blog application.
- Add SQLAlchemy integration.
- Create modular Blueprints.

Hard

- Implement JWT authentication.
- Build a REST API with pagination and filtering.
- Deploy a Flask application using Gunicorn and Nginx.

---

# Module Summary

Flask is a lightweight, extensible web framework built on WSGI. It provides routing, request handling, template rendering, and integration with a rich ecosystem of extensions while leaving architectural decisions to the developer. Production-ready Flask applications use modular Blueprints, the Application Factory pattern, SQLAlchemy for database access, robust testing, and deployment behind a production WSGI server such as Gunicorn.

---

# Python Developer Knowledge Base
# Module 06 — Web Frameworks
# Part 4 — Django Framework

---

# Introduction to Django

Django is a high-level Python web framework that follows the **"batteries included"** philosophy.

Unlike Flask, Django comes with many built-in features.

- ORM
- Authentication
- Admin Panel
- Session Management
- Middleware
- Security Features
- Template Engine
- URL Routing
- Form Handling

Official Goals

- Rapid Development
- Clean Design
- Reusability
- Security
- Scalability

---

# Why Django?

Advantages

✓ Built-in ORM

✓ Automatic Admin Interface

✓ Authentication System

✓ Excellent Security

✓ Scalable Architecture

✓ Large Community

✓ Rich Ecosystem

Common Use Cases

- Enterprise Applications
- E-commerce
- ERP Systems
- CMS
- SaaS Platforms
- Social Networks

---

# Django Architecture

Django follows the **MVT (Model-View-Template)** architecture.

```
Browser

↓

URL Dispatcher

↓

View

↓

Model

↓

Database

↓

View

↓

Template

↓

Response
```

---

# MVT Components

## Model

Represents application data.

Responsible for

- Database Tables
- Validation
- Relationships
- Business Data

---

## View

Processes requests.

Responsible for

- Business Logic
- Database Queries
- Response Generation

---

## Template

Responsible for presentation.

Uses

- HTML
- CSS
- JavaScript
- Django Template Language (DTL)

---

# Django Project Structure

```
myproject/

│

├── manage.py

├── myproject/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   ├── wsgi.py

│

├── app1/

├── app2/

├── templates/

├── static/

└── media/
```

---

# Creating a Project

```bash
django-admin startproject myproject
```

Run

```bash
python manage.py runserver
```

---

# Creating an App

```bash
python manage.py startapp blog
```

Project

↓

Contains multiple apps.

---

# Django Request Lifecycle

```
Browser

↓

Web Server

↓

WSGI / ASGI

↓

urls.py

↓

View

↓

Model

↓

Database

↓

Template

↓

Response
```

---

# URL Routing

```python
from django.urls import path

from . import views

urlpatterns = [

    path("", views.home),

]
```

---

# Views

Function-Based View

```python
from django.http import HttpResponse

def home(request):

    return HttpResponse("Hello Django")
```

---

# Rendering Templates

```python
from django.shortcuts import render

def home(request):

    return render(

        request,

        "home.html"
    )
```

---

# Dynamic URLs

```python
path(

    "user/<int:id>/",

    views.profile
)
```

View

```python
def profile(request,id):

    return HttpResponse(id)
```

---

# Templates

Example

```html
<h1>{{ username }}</h1>
```

Loop

```html
{% for user in users %}

{{ user }}

{% endfor %}
```

Condition

```html
{% if logged_in %}

Welcome

{% endif %}
```

---

# Static Files

Directory

```
static/

css/

js/

images/
```

Load

```html
{% load static %}
```

---

# Models

Example

```python
from django.db import models

class Employee(models.Model):

    name=models.CharField(

        max_length=100

    )

    salary=models.IntegerField()
```

Each model maps to a database table.

---

# Migrations

Create migration

```bash
python manage.py makemigrations
```

Apply migration

```bash
python manage.py migrate
```

---

# Django ORM

Insert

```python
Employee.objects.create(

    name="Alice",

    salary=90000
)
```

Retrieve

```python
Employee.objects.all()
```

Filter

```python
Employee.objects.filter(

    salary__gt=50000
)
```

Update

```python
employee.salary=95000

employee.save()
```

Delete

```python
employee.delete()
```

---

# QuerySet

A QuerySet represents a lazy database query.

Examples

```python
Employee.objects.all()

Employee.objects.filter()

Employee.objects.exclude()
```

QuerySets are evaluated only when needed.

---

# Relationships

One-to-One

```python
OneToOneField
```

One-to-Many

```python
ForeignKey
```

Many-to-Many

```python
ManyToManyField
```

---

# Admin Panel

Create superuser

```bash
python manage.py createsuperuser
```

Register model

```python
from django.contrib import admin

from .models import Employee

admin.site.register(Employee)
```

Access

```
/admin
```

---

# Forms

Example

```python
from django import forms

class LoginForm(

    forms.Form

):

    username=forms.CharField()

    password=forms.CharField(

        widget=forms.PasswordInput
    )
```

Benefits

- Validation
- Security
- Error Handling

---

# Authentication

Built-in User Model

Features

- Login
- Logout
- Password Hashing
- Permissions
- Groups

Login

```python
from django.contrib.auth import authenticate

user=authenticate(

    username=username,

    password=password
)
```

---

# Authorization

Permissions

```python
user.has_perm()
```

Groups

```
Admin

Manager

Employee
```

---

# Sessions

Django stores sessions using

- Database
- Cache
- File
- Signed Cookies

Session Example

```python
request.session["user"]=1
```

---

# Middleware

Middleware processes requests and responses.

Examples

- Authentication
- Sessions
- Security
- CSRF
- Logging

Flow

```
Request

↓

Middleware

↓

View

↓

Middleware

↓

Response
```

---

# Signals

Signals enable event-driven programming.

Example

```
User Created

↓

Send Welcome Email
```

Signal

```python
post_save
```

Common Signals

- pre_save
- post_save
- pre_delete
- post_delete

---

# Function-Based Views (FBV)

Advantages

✓ Simple

✓ Easy to understand

Good for

Small projects.

---

# Class-Based Views (CBV)

Advantages

✓ Reusable

✓ Less code duplication

Example

```python
from django.views import View
```

Generic Views

- ListView
- DetailView
- CreateView
- UpdateView
- DeleteView

---

# Django Security Features

Built-in Protection

✓ CSRF

✓ SQL Injection (ORM)

✓ XSS escaping in templates

✓ Clickjacking protection

✓ Password hashing

✓ Secure session handling

Developers still need to validate input and configure security settings correctly.

---

# Django REST Framework (Introduction)

DRF is the standard toolkit for building REST APIs with Django.

Key Components

- Serializers
- ViewSets
- Routers
- Authentication
- Permissions

Example

```python
from rest_framework.views import APIView
```

(Complete DRF coverage will be provided in the API Development module.)

---

# Django Deployment

Typical Architecture

```
Client

↓

Nginx

↓

Gunicorn / Uvicorn

↓

Django

↓

PostgreSQL

↓

Redis
```

---

# Project Organization

```
project/

│

├── apps/

│   ├── users/

│   ├── orders/

│   ├── inventory/

│

├── templates/

├── static/

├── media/

├── requirements.txt

├── manage.py

└── settings.py
```

---

# Best Practices

✓ Keep apps focused on a single responsibility.

✓ Use the ORM instead of raw SQL where appropriate.

✓ Use environment variables for secrets.

✓ Enable HTTPS in production.

✓ Optimize database queries with `select_related()` and `prefetch_related()`.

✓ Use custom user models when required early in the project.

✓ Write automated tests.

---

# Common Mistakes

❌ Putting all logic inside views.

❌ Ignoring migrations.

❌ N+1 database queries.

❌ Hardcoding secrets.

❌ Disabling CSRF protection without understanding the risks.

❌ Mixing business logic with templates.

---

# Interview Questions

### Easy

1. What is Django?
2. Explain MVT architecture.
3. What is a Django app?
4. What is the ORM?
5. What are migrations?

---

### Medium

1. Difference between FBV and CBV.
2. Explain Django's request lifecycle.
3. What are QuerySets?
4. Explain middleware.
5. How does Django authentication work?

---

### Hard

1. Design a scalable Django application.
2. Optimize slow ORM queries.
3. Compare Flask and Django.
4. Explain `select_related()` vs `prefetch_related()`.
5. Design a multi-app Django project.

---

# Coding Exercises

Easy

- Create a Django project.
- Build a model and migrate it.
- Create CRUD views.

Medium

- Build a blog application.
- Add authentication.
- Create an admin dashboard.

Hard

- Build a production-ready e-commerce backend.
- Optimize ORM performance.
- Implement custom middleware and permissions.

---

# Module Summary

Django is a full-featured Python web framework designed for rapid development and scalable applications. Its MVT architecture, ORM, authentication system, middleware, admin interface, and built-in security features allow developers to build complex applications with minimal external dependencies. Mastering Django's request lifecycle, models, QuerySets, migrations, authentication, and deployment is essential for professional Python backend development.

---

# Python Developer Knowledge Base
# Module 06 — Web Frameworks
# Part 5 — FastAPI Framework

---

# Introduction to FastAPI

FastAPI is a modern, high-performance Python web framework for building APIs.

It is built on

- Starlette (Web Framework)
- Pydantic (Data Validation)
- ASGI (Asynchronous Interface)

Main Goals

- High Performance
- Automatic Validation
- Automatic Documentation
- Type Safety
- Developer Productivity

---

# Why FastAPI?

Advantages

✓ Extremely fast

✓ Native async support

✓ Automatic Swagger UI

✓ Automatic OpenAPI generation

✓ Type hint based validation

✓ Excellent editor support

✓ Easy dependency injection

Common Use Cases

- REST APIs
- Microservices
- AI/ML APIs
- Backend services
- Real-time applications

---

# FastAPI Architecture

```
Client

↓

Uvicorn

↓

FastAPI

↓

Router

↓

Dependency Injection

↓

Business Logic

↓

Database

↓

JSON Response
```

---

# Installation

```bash
pip install fastapi uvicorn
```

Run

```bash
uvicorn main:app --reload
```

---

# Creating Your First Application

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def home():

    return {

        "message": "Hello FastAPI"

    }
```

---

# Request Lifecycle

```
HTTP Request

↓

ASGI Server

↓

Middleware

↓

Router

↓

Dependencies

↓

Path Operation

↓

Response

↓

Client
```

---

# Path Operations

GET

```python
@app.get("/users")
```

POST

```python
@app.post("/users")
```

PUT

```python
@app.put("/users/{id}")
```

PATCH

```python
@app.patch("/users/{id}")
```

DELETE

```python
@app.delete("/users/{id}")
```

---

# Path Parameters

```python
@app.get("/users/{user_id}")

async def get_user(

    user_id:int

):

    return {

        "id":user_id

    }
```

Automatic validation

```
/users/abc

↓

422 Validation Error
```

---

# Query Parameters

```
GET /users?page=1&limit=10
```

```python
@app.get("/users")

async def users(

    page:int=1,

    limit:int=10

):

    return {

        "page":page,

        "limit":limit

    }
```

---

# Optional Query Parameters

```python
from typing import Optional

@app.get("/search")

async def search(

    q:Optional[str]=None

):

    return {

        "query":q

    }
```

---

# Request Body

FastAPI automatically validates request bodies using Pydantic models.

```python
from pydantic import BaseModel

class User(

    BaseModel

):

    name:str

    age:int
```

Endpoint

```python
@app.post("/users")

async def create_user(

    user:User

):

    return user
```

---

# Pydantic Validation

Example

```python
from pydantic import BaseModel, Field

class Product(

    BaseModel

):

    name:str

    price:float=Field(gt=0)

    quantity:int=Field(ge=0)
```

Validation happens automatically.

---

# Response Models

```python
class UserResponse(

    BaseModel

):

    id:int

    name:str

@app.get(

    "/users/{id}",

    response_model=UserResponse

)
```

Benefits

✓ Response validation

✓ API documentation

✓ Field filtering

---

# Status Codes

```python
from fastapi import status

@app.post(

    "/users",

    status_code=status.HTTP_201_CREATED

)
```

---

# Headers

```python
from fastapi import Header

@app.get("/")

async def home(

    token:str=Header()

):

    return token
```

---

# Cookies

```python
from fastapi import Cookie

@app.get("/")

async def read_cookie(

    session:str=Cookie()

):
    return session
```

---

# Dependency Injection

One of FastAPI's most powerful features.

```python
from fastapi import Depends

def get_db():

    return "database"

@app.get("/")

async def home(

    db=Depends(get_db)

):

    return db
```

Use Cases

- Database sessions
- Authentication
- Configuration
- Logging
- Shared services

---

# APIRouter

Large applications organize endpoints into routers.

```python
from fastapi import APIRouter

router=APIRouter()

@router.get("/users")

async def users():

    return []
```

Main application

```python
app.include_router(router)
```

---

# Background Tasks

```python
from fastapi import BackgroundTasks

@app.post("/email")

async def send(

    background:BackgroundTasks

):

    background.add_task(

        send_email
    )
```

Useful for

- Emails
- Notifications
- Logging
- Report generation

---

# File Upload

```python
from fastapi import UploadFile, File

@app.post("/upload")

async def upload(

    file:UploadFile=File(...)

):

    return {

        "filename":file.filename

    }
```

---

# Form Data

```python
from fastapi import Form

@app.post("/login")

async def login(

    username:str=Form(...),

    password:str=Form(...)

):
```

---

# Middleware

```python
@app.middleware("http")

async def log_request(

    request,

    call_next

):

    response=await call_next(request)

    return response
```

Common Uses

- Logging
- Authentication
- Timing
- Metrics
- CORS

---

# Exception Handling

```python
from fastapi import HTTPException

@app.get("/users/{id}")

async def user(id:int):

    if id==0:

        raise HTTPException(

            status_code=404,

            detail="User not found"

        )
```

---

# CORS

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_methods=["*"],

    allow_headers=["*"]

)
```

In production, specify trusted origins instead of `"*"`.

---

# WebSockets

```python
from fastapi import WebSocket

@app.websocket("/ws")

async def websocket(

    websocket:WebSocket

):

    await websocket.accept()

    while True:

        data=await websocket.receive_text()

        await websocket.send_text(data)
```

Applications

- Chat
- Live dashboards
- Notifications
- Games

---

# OpenAPI Documentation

Automatically generated.

Swagger UI

```
/docs
```

ReDoc

```
/redoc
```

No additional configuration required for basic APIs.

---

# Async Database Integration

Common libraries

- SQLAlchemy 2.x (async support)
- asyncpg
- Motor (MongoDB)
- aiomysql

Example pattern

```python
async with session.begin():

    ...
```

---

# Authentication

Common approaches

- JWT
- OAuth2
- API Keys

FastAPI provides utilities through its security modules.

---

# OAuth2 Example

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme=

OAuth2PasswordBearer(

    tokenUrl="token"
)
```

---

# Testing

```python
from fastapi.testclient import TestClient

client=TestClient(app)

def test_home():

    response=client.get("/")

    assert response.status_code==200
```

---

# Project Structure

```
app/

│

├── main.py

├── routers/

├── models/

├── schemas/

├── services/

├── database/

├── dependencies/

├── middleware/

├── core/

├── tests/

└── config.py
```

---

# Production Deployment

```
Client

↓

Nginx

↓

Load Balancer

↓

Uvicorn Workers

↓

FastAPI

↓

Redis

↓

PostgreSQL
```

Common production command

```bash
gunicorn app.main:app \
    -k uvicorn.workers.UvicornWorker
```

---

# Performance Best Practices

✓ Prefer async endpoints for I/O-bound work.

✓ Use connection pooling.

✓ Validate data with Pydantic.

✓ Keep business logic outside route handlers.

✓ Paginate large datasets.

✓ Cache frequently accessed data.

✓ Use dependency injection for shared resources.

✓ Monitor response times and database queries.

---

# Common Mistakes

❌ Blocking the event loop with synchronous I/O.

❌ Opening a new database connection for every request.

❌ Returning raw ORM objects without serialization.

❌ Using global mutable state.

❌ Allowing all CORS origins in production.

❌ Putting business logic directly inside endpoints.

---

# Interview Questions

### Easy

1. What is FastAPI?
2. Why is FastAPI faster than many traditional frameworks?
3. What is Pydantic?
4. What is dependency injection?
5. What is APIRouter?

---

### Medium

1. Explain the FastAPI request lifecycle.
2. Difference between path and query parameters.
3. How does FastAPI perform validation?
4. Explain BackgroundTasks.
5. How does automatic OpenAPI generation work?

---

### Hard

1. Design a scalable FastAPI microservice.
2. Compare FastAPI, Flask, and Django.
3. Implement JWT authentication with refresh tokens.
4. Design a WebSocket-based notification service.
5. Optimize a high-throughput FastAPI application.

---

# Coding Exercises

Easy

- Create CRUD endpoints.
- Validate request bodies with Pydantic.
- Return custom status codes.

Medium

- Build a blog API using APIRouter and SQLAlchemy.
- Add JWT authentication.
- Upload and validate files.

Hard

- Build a real-time chat server using WebSockets.
- Implement async PostgreSQL integration.
- Design a production-ready FastAPI project with dependency injection, caching, and background tasks.

---

# Module Summary

FastAPI is a modern ASGI framework designed for building high-performance APIs. It combines asynchronous request handling, automatic validation through Pydantic, dependency injection, OpenAPI documentation, and first-class support for async programming. When paired with Uvicorn, SQLAlchemy, Redis, and PostgreSQL, FastAPI provides a robust foundation for scalable, production-grade backend systems.

---

# Python Developer Knowledge Base
# Module 06 — Web Frameworks
# Part 6 — Advanced Web Framework Concepts

---

# Module Overview

This section covers production-ready concepts common to Flask, Django, and FastAPI.

Topics

- Middleware
- CORS
- Cookies & Sessions
- CSRF
- Authentication
- Authorization
- JWT
- OAuth2
- Password Hashing
- RBAC
- File Uploads
- Background Tasks
- Celery
- WebSockets
- Server-Sent Events
- API Versioning
- Rate Limiting
- Logging
- Monitoring
- Security Best Practices

---

# Middleware

## What is Middleware?

Middleware is software that executes before and/or after the request reaches the application.

```
Client

↓

Middleware

↓

Application

↓

Middleware

↓

Response
```

Common Uses

- Logging
- Authentication
- Authorization
- CORS
- Compression
- Metrics
- Rate Limiting

---

# Middleware Execution Flow

```
Incoming Request

↓

Authentication

↓

Logging

↓

Business Logic

↓

Logging

↓

Response
```

Every request passes through middleware.

---

# CORS

## Cross-Origin Resource Sharing

Browsers block requests made from different origins unless explicitly allowed.

Example

Frontend

```
http://localhost:3000
```

Backend

```
http://localhost:8000
```

Different origins require CORS configuration.

---

# CORS Configuration (FastAPI)

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
    allow_credentials=True
)
```

Avoid using `"*"` in production when credentials are involved.

---

# Cookies

Cookies are stored in the browser.

Example

```
Set-Cookie

session=abc123
```

Common Uses

- Sessions
- Preferences
- Authentication

Attributes

- HttpOnly
- Secure
- SameSite
- Max-Age
- Domain
- Path

---

# Sessions

Sessions store user-specific data across requests.

Typical Flow

```
Browser

↓

Session Cookie

↓

Server

↓

Session Store
```

Session Stores

- Database
- Redis
- Memory
- Files

---

# Cookies vs Sessions

| Cookies | Sessions |
|----------|----------|
| Stored in browser | Stored on server |
| Limited size | Larger storage |
| Can be modified by client | Controlled by server |
| Sent with each request | Identified by session ID |

---

# CSRF

## Cross-Site Request Forgery

An attacker tricks an authenticated user into performing unintended actions.

Example

```
User logged into bank

↓

Visits malicious website

↓

Hidden form submits transfer request
```

Protection

- CSRF Tokens
- SameSite Cookies
- Origin Validation
- Referer Validation

Django provides built-in CSRF protection.

---

# Authentication

Authentication answers:

> Who are you?

Examples

- Username & Password
- API Keys
- JWT
- OAuth2
- SSO
- Biometrics

---

# Authorization

Authorization answers:

> What are you allowed to do?

Examples

```
Admin

↓

Create User
```

```
Customer

↓

View Orders
```

Authentication always happens before authorization.

---

# Authentication Flow

```
User

↓

Login

↓

Verify Credentials

↓

Generate Token / Session

↓

Client Stores Token

↓

Future Requests

↓

Protected Resource
```

---

# JWT

## JSON Web Token

A compact, signed token used for stateless authentication.

Structure

```
Header

.

Payload

.

Signature
```

Example

```
xxxxx.yyyyy.zzzzz
```

Payload

```json
{
  "user_id": 15,
  "role": "admin"
}
```

Do not store sensitive information in JWT payloads.

---

# JWT Authentication Flow

```
Login

↓

JWT Generated

↓

Client Stores Token

↓

Authorization Header

↓

Server Verifies Signature

↓

Access Granted
```

Authorization Header

```
Authorization: Bearer <token>
```

---

# Access Tokens vs Refresh Tokens

Access Token

- Short lifetime
- Used for API requests

Refresh Token

- Longer lifetime
- Used to obtain a new access token

This limits exposure if an access token is compromised.

---

# OAuth2

OAuth2 allows users to authorize third-party applications without sharing passwords.

Example

```
Login with Google

↓

Google Authenticates User

↓

Application Receives Access Token
```

Common Grant Types

- Authorization Code
- Client Credentials
- Device Authorization
- Refresh Token

Authorization Code with PKCE is recommended for public clients.

---

# Password Hashing

Never store plain text passwords.

Incorrect

```
password123
```

Correct

```
$2b$12$...
```

Recommended Algorithms

- bcrypt
- Argon2
- scrypt

Avoid fast hashing algorithms such as MD5 or SHA-1 for password storage.

---

# Role-Based Access Control (RBAC)

Example Roles

```
Admin

Manager

Employee

Customer
```

Permissions

| Role | Read | Write | Delete |
|------|------|--------|---------|
| Admin | ✓ | ✓ | ✓ |
| Manager | ✓ | ✓ | ✗ |
| Customer | ✓ | ✗ | ✗ |

---

# File Uploads

Typical Flow

```
Client

↓

Upload

↓

Validate

↓

Virus Scan (optional)

↓

Storage

↓

Database
```

Validation

- File Type
- File Size
- MIME Type
- Extension

Store uploaded files outside the application source directory when possible.

---

# Static Files vs Media Files

Static Files

- CSS
- JavaScript
- Images
- Fonts

Media Files

- User uploads
- Documents
- Videos
- Profile pictures

---

# Background Tasks

Used for operations that should not delay the response.

Examples

- Sending Emails
- Notifications
- Image Processing
- Report Generation

---

# Celery

Celery is a distributed task queue.

Architecture

```
Application

↓

Message Broker

↓

Celery Worker

↓

Task Execution
```

Message Brokers

- Redis
- RabbitMQ

---

# WebSockets

HTTP

```
Request

↓

Response

↓

Connection Closed
```

WebSocket

```
Connection

↓

Persistent

↓

Bidirectional Communication
```

Applications

- Chat
- Multiplayer Games
- Live Dashboards
- Notifications

---

# Server-Sent Events (SSE)

Server pushes updates to the client over a single HTTP connection.

Characteristics

- One-way communication
- Simpler than WebSockets
- Good for live notifications and dashboards

---

# API Versioning

Why?

Avoid breaking existing clients.

Examples

URI Versioning

```
/api/v1/users
```

Header Versioning

```
Accept: application/vnd.company.v2+json
```

Query Parameter Versioning

```
/users?version=2
```

URI versioning is the most common and easiest to understand.

---

# Rate Limiting

Purpose

Prevent abuse and protect system resources.

Examples

```
100 requests/minute
```

Algorithms

- Token Bucket
- Leaky Bucket
- Fixed Window
- Sliding Window

Implement rate limiting at the API gateway or application layer.

---

# Logging

Record application events.

Levels

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Good Logs Include

- Timestamp
- Request ID
- User ID (if appropriate)
- Endpoint
- Status Code
- Duration

Avoid logging secrets or sensitive personal data.

---

# Monitoring

Track application health.

Monitor

- CPU
- Memory
- Response Time
- Error Rate
- Request Rate
- Database Performance
- Cache Hit Ratio

Popular Tools

- Prometheus
- Grafana
- ELK Stack
- OpenTelemetry

---

# Security Best Practices

✓ Use HTTPS everywhere.

✓ Validate all user input.

✓ Escape output where required.

✓ Use parameterized SQL queries.

✓ Hash passwords with bcrypt or Argon2.

✓ Rotate secrets regularly.

✓ Keep dependencies updated.

✓ Enable security headers.

✓ Apply least privilege.

✓ Implement proper logging and monitoring.

---

# Production Architecture

```
Client

↓

CDN

↓

Load Balancer

↓

Nginx

↓

Application Servers

↓

Redis

↓

PostgreSQL

↓

Object Storage

↓

Monitoring
```

---

# Common Mistakes

❌ Storing passwords in plain text.

❌ Trusting client input.

❌ Disabling CSRF protection unnecessarily.

❌ Allowing unrestricted CORS.

❌ Long-lived JWTs without refresh tokens.

❌ No rate limiting.

❌ Logging sensitive information.

❌ Running background jobs inside request handlers.

---

# Interview Questions

### Easy

1. What is middleware?
2. Difference between authentication and authorization.
3. What is CORS?
4. Explain JWT.
5. What is CSRF?

---

### Medium

1. Compare JWT and session-based authentication.
2. Explain OAuth2.
3. Why should passwords be hashed?
4. Compare WebSockets and SSE.
5. Explain Celery architecture.

---

### Hard

1. Design a secure authentication system for a SaaS platform.
2. Implement RBAC for an enterprise application.
3. Design API versioning for a public API.
4. Build a scalable notification system using WebSockets.
5. Design a rate-limiting solution for millions of API requests.

---

# Coding Exercises

Easy

- Add JWT authentication to an API.
- Configure CORS.
- Upload and validate files.

Medium

- Build RBAC with multiple roles.
- Integrate Celery with Redis.
- Implement API versioning.

Hard

- Build a real-time chat application using WebSockets.
- Design a secure authentication service with refresh tokens.
- Implement distributed rate limiting using Redis.

---

# Module Summary

Modern Python web applications require more than just routing and database access. Production systems depend on middleware, secure authentication, authorization, background processing, real-time communication, monitoring, and robust security practices. Mastering these concepts enables developers to build scalable, secure, and maintainable backend services using Flask, Django, or FastAPI.

---

