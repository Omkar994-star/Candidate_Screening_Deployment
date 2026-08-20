# Python Developer Knowledge Base
# Module 10 — Deployment and DevOps
# Part 1 — Deployment Fundamentals & Python Environments

---

# Module Overview

This module covers the complete deployment lifecycle for Python applications.

Topics include

- Deployment Fundamentals
- Virtual Environments
- Package Management
- Environment Variables
- Docker
- Docker Compose
- Linux Deployment
- Nginx
- Gunicorn
- Uvicorn
- CI/CD
- Cloud Deployment
- Kubernetes
- Monitoring
- Security
- High Availability
- Production Best Practices

---

# What is Deployment?

Deployment is the process of making an application available for users.

Typical workflow

```
Developer

↓

Build

↓

Test

↓

Package

↓

Deploy

↓

Production
```

---

# Development Lifecycle

```
Requirements

↓

Development

↓

Testing

↓

Staging

↓

Production
```

Each stage has a different purpose.

---

# Development Environment

Used for writing and testing code locally.

Characteristics

- Frequent changes
- Debugging enabled
- Local databases
- Developer tools installed

---

# Staging Environment

A production-like environment used before release.

Purpose

- Final testing
- Performance validation
- User acceptance testing
- Deployment verification

---

# Production Environment

The live application used by end users.

Requirements

- High availability
- Monitoring
- Security
- Reliability
- Backups
- Logging

---

# Deployment Goals

A good deployment should be

✓ Reliable

✓ Repeatable

✓ Automated

✓ Secure

✓ Easy to roll back

---

# Deployment Strategies

Common strategies

- Recreate
- Rolling Update
- Blue-Green Deployment
- Canary Deployment

---

# Recreate Deployment

```
Old Version

↓

Stop

↓

New Version

↓

Start
```

Advantages

- Simple

Disadvantages

- Downtime

---

# Rolling Deployment

```
Server A → Update

↓

Server B → Update

↓

Server C → Update
```

Advantages

- Minimal downtime
- Safer updates

---

# Blue-Green Deployment

```
Blue Environment (Current)

↓

Deploy Green

↓

Switch Traffic

↓

Remove Blue
```

Advantages

- Instant rollback
- Minimal downtime

---

# Canary Deployment

```
5% Users

↓

20%

↓

50%

↓

100%
```

New version is gradually released to users.

Advantages

- Lower deployment risk
- Easier monitoring

---

# Python Runtime

Applications require

- Python Interpreter
- Dependencies
- Configuration
- Environment Variables

Consistent environments reduce deployment issues.

---

# Why Virtual Environments?

Without virtual environments

```
Project A

↓

Shared Packages

↓

Project B
```

Package conflicts become likely.

---

# Virtual Environment

Each project gets an isolated Python environment.

```
Project

↓

Virtual Environment

↓

Independent Packages
```

---

# Creating a Virtual Environment

```bash
python -m venv venv
```

Project structure

```
project/

├── venv/

├── app.py

└── requirements.txt
```

---

# Activating Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

# Deactivating

```bash
deactivate
```

---

# Installing Packages

```bash
pip install fastapi
```

Package is installed only inside the active virtual environment.

---

# Viewing Installed Packages

```bash
pip list
```

---

# Freezing Dependencies

Generate

```bash
pip freeze > requirements.txt
```

Example

```
fastapi==0.116.0

uvicorn==0.35.0

requests==2.32.0
```

Version pinning helps ensure reproducible builds.

---

# Installing Dependencies

```bash
pip install -r requirements.txt
```

---

# requirements.txt

Purpose

- Dependency management
- Reproducible environments
- Easy installation
- CI/CD support

---

# pip

Python's default package manager.

Common commands

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

---

# Package Versioning

Examples

Exact version

```
fastapi==0.116.0
```

Minimum version

```
fastapi>=0.116.0
```

Compatible release

```
fastapi~=0.116
```

Choose version constraints appropriate for your release process.

---

# Dependency Conflicts

Example

```
Project A

requests==2.30

Project B

requests==2.32
```

Virtual environments isolate these requirements.

---

# Python Package Index (PyPI)

Most Python packages are published on the Python Package Index (PyPI).

```
Developer

↓

PyPI

↓

pip install
```

---

# Upgrading pip

```bash
python -m pip install --upgrade pip
```

Keeping tooling up to date helps with compatibility and security fixes.

---

# Environment Isolation

Every project should have

- Separate virtual environment
- Separate dependencies
- Separate configuration
- Independent lifecycle

---

# Common Directory Structure

```
project/

├── app/

├── tests/

├── venv/

├── requirements.txt

├── README.md

└── .gitignore
```

---

# .gitignore

Never commit

```
venv/

__pycache__/

*.pyc

.env
```

These files are environment-specific or generated automatically.

---

# Why Not Commit venv?

Reasons

- Large size
- Platform-specific binaries
- Easily recreated
- Causes merge conflicts

Commit dependency files instead.

---

# Dependency Management Best Practices

✓ Use a virtual environment per project.

✓ Pin dependency versions for production.

✓ Remove unused packages.

✓ Regularly update dependencies after testing.

✓ Review dependency security advisories.

---

# Common Mistakes

❌ Installing packages globally.

❌ Forgetting to activate the virtual environment.

❌ Committing the `venv` directory.

❌ Missing `requirements.txt`.

❌ Using untested dependency upgrades directly in production.

---

# Interview Questions

### Easy

1. What is deployment?
2. Why use virtual environments?
3. What is `requirements.txt`?
4. What does `pip freeze` do?
5. Why should `venv` not be committed to Git?

---

### Medium

1. Compare development, staging, and production environments.
2. Explain Blue-Green deployment.
3. What problems do virtual environments solve?
4. How do you reproduce a Python environment?
5. Explain dependency version pinning.

---

### Hard

1. Design a deployment workflow for a FastAPI application.
2. Compare deployment strategies for zero-downtime releases.
3. Design dependency management for a large enterprise project.
4. Explain how dependency conflicts occur and how to avoid them.
5. Build a production-ready deployment pipeline from development to production.

---

# Coding Exercises

Easy

- Create a virtual environment.
- Install packages using `pip`.
- Generate a `requirements.txt` file.

Medium

- Recreate a project environment from `requirements.txt`.
- Build a clean project structure with `.gitignore`.
- Experiment with version constraints.

Hard

- Automate environment setup using shell scripts.
- Create reproducible development and staging environments.
- Design a deployment checklist for a production API.

---

# Module Summary

Deployment is the process of delivering an application to users in a reliable, repeatable, and secure manner. Python applications rely on isolated virtual environments, dependency management with `pip`, and reproducible environments defined by `requirements.txt`. Understanding deployment environments, version management, and deployment strategies provides the foundation for building production-ready Python systems.

---

# Python Developer Knowledge Base
# Module 10 — Deployment and DevOps
# Part 2 — Package Management & Configuration

---

# Why Dependency Management Matters

Python applications depend on external libraries.

Without proper dependency management

- Version conflicts occur
- Builds become non-reproducible
- Deployments fail
- Security vulnerabilities increase

Goals

✓ Reproducible builds

✓ Consistent environments

✓ Easy upgrades

✓ Dependency isolation

---

# Python Packaging Evolution

```
setup.py

↓

requirements.txt

↓

pyproject.toml
```

Modern Python packaging centers around `pyproject.toml`.

---

# pip

Default Python package manager.

Install package

```bash
pip install requests
```

Upgrade package

```bash
pip install --upgrade requests
```

Remove package

```bash
pip uninstall requests
```

Show installed packages

```bash
pip list
```

---

# requirements.txt

Lists project dependencies.

Example

```text
fastapi==0.116.0
uvicorn==0.35.0
requests==2.32.0
```

Install

```bash
pip install -r requirements.txt
```

---

# Limitations of requirements.txt

- No dependency grouping
- Manual updates
- Weak project metadata
- Dependency resolution can be difficult

Modern tools address these limitations.

---

# pip-tools

Adds dependency compilation.

Install

```bash
pip install pip-tools
```

Input file

```
requirements.in
```

Compile

```bash
pip-compile
```

Output

```
requirements.txt
```

Benefits

- Locked dependency versions
- Deterministic builds
- Easier upgrades

---

# Poetry

A modern dependency and project management tool.

Install

```bash
pip install poetry
```

Create project

```bash
poetry new my_project
```

Install dependencies

```bash
poetry install
```

Add dependency

```bash
poetry add fastapi
```

---

# Poetry Project Structure

```
project/

├── pyproject.toml

├── poetry.lock

├── app/

└── tests/
```

---

# poetry.lock

Contains exact dependency versions.

Purpose

- Reproducible builds
- Consistent deployments
- Stable dependency resolution

Commit this file to version control.

---

# uv

`uv` is a modern, high-performance Python package and environment manager.

Advantages

- Very fast dependency resolution
- Fast virtual environment creation
- Compatible with existing Python packaging standards
- Suitable for CI/CD

Install (example)

```bash
pip install uv
```

Create virtual environment

```bash
uv venv
```

Install dependencies

```bash
uv pip install -r requirements.txt
```

---

# pyproject.toml

Modern Python project configuration file.

Example

```toml
[project]
name = "my_app"
version = "1.0.0"
description = "Sample application"
requires-python = ">=3.12"

dependencies = [
    "fastapi",
    "uvicorn"
]
```

Can contain

- Project metadata
- Dependencies
- Build configuration
- Tool configuration

---

# Tool Configuration

Many tools store configuration in `pyproject.toml`.

Example

```
Black

Ruff

isort

MyPy

Pytest
```

Single configuration file for multiple tools.

---

# Environment Variables

Applications should not hardcode configuration.

Instead

```
Application

↓

Environment Variables

↓

Configuration
```

Examples

- Database URL
- API keys
- Secret keys
- Debug mode

---

# Reading Environment Variables

```python
import os

host = os.getenv("HOST")
```

With a default

```python
port = os.getenv("PORT", "8000")
```

---

# Setting Environment Variables

Linux/macOS

```bash
export API_KEY=secret
```

Windows (Command Prompt)

```cmd
set API_KEY=secret
```

PowerShell

```powershell
$env:API_KEY="secret"
```

---

# Why Environment Variables?

Avoid hardcoding

```python
API_KEY = "123456"
```

Prefer

```python
API_KEY = os.getenv("API_KEY")
```

Benefits

- Better security
- Environment-specific configuration
- Easier deployment

---

# .env File

Store development environment variables.

Example

```text
DEBUG=True
HOST=localhost
PORT=8000
DATABASE_URL=postgresql://user:password@localhost/db
SECRET_KEY=my-secret
```

---

# python-dotenv

Loads variables from a `.env` file.

Install

```bash
pip install python-dotenv
```

Example

```python
from dotenv import load_dotenv

load_dotenv()
```

Then

```python
import os

secret = os.getenv("SECRET_KEY")
```

---

# .env Example

```
.env

↓

load_dotenv()

↓

os.getenv()
```

Simple workflow for local development.

---

# Configuration by Environment

Development

```
DEBUG=True
```

Testing

```
DEBUG=False
```

Production

```
DEBUG=False
```

Different environments typically use different databases, credentials, and logging settings.

---

# Configuration Separation

```
Development

↓

Testing

↓

Staging

↓

Production
```

Each environment should have independent configuration.

---

# Secrets Management

Never store

- API Keys
- Passwords
- OAuth Tokens
- Database Passwords
- Private Keys

Inside source code.

---

# Secret Storage Options

Examples

- Environment variables
- Cloud secret managers
- Kubernetes Secrets
- Encrypted configuration systems

---

# Configuration Object

Example

```python
class Config:

    DEBUG = False

    HOST = "localhost"
```

Better

```python
class Config:

    DEBUG = os.getenv("DEBUG")
```

---

# Pydantic Settings

Common in FastAPI applications.

Example

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    database_url: str

    secret_key: str

settings = Settings()
```

Benefits

- Type validation
- Default values
- Environment loading
- Cleaner configuration management

---

# Configuration Validation

Validate required settings during startup.

Example

```
Application

↓

Read Configuration

↓

Validate

↓

Start
```

Fail fast if mandatory configuration is missing.

---

# Configuration Best Practices

✓ Store secrets outside source code.

✓ Use environment variables.

✓ Validate configuration at startup.

✓ Separate configuration by environment.

✓ Commit example configuration files (e.g., `.env.example`).

✓ Document required environment variables.

---

# Common Mistakes

❌ Hardcoding API keys.

❌ Committing `.env` files.

❌ Sharing production credentials.

❌ Using development configuration in production.

❌ Ignoring missing environment variables.

---

# .gitignore

Never commit

```
.env

.env.local

.env.production

*.pem
```

Sensitive files should remain outside version control.

---

# Interview Questions

### Easy

1. What is `pyproject.toml`?
2. What is Poetry?
3. What is a `.env` file?
4. Why use environment variables?
5. Why should `.env` not be committed?

---

### Medium

1. Compare `requirements.txt` and Poetry.
2. Explain dependency locking.
3. Compare `pip` and `uv`.
4. Why validate configuration during startup?
5. Explain secret management strategies.

---

### Hard

1. Design configuration management for a microservices application.
2. Compare environment variables and cloud secret managers.
3. Explain reproducible dependency management for enterprise projects.
4. Design a secure configuration strategy for a FastAPI application.
5. Build a deployment process using `pyproject.toml` and locked dependencies.

---

# Coding Exercises

Easy

- Create a `.env` file.
- Read environment variables using `os.getenv()`.
- Load configuration with `python-dotenv`.

Medium

- Configure a project using `pyproject.toml`.
- Build a configuration class with Pydantic Settings.
- Generate a lock file using Poetry.

Hard

- Design a multi-environment configuration system.
- Build a secure secrets management workflow.
- Create a production-ready dependency management strategy.

---

# Module Summary

Modern Python projects rely on robust dependency and configuration management. Tools such as `pip`, `pip-tools`, Poetry, and `uv` help create reproducible environments, while `pyproject.toml` centralizes project configuration. Environment variables and secret management keep sensitive data out of source code, and validated configuration ensures applications start reliably across development, testing, staging, and production environments.

---

# Python Developer Knowledge Base
# Module 10 — Deployment and DevOps
# Part 3 — Docker & Containerization

---

# What is Docker?

Docker is a containerization platform that packages an application and all its dependencies into a portable container.

Container includes

- Application code
- Python runtime
- Libraries
- System dependencies
- Configuration

Goal

```
Build Once

↓

Run Anywhere
```

---

# Why Docker?

Without Docker

```
Developer Machine

↓

Works

↓

Production Server

↓

Fails
```

With Docker

```
Developer

↓

Docker Image

↓

Production

↓

Same Environment
```

Benefits

✓ Consistent environments

✓ Easy deployment

✓ Fast startup

✓ Isolation

✓ Portability

✓ Scalability

---

# Virtual Machine vs Container

Virtual Machine

```
Hardware

↓

Host OS

↓

Hypervisor

↓

Guest OS

↓

Application
```

Container

```
Hardware

↓

Host OS

↓

Docker Engine

↓

Container

↓

Application
```

Containers share the host operating system kernel, making them lightweight and fast.

---

# Docker Architecture

```
Docker Client

↓

Docker Daemon

↓

Images

↓

Containers
```

Components

- Docker Client
- Docker Engine (Daemon)
- Images
- Containers
- Registry

---

# Docker Image

An image is a read-only template used to create containers.

Contains

- Application
- Runtime
- Libraries
- Dependencies
- Configuration

Images are immutable once built.

---

# Docker Container

A running instance of an image.

Example

```
Docker Image

↓

docker run

↓

Running Container
```

Multiple containers can be created from the same image.

---

# Docker Registry

Stores Docker images.

Common registries

- Docker Hub
- GitHub Container Registry
- Amazon ECR
- Azure Container Registry
- Google Artifact Registry

---

# Installing Docker

Verify installation

```bash
docker --version
```

Verify daemon

```bash
docker info
```

---

# Basic Docker Commands

List images

```bash
docker images
```

List running containers

```bash
docker ps
```

List all containers

```bash
docker ps -a
```

Remove container

```bash
docker rm container_id
```

Remove image

```bash
docker rmi image_id
```

---

# Pulling an Image

Example

```bash
docker pull python:3.12
```

Downloads the image from a registry.

---

# Running a Container

Interactive shell

```bash
docker run -it python:3.12
```

Run a command

```bash
docker run python:3.12 python --version
```

---

# Dockerfile

A Dockerfile defines how to build an image.

Example

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

---

# Dockerfile Instructions

| Instruction | Purpose |
|------------|---------|
| FROM | Base image |
| WORKDIR | Working directory |
| COPY | Copy files |
| ADD | Copy files (with extra features) |
| RUN | Execute command during build |
| ENV | Set environment variable |
| EXPOSE | Document listening port |
| CMD | Default command |
| ENTRYPOINT | Main executable |

---

# Building an Image

```bash
docker build -t myapp .
```

Options

- `-t` assigns a tag
- `.` specifies the build context

---

# Running an Image

```bash
docker run myapp
```

Run in background

```bash
docker run -d myapp
```

---

# Port Mapping

Expose application ports.

Example

```bash
docker run -p 8000:8000 myapp
```

Format

```
Host Port : Container Port
```

---

# Naming Containers

```bash
docker run --name api myapp
```

Instead of using an automatically generated name.

---

# Viewing Logs

```bash
docker logs api
```

Follow logs

```bash
docker logs -f api
```

---

# Executing Commands

Open a shell

```bash
docker exec -it api bash
```

For Alpine-based images

```bash
docker exec -it api sh
```

---

# Stopping Containers

```bash
docker stop api
```

Restart

```bash
docker restart api
```

Remove

```bash
docker rm api
```

---

# Environment Variables

Pass configuration

```bash
docker run

-e DATABASE_URL=db

myapp
```

Multiple variables

```bash
docker run \
-e HOST=0.0.0.0 \
-e PORT=8000 \
myapp
```

---

# Volumes

Persist data outside containers.

```
Container

↓

Volume

↓

Host Storage
```

Example

```bash
docker run

-v data:/app/data

myapp
```

Benefits

- Persistent storage
- Shared data
- Backup support

---

# Bind Mounts

Mount local directories.

```bash
docker run

-v $(pwd):/app

myapp
```

Useful during development for live code changes.

---

# Docker Networks

Allow containers to communicate.

```
API Container

↓

Docker Network

↓

Database Container
```

Create network

```bash
docker network create app-network
```

---

# Docker Compose

Manages multi-container applications.

Example

```
API

↓

Database

↓

Redis
```

All started with one command.

---

# docker-compose.yml

Example

```yaml
services:

  api:

    build: .

    ports:

      - "8000:8000"

  postgres:

    image: postgres:17

  redis:

    image: redis:8
```

---

# Docker Compose Commands

Start

```bash
docker compose up
```

Detached mode

```bash
docker compose up -d
```

Stop

```bash
docker compose down
```

Rebuild

```bash
docker compose up --build
```

---

# Multi-Stage Builds

Reduce image size.

Example

```
Builder Stage

↓

Compiled Application

↓

Runtime Stage
```

Only the necessary runtime artifacts are copied into the final image.

---

# Example Multi-Stage Dockerfile

```dockerfile
FROM python:3.12 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --prefix=/install -r requirements.txt

FROM python:3.12-slim

COPY --from=builder /install /usr/local

WORKDIR /app

COPY . .

CMD ["python", "app.py"]
```

---

# .dockerignore

Exclude unnecessary files.

Example

```
venv/

__pycache__/

.git/

.pytest_cache/

.env
```

Reduces build context size.

---

# Image Tagging

Example

```bash
docker build -t myapp:1.0 .
```

Latest

```bash
docker build -t myapp:latest .
```

Use versioned tags in production instead of relying only on `latest`.

---

# Inspecting Containers

```bash
docker inspect api
```

Provides

- Network details
- Mounts
- Environment variables
- Configuration

---

# Resource Limits

Limit CPU

```bash
docker run --cpus=2 myapp
```

Limit memory

```bash
docker run --memory=512m myapp
```

Helps prevent one container from consuming excessive resources.

---

# Container Lifecycle

```
Image

↓

Create

↓

Run

↓

Stop

↓

Remove
```

---

# Best Practices

✓ Use small base images (`python:slim` when appropriate).

✓ Pin base image versions.

✓ Use `.dockerignore`.

✓ Run one main process per container.

✓ Keep images immutable.

✓ Store configuration in environment variables.

✓ Use multi-stage builds.

✓ Do not run as the root user in production.

---

# Common Mistakes

❌ Using `latest` everywhere.

❌ Committing secrets into images.

❌ Installing unnecessary packages.

❌ Creating very large images.

❌ Storing persistent data inside containers.

❌ Running production containers with debug settings.

---

# Interview Questions

### Easy

1. What is Docker?
2. What is a container?
3. What is an image?
4. Difference between an image and a container.
5. What is a Dockerfile?

---

### Medium

1. Explain Docker architecture.
2. What are Docker volumes?
3. Compare bind mounts and volumes.
4. What is Docker Compose?
5. Why use multi-stage builds?

---

### Hard

1. Design a Docker deployment for a FastAPI application with PostgreSQL and Redis.
2. Explain how to optimize Docker image size.
3. Compare containers and virtual machines.
4. Design networking for multiple containers.
5. Build a production-ready Docker strategy for a Python backend.

---

# Coding Exercises

Easy

- Build a Docker image for a Python script.
- Run a container with port mapping.
- Pass environment variables to a container.

Medium

- Create a `docker-compose.yml` for an API and database.
- Mount a local directory using a bind mount.
- Persist database data using Docker volumes.

Hard

- Create a multi-stage Docker build for a FastAPI application.
- Optimize image size and build performance.
- Deploy a multi-container Python application using Docker Compose.

---

# Module Summary

Docker packages Python applications and their dependencies into portable, isolated containers that run consistently across environments. Images define application templates, while containers are their running instances. Dockerfiles, volumes, networks, and Docker Compose enable reproducible deployments, and multi-stage builds help create smaller, production-ready images. Following Docker best practices results in secure, efficient, and maintainable deployments.

---

# Python Developer Knowledge Base
# Module 10 — Deployment and DevOps
# Part 4 — Linux, Process Management & Python Application Servers

---

# Why Linux?

Most production Python applications run on Linux servers.

Reasons

- Stable
- Secure
- Open Source
- High Performance
- Excellent Networking
- Cloud Standard

Common Linux Distributions

- Ubuntu
- Debian
- Rocky Linux
- AlmaLinux
- Red Hat Enterprise Linux
- Amazon Linux

---

# Linux File System

```
/

├── bin/

├── etc/

├── home/

├── opt/

├── usr/

├── var/

└── tmp/
```

Important directories

```
/etc

Configuration files

/var/log

Application logs

/home

User files

/opt

Third-party software

/tmp

Temporary files
```

---

# Useful Linux Commands

Current directory

```bash
pwd
```

List files

```bash
ls
```

Detailed list

```bash
ls -la
```

Change directory

```bash
cd
```

Create directory

```bash
mkdir app
```

Copy

```bash
cp
```

Move

```bash
mv
```

Delete

```bash
rm
```

Find files

```bash
find .
```

---

# Viewing Files

```bash
cat file.txt
```

Large files

```bash
less app.log
```

View last lines

```bash
tail app.log
```

Follow log

```bash
tail -f app.log
```

---

# Searching

```bash
grep ERROR app.log
```

Recursive search

```bash
grep -R "FastAPI" .
```

---

# File Permissions

```
r

Read

w

Write

x

Execute
```

Example

```
-rwxr-xr--
```

Represents permissions for

- Owner
- Group
- Others

---

# Changing Permissions

```bash
chmod 755 app.py
```

Owner

```
Read

Write

Execute
```

Others

```
Read

Execute
```

---

# Changing Owner

```bash
chown user:user app.py
```

---

# Environment Variables

Display

```bash
env
```

Export

```bash
export PORT=8000
```

---

# Process Management

View processes

```bash
ps aux
```

Interactive process viewer

```bash
top
```

Modern alternative

```bash
htop
```

---

# Killing Processes

Terminate

```bash
kill PID
```

Force terminate

```bash
kill -9 PID
```

Use `kill -9` only when graceful termination fails.

---

# Background Processes

Run in background

```bash
python app.py &
```

Bring to foreground

```bash
fg
```

---

# systemd

Most modern Linux systems use `systemd`.

Purpose

- Start services
- Stop services
- Restart services
- Auto-start on boot
- Monitor services

---

# Service File

Example

```
/etc/systemd/system/myapp.service
```

---

# Example Service

```ini
[Unit]

Description=FastAPI Application

After=network.target

[Service]

User=ubuntu

WorkingDirectory=/home/ubuntu/app

ExecStart=/home/ubuntu/venv/bin/uvicorn app:app --host 0.0.0.0 --port 8000

Restart=always

[Install]

WantedBy=multi-user.target
```

---

# systemctl Commands

Reload configuration

```bash
sudo systemctl daemon-reload
```

Start service

```bash
sudo systemctl start myapp
```

Stop

```bash
sudo systemctl stop myapp
```

Restart

```bash
sudo systemctl restart myapp
```

Enable on boot

```bash
sudo systemctl enable myapp
```

Status

```bash
sudo systemctl status myapp
```

---

# Journal Logs

View service logs

```bash
journalctl -u myapp
```

Follow logs

```bash
journalctl -u myapp -f
```

---

# Python Development Server

Example

```bash
uvicorn app:app
```

Development only.

Reasons

- Single worker
- Limited robustness
- Debug-oriented

---

# Production Application Servers

Common servers

- Gunicorn
- Uvicorn
- Daphne
- Hypercorn

---

# Gunicorn

Production WSGI server.

Suitable for

- Flask
- Django
- Other WSGI applications

Install

```bash
pip install gunicorn
```

Run

```bash
gunicorn app:app
```

---

# Workers

Gunicorn starts multiple worker processes.

Example

```bash
gunicorn

-w 4

app:app
```

General starting point

```
workers = (2 × CPU cores) + 1
```

Adjust based on workload and benchmarking.

---

# Uvicorn

ASGI server.

Supports

- FastAPI
- Starlette
- Quart
- Async applications

Run

```bash
uvicorn app:app
```

---

# Production Uvicorn

```bash
uvicorn

app:app

--host 0.0.0.0

--port 8000
```

---

# Gunicorn + Uvicorn

Recommended for FastAPI production.

```bash
gunicorn

-k uvicorn.workers.UvicornWorker

-w 4

app:app
```

Gunicorn manages workers while Uvicorn handles ASGI requests.

---

# WSGI vs ASGI

| WSGI | ASGI |
|------|------|
| Synchronous | Asynchronous |
| Flask | FastAPI |
| Django (traditional) | FastAPI, Starlette |
| Gunicorn | Uvicorn / Hypercorn |

Recent versions of Django also support ASGI for asynchronous capabilities.

---

# Nginx

Nginx is a

- Reverse Proxy
- Web Server
- Load Balancer
- Static File Server

Architecture

```
Internet

↓

Nginx

↓

Gunicorn

↓

Python App
```

---

# Why Use Nginx?

Benefits

✓ SSL termination

✓ Static file serving

✓ Load balancing

✓ Compression

✓ Reverse proxy

✓ Security

---

# Reverse Proxy

Instead of users connecting directly

```
User

↓

Python App
```

Use

```
User

↓

Nginx

↓

Python App
```

---

# Nginx Configuration

Example

```nginx
server {

    listen 80;

    location / {

        proxy_pass http://127.0.0.1:8000;

    }
}
```

---

# HTTPS

HTTP

```
Plain Text
```

HTTPS

```
Encrypted
```

Use HTTPS in production to protect data in transit.

---

# SSL Certificate

Common providers

- Let's Encrypt
- Commercial Certificate Authorities

---

# Port Architecture

```
Internet

↓

443

↓

Nginx

↓

8000

↓

FastAPI
```

Users connect to Nginx, not directly to the application server.

---

# Static Files

Nginx efficiently serves

- Images
- CSS
- JavaScript
- Fonts
- Downloads

Avoid serving these directly from the Python application when possible.

---

# Load Balancing

```
Nginx

↓

App 1

↓

App 2

↓

App 3
```

Distributes requests across multiple application instances.

---

# Health Checks

Monitor

- CPU
- Memory
- Response Time
- Status Code
- Worker Health

Detect problems early.

---

# Deployment Flow

```
Client

↓

Nginx

↓

Gunicorn

↓

Application

↓

Database
```

---

# Best Practices

✓ Use Linux for production.

✓ Manage applications with `systemd`.

✓ Place Nginx in front of application servers.

✓ Use HTTPS.

✓ Run multiple workers.

✓ Monitor logs.

✓ Configure automatic service restart.

✓ Keep operating system updated.

---

# Common Mistakes

❌ Running development servers in production.

❌ Running applications as root.

❌ Exposing application ports directly to the internet.

❌ Ignoring service logs.

❌ Using a single worker for high-traffic applications.

❌ Not enabling automatic service restart.

---

# Interview Questions

### Easy

1. Why is Linux preferred for production?
2. What is `systemd`?
3. What is Gunicorn?
4. What is Uvicorn?
5. What is Nginx?

---

### Medium

1. Explain WSGI vs ASGI.
2. Why use a reverse proxy?
3. How does `systemctl` manage services?
4. Explain Gunicorn workers.
5. Why should HTTPS be used?

---

### Hard

1. Design a production deployment architecture for a FastAPI application.
2. Compare Gunicorn and Uvicorn.
3. Explain how Nginx performs load balancing.
4. Build a high-availability Linux deployment strategy.
5. Design a scalable backend deployment with multiple application servers.

---

# Coding Exercises

Easy

- Create a `systemd` service for a Python application.
- Run Gunicorn with multiple workers.
- Configure a simple Nginx reverse proxy.

Medium

- Deploy a FastAPI application behind Nginx.
- Enable HTTPS using Let's Encrypt.
- Configure automatic service startup.

Hard

- Design a multi-server deployment with load balancing.
- Tune Gunicorn worker settings for different workloads.
- Deploy a highly available Python backend on Linux.

---

# Module Summary

Linux is the standard operating system for production Python deployments. `systemd` manages application services, while Gunicorn and Uvicorn provide robust application servers for WSGI and ASGI applications. Nginx acts as a reverse proxy, handling HTTPS, static files, and load balancing before forwarding requests to the Python application. Together, these components create a secure, scalable, and production-ready deployment architecture.

---

# Python Developer Knowledge Base
# Module 10 — Deployment and DevOps
# Part 5 (Final) — Cloud Deployment, Kubernetes & Production Operations

---

# Cloud Computing

Cloud computing provides on-demand computing resources over the internet.

Resources include

- Virtual Machines
- Storage
- Databases
- Networking
- Containers
- Serverless Functions

Benefits

✓ Scalability

✓ High Availability

✓ Pay-as-you-go

✓ Managed Services

✓ Global Infrastructure

---

# Major Cloud Providers

Popular platforms

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud Platform (GCP)

Each provides similar core services with different naming conventions.

---

# Common Cloud Services

| Service | Purpose |
|---------|---------|
| Compute | Run applications |
| Storage | Store files and objects |
| Database | Managed SQL/NoSQL databases |
| Networking | Virtual networks, firewalls |
| Monitoring | Metrics and alerts |
| IAM | Identity and access management |

---

# Virtual Machines

```
Cloud Provider

↓

Virtual Machine

↓

Linux

↓

Python Application
```

Examples

- AWS EC2
- Azure Virtual Machines
- Google Compute Engine

---

# Containers in the Cloud

```
Docker Image

↓

Container Platform

↓

Running Containers
```

Examples

- AWS ECS
- Azure Container Apps
- Google Cloud Run
- Kubernetes

---

# Serverless

Run code without managing servers.

Examples

- AWS Lambda
- Azure Functions
- Google Cloud Functions

Best suited for

- Event-driven workloads
- Background jobs
- Lightweight APIs

---

# Infrastructure as Code (IaC)

Infrastructure is defined using code instead of manual configuration.

Popular tools

- Terraform
- AWS CloudFormation
- Pulumi
- Bicep

Benefits

- Repeatability
- Version control
- Automation

---

# CI/CD Overview

Continuous Integration (CI)

- Build
- Test
- Validate

Continuous Deployment/Delivery (CD)

- Package
- Deploy
- Release

Pipeline

```
Developer

↓

Git Push

↓

CI

↓

Tests

↓

Build Image

↓

Deploy

↓

Production
```

---

# GitHub Actions Example

```yaml
name: Deploy

on:
  push:
    branches:
      - main

jobs:
  build:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5

      - run: pip install -r requirements.txt

      - run: pytest

      - run: docker build -t myapp .
```

---

# Container Registry

Docker images are stored in registries.

Examples

- Docker Hub
- GitHub Container Registry
- Amazon ECR
- Azure Container Registry
- Google Artifact Registry

Workflow

```
Build Image

↓

Push Registry

↓

Deploy
```

---

# Kubernetes

Kubernetes (K8s) is a container orchestration platform.

Responsibilities

- Scheduling
- Scaling
- Self-healing
- Service discovery
- Rolling updates

---

# Kubernetes Architecture

```
Control Plane

↓

Worker Nodes

↓

Pods

↓

Containers
```

---

# Pod

Smallest deployable Kubernetes unit.

```
Pod

↓

One or More Containers
```

Typically, one application container runs per pod.

---

# Deployment

Defines the desired application state.

Responsibilities

- Replica management
- Updates
- Rollbacks

Example

```
Deployment

↓

3 Replicas

↓

3 Running Pods
```

---

# ReplicaSet

Ensures the desired number of pods are running.

If a pod fails

```
ReplicaSet

↓

Creates New Pod
```

---

# Service

Provides stable networking for pods.

Types

- ClusterIP
- NodePort
- LoadBalancer

Architecture

```
Service

↓

Pods
```

---

# Ingress

Routes external HTTP/HTTPS traffic into the cluster.

```
Internet

↓

Ingress

↓

Service

↓

Pods
```

---

# ConfigMap

Stores non-sensitive configuration.

Examples

- Hostnames
- Feature flags
- Configuration values

---

# Secret

Stores sensitive data.

Examples

- API Keys
- Database Passwords
- Tokens
- Certificates

Avoid storing secrets directly in manifests.

---

# Horizontal Scaling

Increase capacity by adding more replicas.

```
2 Pods

↓

4 Pods

↓

8 Pods
```

Suitable for stateless applications.

---

# Vertical Scaling

Increase resources for a single instance.

```
2 CPU

↓

4 CPU
```

Limited by machine capacity.

---

# Rolling Updates

Replace pods gradually.

```
Old Pod

↓

New Pod

↓

Old Pod Removed
```

Benefits

- No downtime
- Safer deployments
- Easy rollback

---

# Rollback

Restore a previous application version if deployment fails.

```
Version 2

↓

Issue Found

↓

Rollback

↓

Version 1
```

---

# Health Checks

Liveness Probe

Checks if the application is still running.

Readiness Probe

Checks if the application is ready to receive traffic.

Startup Probe

Allows slower applications additional startup time.

---

# Monitoring

Monitor

- CPU
- Memory
- Disk
- Network
- Error Rate
- Response Time
- Throughput
- Queue Length

---

# Prometheus

Collects application and infrastructure metrics.

Example metrics

- Requests per second
- Latency
- CPU utilization

---

# Grafana

Visualizes metrics from Prometheus and other sources.

Common dashboards

- Application performance
- Resource usage
- Database metrics

---

# Logging

Centralized logging improves troubleshooting.

Common solutions

- ELK Stack (Elasticsearch, Logstash, Kibana)
- OpenSearch
- Loki

Workflow

```
Application

↓

Logs

↓

Centralized Storage

↓

Dashboard
```

---

# Distributed Tracing

Tracks requests across multiple services.

Popular tools

- OpenTelemetry
- Jaeger
- Zipkin

Useful for debugging microservices.

---

# Scalability

Scale

- Application servers
- Databases
- Caches
- Queues

Avoid relying on a single server.

---

# High Availability

Goal

No single point of failure.

Example

```
Load Balancer

↓

App 1

↓

App 2

↓

Database Replica
```

---

# Backup Strategy

Regularly back up

- Databases
- Object storage
- Configuration
- Secrets

Test restoration procedures periodically.

---

# Disaster Recovery

Plan for

- Server failures
- Data corruption
- Region outages
- Security incidents

Document recovery procedures.

---

# Security Best Practices

✓ Use HTTPS.

✓ Rotate secrets regularly.

✓ Apply least-privilege access.

✓ Keep dependencies updated.

✓ Scan container images.

✓ Enable logging and monitoring.

✓ Encrypt sensitive data.

✓ Use firewalls and network policies.

---

# Production Deployment Checklist

Before deployment

✓ Tests pass

✓ Lint passes

✓ Security scan completed

✓ Configuration validated

✓ Secrets configured

✓ Monitoring enabled

✓ Backups verified

✓ Rollback plan documented

✓ Health checks configured

✓ Documentation updated

---

# DevOps Best Practices

✓ Automate deployments.

✓ Use Infrastructure as Code.

✓ Monitor continuously.

✓ Implement CI/CD.

✓ Keep environments consistent.

✓ Practice regular disaster recovery drills.

✓ Review logs and metrics proactively.

---

# Common Mistakes

❌ Deploying without automated tests.

❌ Hardcoding secrets.

❌ Ignoring monitoring.

❌ Manual production changes.

❌ No rollback strategy.

❌ Running everything on a single server.

❌ Not testing backups.

---

# Complete Production Architecture

```
Users

↓

Load Balancer

↓

Nginx / Ingress

↓

Application Pods

↓

Redis Cache

↓

PostgreSQL

↓

Object Storage

↓

Monitoring & Logging
```

---

# Interview Questions

### Easy

1. What is Kubernetes?
2. What is a Pod?
3. What is CI/CD?
4. What is a Load Balancer?
5. What is a ConfigMap?

---

### Medium

1. Compare virtual machines and containers.
2. Explain Kubernetes Deployments.
3. What is the difference between a ConfigMap and a Secret?
4. Why are readiness probes important?
5. Explain rolling updates.

---

### Hard

1. Design a production deployment architecture for a FastAPI application on Kubernetes.
2. Explain horizontal and vertical scaling trade-offs.
3. Build a CI/CD pipeline for containerized Python applications.
4. Design monitoring and logging for a microservices platform.
5. Create a disaster recovery strategy for a cloud-native backend.

---

# Coding Exercises

Easy

- Write a basic Kubernetes Deployment manifest.
- Configure a Service for a Python application.
- Create a ConfigMap for application settings.

Medium

- Deploy a FastAPI application to Kubernetes.
- Configure rolling updates.
- Add readiness and liveness probes.

Hard

- Design a highly available Kubernetes architecture.
- Build a complete CI/CD pipeline deploying Docker images to Kubernetes.
- Integrate Prometheus, Grafana, and centralized logging into a production environment.

---

# Module Summary

Modern Python deployments rely on cloud infrastructure, container orchestration, and automation. CI/CD pipelines ensure code is tested and deployed consistently, while Kubernetes provides scalable, self-healing container management. Monitoring, logging, health checks, backups, and disaster recovery complete a production-ready deployment strategy. Together, these practices enable secure, resilient, and highly available Python applications.

---

