# Python Developer Knowledge Base
# Module 08 — Concurrency and Performance
# Part 1 — Concurrency Fundamentals

---

# Module Overview

Modern applications must handle multiple tasks efficiently.

Examples

- Thousands of API requests
- Database operations
- File processing
- Network communication
- Background jobs
- Data processing
- Real-time systems

This module covers

- Concurrency
- Parallelism
- Processes
- Threads
- GIL
- AsyncIO
- Event Loop
- Coroutines
- Executors
- Synchronization
- Performance Optimization
- Profiling
- Memory Optimization

---

# Why Concurrency?

Imagine an API server receiving 10,000 requests.

Without concurrency

```
Request 1

↓

Request 2

↓

Request 3

↓

...
```

Each request waits for the previous one.

Response times become extremely high.

---

With concurrency

```
Request 1

Request 2

Request 3

Request 4

↓

All progress independently
```

The CPU remains productive while waiting for slow operations.

---

# What is Concurrency?

Concurrency means multiple tasks make progress during overlapping time periods.

Important

Tasks do **not necessarily execute simultaneously**.

Example

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

The operating system or runtime switches between tasks.

---

# What is Parallelism?

Parallelism means multiple tasks execute at the same time.

Example

```
CPU Core 1

↓

Task A

------------------

CPU Core 2

↓

Task B
```

Requires multiple CPU cores.

---

# Concurrency vs Parallelism

Concurrency

```
One cashier

Serving multiple customers

One at a time
```

Parallelism

```
Four cashiers

Serving four customers

Simultaneously
```

---

# Key Differences

| Concurrency | Parallelism |
|-------------|-------------|
| Multiple tasks make progress | Multiple tasks execute simultaneously |
| Can use one CPU core | Requires multiple CPU cores |
| Good for I/O | Good for CPU-intensive work |
| Context switching | True simultaneous execution |

---

# CPU-bound Tasks

CPU-bound programs spend most of their time performing computations.

Examples

- Image processing
- Video encoding
- Scientific simulations
- Matrix multiplication
- Encryption
- Machine learning training

Performance depends primarily on CPU speed.

---

# I/O-bound Tasks

I/O-bound programs spend most of their time waiting.

Examples

- Database queries
- Reading files
- Writing files
- Network requests
- REST APIs
- Downloading data

During waiting periods, the CPU is mostly idle.

---

# CPU-bound Example

```
Calculate

↓

Calculate

↓

Calculate
```

No waiting.

CPU utilization is high.

---

# I/O-bound Example

```
Send Request

↓

Wait

↓

Receive Response

↓

Process Data
```

Most time is spent waiting.

---

# Which Model Should You Use?

| Workload | Best Choice |
|-----------|-------------|
| CPU-intensive | Multiprocessing |
| File operations | AsyncIO / Threads |
| Network requests | AsyncIO |
| Web APIs | AsyncIO |
| Machine learning inference | Depends on workload |
| Scientific computing | Multiprocessing |

---

# Blocking Operations

Blocking code prevents other work from progressing.

Example

```
Read File

↓

Wait

↓

Continue
```

Nothing else happens while waiting.

---

# Non-Blocking Operations

Non-blocking code allows other tasks to execute while waiting.

Example

```
Task A waiting

↓

Task B executes

↓

Task C executes

↓

Task A resumes
```

This improves resource utilization.

---

# Synchronous Programming

Execution occurs sequentially.

```
Task 1

↓

Task 2

↓

Task 3
```

Simple to understand but may waste time during I/O waits.

---

# Asynchronous Programming

Execution pauses only when waiting.

```
Task A

↓

Waiting

↓

Task B

↓

Waiting

↓

Task C

↓

Resume Task A
```

Ideal for high-concurrency I/O workloads.

---

# Throughput

Throughput measures how much work is completed over time.

Example

```
500 requests/second
```

Higher throughput generally indicates better scalability.

---

# Latency

Latency is the time taken to complete one request.

Example

```
150 milliseconds
```

Lower latency improves user experience.

---

# Throughput vs Latency

| Throughput | Latency |
|------------|----------|
| Work completed | Time per request |
| Higher is better | Lower is better |

A system may have high throughput but still experience high latency under heavy load.

---

# Scalability

Scalability is the ability of a system to handle increasing workload.

Two common approaches

Vertical Scaling

```
Faster CPU

More RAM
```

Horizontal Scaling

```
Server A

Server B

Server C
```

Horizontal scaling is generally preferred for distributed systems.

---

# Resource Contention

Multiple tasks competing for the same resource.

Examples

- CPU
- Memory
- Disk
- Database
- Network

Poor resource management reduces performance.

---

# Context Switching

The operating system switches execution between tasks.

```
Task A

↓

Task B

↓

Task C

↓

Task A
```

Advantages

- Better responsiveness
- Improved resource utilization

Disadvantages

- Switching has overhead
- Too many switches reduce performance

---

# Work Queue

Tasks are often placed into queues.

```
Queue

↓

Worker

↓

Result
```

Examples

- Celery
- RabbitMQ
- Redis Queue

---

# Real-World Examples

### API Server

Thousands of users send requests simultaneously.

Best choice

```
AsyncIO
```

---

### Video Encoding

Millions of calculations.

Best choice

```
Multiprocessing
```

---

### File Downloader

Downloading hundreds of files.

Best choice

```
AsyncIO
```

---

### Machine Learning Training

Heavy numerical computation.

Best choice

```
Multiprocessing

GPU
```

---

# Choosing the Right Concurrency Model

| Problem | Recommended Solution |
|----------|----------------------|
| REST API | AsyncIO |
| Database queries | AsyncIO |
| File uploads | AsyncIO |
| CPU-intensive calculations | Multiprocessing |
| Image processing | Multiprocessing |
| Background tasks | Celery + Workers |
| Real-time chat | AsyncIO |

---

# Best Practices

✓ Understand whether the workload is CPU-bound or I/O-bound.

✓ Avoid blocking operations in asynchronous applications.

✓ Measure performance before optimizing.

✓ Use concurrency only when it provides measurable benefits.

✓ Choose the simplest model that solves the problem.

---

# Common Mistakes

❌ Using threads for CPU-intensive Python code.

❌ Blocking the event loop with synchronous functions.

❌ Assuming concurrency always improves performance.

❌ Creating excessive threads.

❌ Ignoring resource contention.

---

# Interview Questions

### Easy

1. What is concurrency?
2. What is parallelism?
3. Difference between CPU-bound and I/O-bound tasks.
4. What is blocking code?
5. What is throughput?

---

### Medium

1. Compare synchronous and asynchronous programming.
2. Explain context switching.
3. Why doesn't concurrency always mean parallel execution?
4. How do you identify CPU-bound workloads?
5. Compare throughput and latency.

---

### Hard

1. Design a concurrent file processing system.
2. Explain how an asynchronous web server handles thousands of requests.
3. Compare concurrency models for different workloads.
4. Design a scalable background job system.
5. Explain trade-offs between threads, processes, and AsyncIO.

---

# Coding Exercises

Easy

- Measure execution time of sequential code.
- Simulate blocking operations.

Medium

- Build a concurrent file downloader.
- Compare synchronous and asynchronous implementations.

Hard

- Benchmark multiple concurrency models.
- Design a scalable task processing system.

---

# Module Summary

Concurrency allows multiple tasks to make progress efficiently, while parallelism enables tasks to execute simultaneously on multiple CPU cores. Choosing the right concurrency model depends on the workload: CPU-bound tasks benefit from multiprocessing, whereas I/O-bound tasks are better suited to asynchronous programming or threading. Understanding these fundamentals is essential before exploring Python's threading, multiprocessing, and AsyncIO libraries.

---

# Python Developer Knowledge Base
# Module 08 — Concurrency and Performance
# Part 2 — Processes, Threads & Python Execution Model

---

# What is a Process?

A process is an independent program in execution.

Each process has its own:

- Memory space
- Address space
- Variables
- File descriptors
- Stack
- Heap
- Program Counter

Example

```
Operating System

├── Chrome
├── VS Code
├── Python Program
└── Spotify
```

Each runs as a separate process.

---

# Process Memory Layout

```
+----------------------+
| Program Code (Text)  |
+----------------------+
| Initialized Data     |
+----------------------+
| Global Variables     |
+----------------------+
| Heap                 |
| (Dynamic Memory)     |
+----------------------+
|                      |
|      Free Space      |
|                      |
+----------------------+
| Stack                |
| (Function Calls)     |
+----------------------+
```

---

# Characteristics of a Process

✓ Independent execution

✓ Own memory

✓ Protected from other processes

✓ Managed by the operating system

✓ Can contain multiple threads

---

# Process Lifecycle

```
New

↓

Ready

↓

Running

↓

Waiting

↓

Ready

↓

Running

↓

Terminated
```

---

# Process States

### New

Process is created.

### Ready

Waiting for CPU time.

### Running

Currently executing.

### Waiting

Waiting for I/O or another event.

### Terminated

Execution completed.

---

# What is a Thread?

A thread is the smallest unit of execution inside a process.

A process may contain one or more threads.

Example

```
Python Process

├── Thread 1
├── Thread 2
├── Thread 3
```

---

# Thread Memory Model

Threads share:

- Heap
- Global Variables
- Open Files

Each thread has its own:

- Stack
- Registers
- Program Counter

---

# Thread Architecture

```
Process

+----------------------+
| Shared Heap          |
| Shared Globals       |
| Shared Files         |
+----------------------+

Thread A -> Stack A

Thread B -> Stack B

Thread C -> Stack C
```

---

# Why Threads?

Threads allow multiple tasks inside one process.

Examples

- Reading files
- Network requests
- Database queries
- UI updates
- Logging

---

# Process vs Thread

| Process | Thread |
|----------|---------|
| Independent | Part of a process |
| Own memory | Shared memory |
| Higher creation cost | Lower creation cost |
| More isolation | Less isolation |
| IPC required | Direct communication |

---

# Process Creation

Python uses the `multiprocessing` module.

Example

```python
from multiprocessing import Process

def worker():
    print("Worker running")

p = Process(target=worker)

p.start()

p.join()
```

---

# Thread Creation

Python uses the `threading` module.

```python
import threading

def worker():
    print("Worker running")

t = threading.Thread(target=worker)

t.start()

t.join()
```

---

# Daemon Threads

Daemon threads run in the background.

Examples

- Logging
- Monitoring
- Cleanup tasks

Example

```python
thread = threading.Thread(target=worker)

thread.daemon = True
```

Daemon threads terminate automatically when the main program exits.

---

# User Threads

User threads must complete before the process exits.

They are suitable for important work such as:

- Saving data
- Completing transactions
- Writing files

---

# Context Switching

The operating system switches execution between processes or threads.

Example

```
Thread A

↓

Thread B

↓

Thread C

↓

Thread A
```

Context switching enables multitasking but has overhead.

---

# Thread Scheduling

The operating system decides which thread executes next.

Factors include

- Priority
- Waiting time
- Fairness
- CPU availability

Python does not directly control OS thread scheduling.

---

# Process Scheduling

The operating system scheduler allocates CPU time to processes.

Goals

- Fairness
- High CPU utilization
- Low response time
- High throughput

---

# Shared Memory

Threads can directly access shared variables.

Example

```python
counter = 0
```

Every thread can read and modify `counter`.

This improves communication but introduces synchronization challenges.

---

# Race Condition

A race condition occurs when multiple threads modify shared data simultaneously.

Example

```
Counter = 5

↓

Thread A reads 5

↓

Thread B reads 5

↓

Both write 6

Expected: 7

Actual: 6
```

Race conditions lead to inconsistent results.

---

# Inter-Process Communication (IPC)

Processes have separate memory spaces.

Communication requires IPC mechanisms.

Common IPC Methods

- Pipes
- Queues
- Shared Memory
- Sockets
- Message Queues

---

# Pipes

Pipe communication

```
Process A

↓

Pipe

↓

Process B
```

Suitable for simple one-way communication.

---

# Queues

Queues provide thread-safe and process-safe communication.

Example

```
Producer

↓

Queue

↓

Consumer
```

Python

```python
from multiprocessing import Queue

queue = Queue()
```

---

# Shared Memory

Processes can explicitly share memory.

Useful for

- Large datasets
- High-performance computing

Requires careful synchronization.

---

# Sockets

Processes on the same or different machines communicate over a network.

Example

```
Server

↓

Socket

↓

Client
```

Sockets enable distributed systems.

---

# Thread Communication

Threads communicate through shared objects.

Examples

- Shared variables
- Queues
- Events
- Locks
- Conditions

---

# Producer-Consumer Pattern

```
Producer

↓

Queue

↓

Consumer
```

Applications

- Task queues
- Job processing
- Background workers

---

# Worker Pools

Instead of creating many threads repeatedly:

```
Task Queue

↓

Worker 1

Worker 2

Worker 3
```

Worker pools improve performance and reduce overhead.

---

# Process Pools

Useful for CPU-intensive workloads.

```
Task Queue

↓

Process Pool

↓

Results
```

Python

```python
from multiprocessing import Pool
```

---

# Thread Pools

Useful for I/O-bound workloads.

Python

```python
from concurrent.futures import ThreadPoolExecutor
```

---

# Process Pools vs Thread Pools

| Process Pool | Thread Pool |
|--------------|-------------|
| CPU-bound tasks | I/O-bound tasks |
| Separate memory | Shared memory |
| Higher overhead | Lower overhead |
| Bypasses GIL | Limited by GIL |

---

# Choosing Threads or Processes

Use Threads When

✓ Network requests

✓ File I/O

✓ Database operations

✓ Waiting for APIs

Use Processes When

✓ Image processing

✓ Video encoding

✓ Scientific computing

✓ CPU-intensive algorithms

---

# Best Practices

✓ Prefer thread pools over creating many threads.

✓ Use process pools for CPU-intensive tasks.

✓ Minimize shared mutable state.

✓ Use queues instead of shared variables where possible.

✓ Join threads and processes before exiting.

---

# Common Mistakes

❌ Creating thousands of threads.

❌ Sharing mutable data without synchronization.

❌ Using threads for CPU-bound Python code.

❌ Forgetting to join threads or processes.

❌ Assuming processes share memory automatically.

---

# Interview Questions

### Easy

1. What is a process?
2. What is a thread?
3. Difference between a process and a thread.
4. What is a daemon thread?
5. What is IPC?

---

### Medium

1. Explain shared memory.
2. What is a race condition?
3. Compare process pools and thread pools.
4. Explain producer-consumer architecture.
5. Why do processes require IPC?

---

### Hard

1. Design a concurrent image processing application.
2. Build a scalable producer-consumer system.
3. Explain how the operating system schedules processes.
4. Compare multiprocessing and multithreading for a web crawler.
5. Design a high-throughput task execution framework.

---

# Coding Exercises

Easy

- Create multiple threads.
- Create multiple processes.
- Print process IDs and thread IDs.

Medium

- Build a producer-consumer system using queues.
- Implement a thread pool.
- Implement a process pool.

Hard

- Build a parallel image processing pipeline.
- Design a distributed worker system using multiprocessing.
- Benchmark threads vs processes for different workloads.

---

# Module Summary

Processes and threads are the fundamental building blocks of concurrent applications. Processes provide isolation and are ideal for CPU-bound workloads, while threads share memory and are well suited for I/O-bound tasks. Understanding process lifecycles, memory models, context switching, IPC, and synchronization is essential for building scalable and efficient Python applications.

---

# Python Developer Knowledge Base
# Module 08 — Concurrency and Performance
# Part 3 — Global Interpreter Lock (GIL)

---

# Introduction to the GIL

The **Global Interpreter Lock (GIL)** is a mutex (mutual exclusion lock) used by the **CPython** interpreter.

It ensures that **only one thread executes Python bytecode at a time** within a single Python process.

Important Notes

- The GIL is specific to **CPython**.
- Not all Python implementations use a GIL.
- The GIL simplifies memory management but limits true parallel execution of Python bytecode.

---

# Why Does Python Have a GIL?

The GIL was introduced to simplify:

- Memory management
- Reference counting
- Object lifecycle
- Garbage collection

Without the GIL, CPython's reference counting mechanism would require complex synchronization for every object access.

---

# CPython Memory Management

Every Python object maintains a **reference count**.

Example

```python
x = []

y = x
```

Reference Count

```
x created

↓

Reference Count = 1

↓

Assigned to y

↓

Reference Count = 2
```

When the reference count reaches zero, the object can be deallocated.

---

# Why Reference Counting Needs Protection

Imagine two threads modifying the same object's reference count simultaneously.

```
Thread A

↓

Increment Count

----------------

Thread B

↓

Decrement Count
```

Without synchronization, the reference count could become incorrect, leading to memory corruption or crashes.

The GIL prevents multiple threads from modifying Python objects at the same time.

---

# How the GIL Works

```
Python Process

↓

Thread A

↓

GIL Acquired

↓

Execute Python Bytecode

↓

Release GIL

↓

Thread B Acquires GIL
```

Only one thread executes Python bytecode at any instant.

---

# GIL Execution Flow

```
Thread 1

↓

Acquire GIL

↓

Execute Python Code

↓

Release GIL

--------------------

Thread 2

↓

Acquire GIL

↓

Execute Python Code
```

Threads take turns executing.

---

# Does the GIL Prevent Concurrency?

No.

Threads can still make progress concurrently.

However, only one thread executes Python bytecode at a time.

This distinction is important.

---

# CPU-bound Example

```python
def calculate():

    for i in range(100000000):

        pass
```

Multiple threads executing this function do **not** significantly speed up execution because they compete for the GIL.

---

# I/O-bound Example

```python
import requests

response = requests.get(
    "https://example.com"
)
```

While waiting for network I/O, the thread releases the GIL, allowing another thread to execute.

Threads are therefore useful for many I/O-bound workloads.

---

# When Is the GIL Released?

The GIL is commonly released during blocking operations such as:

- File I/O
- Network I/O
- Database I/O
- Sleep operations
- Some C extensions performing long-running work

Example

```python
import time

time.sleep(2)
```

During `sleep()`, other threads can execute.

---

# CPU-bound vs I/O-bound with the GIL

| Workload | Thread Performance |
|----------|--------------------|
| CPU-bound | Poor scaling |
| I/O-bound | Good scaling |

Reason

CPU-bound threads spend their time executing Python bytecode and compete for the GIL.

I/O-bound threads spend much of their time waiting, allowing other threads to run.

---

# Example Timeline

CPU-bound Threads

```
Thread A

↓↓↓↓↓↓↓↓

Thread B

(waiting)

↓

Thread B

↓↓↓↓↓↓↓↓
```

Execution is mostly serialized.

---

I/O-bound Threads

```
Thread A

↓

Waiting

↓

Thread B Executes

↓

Waiting

↓

Thread C Executes
```

Overall throughput improves because waiting time is utilized.

---

# GIL and Multithreading

Threading is still valuable for:

- HTTP requests
- File downloads
- Database queries
- Web scraping
- API servers
- Socket programming

It is generally **not** the best choice for CPU-intensive computation.

---

# Multiprocessing Bypasses the GIL

Each process has its own:

- Memory space
- Python interpreter
- Global Interpreter Lock

Example

```
CPU Core 1

↓

Python Process A

↓

Own GIL

----------------

CPU Core 2

↓

Python Process B

↓

Own GIL
```

Processes can execute Python bytecode in parallel.

---

# Threads vs Processes with the GIL

| Threads | Processes |
|----------|-----------|
| One GIL per process | One GIL per process, but each process has its own interpreter |
| Shared memory | Separate memory |
| Lower overhead | Higher overhead |
| Good for I/O | Good for CPU |

---

# C Extensions and the GIL

Many C libraries temporarily release the GIL while performing computational work.

Examples include libraries such as:

- NumPy (many vectorized operations)
- OpenCV (many image operations)
- lxml (many parsing operations)

This allows native code to execute more efficiently and, in some cases, utilize multiple CPU cores.

---

# Common Misconceptions

### Misconception 1

"Python cannot use multiple CPU cores."

Incorrect.

Python can utilize multiple CPU cores using:

- Multiprocessing
- Multiple processes
- Native extensions that release the GIL

---

### Misconception 2

"Threads are useless in Python."

Incorrect.

Threads are highly effective for:

- Network applications
- File processing
- Database access
- Concurrent I/O

---

### Misconception 3

"The GIL makes Python slow."

Not necessarily.

Many real-world Python applications are I/O-bound, where the GIL has little impact.

---

# Alternatives to CPython

Some Python implementations differ in their handling of threading.

Examples

- PyPy
- Jython
- IronPython

Their implementation details and concurrency behavior differ from CPython.

---

# Free-Threaded Python (PEP 703)

PEP 703 introduces an **optional free-threaded build** of CPython that removes the traditional GIL.

Goals

- Better CPU-bound multithreading
- Improved scalability on multi-core systems

Key Points

- It is an optional build, not a mandatory replacement.
- Existing extensions may require updates for compatibility.
- Traditional GIL-based builds continue to exist.

---

# Choosing the Right Model

| Workload | Recommended Approach |
|----------|----------------------|
| Network requests | Threads or AsyncIO |
| Database operations | Threads or AsyncIO |
| File downloads | Threads or AsyncIO |
| Image processing | Multiprocessing |
| Scientific computing | Multiprocessing |
| Machine learning preprocessing | Depends on workload; multiprocessing is common for CPU-bound work |

---

# Best Practices

✓ Use threads for I/O-bound work.

✓ Use multiprocessing for CPU-bound work.

✓ Benchmark your application before optimizing.

✓ Minimize shared mutable state.

✓ Understand when libraries release the GIL.

---

# Common Mistakes

❌ Expecting CPU-bound threads to scale across cores.

❌ Ignoring multiprocessing for computational workloads.

❌ Assuming the GIL affects every operation equally.

❌ Optimizing before measuring performance.

---

# Interview Questions

### Easy

1. What is the Global Interpreter Lock?
2. Why does CPython use the GIL?
3. Does the GIL prevent concurrency?
4. When is the GIL released?
5. Why are threads useful for I/O-bound work?

---

### Medium

1. Explain how the GIL affects multithreading.
2. Compare threads and processes in the presence of the GIL.
3. Why is multiprocessing effective for CPU-bound tasks?
4. How does reference counting relate to the GIL?
5. Give examples of operations that release the GIL.

---

### Hard

1. Explain the internal motivation behind the GIL.
2. Design a high-performance image processing system considering the GIL.
3. Compare AsyncIO, threading, and multiprocessing for different workloads.
4. Discuss the trade-offs of removing the GIL.
5. Explain the goals of PEP 703 and its potential impact.

---

# Coding Exercises

Easy

- Compare execution time of one CPU-bound thread versus two CPU-bound threads.
- Create multiple threads performing HTTP requests.

Medium

- Compare threading and multiprocessing for calculating prime numbers.
- Benchmark file downloads using threads.

Hard

- Build a parallel image processing pipeline using multiprocessing.
- Measure performance differences between threading, multiprocessing, and AsyncIO for different workloads.

---

# Module Summary

The Global Interpreter Lock is a synchronization mechanism in CPython that allows only one thread to execute Python bytecode at a time within a process. It simplifies memory management and reference counting but limits CPU-bound multithreading. Threads remain an excellent choice for I/O-bound tasks because the GIL is released during many blocking operations, while multiprocessing enables true parallel execution by using separate Python processes. Understanding the GIL is essential for selecting the most effective concurrency model for a given workload.

---

# Python Developer Knowledge Base
# Module 08 — Concurrency and Performance
# Part 4 — Multithreading, Synchronization & Thread Safety

---

# Introduction to Multithreading

Multithreading allows multiple threads to execute within the same process.

Characteristics

- Shared memory
- Lightweight
- Fast context switching
- Suitable for I/O-bound workloads

Examples

- Web servers
- File downloads
- Database access
- Logging
- Background tasks

---

# Python threading Module

Python provides the built-in `threading` module.

Example

```python
import threading

def worker():
    print("Worker thread running")

thread = threading.Thread(target=worker)

thread.start()

thread.join()
```

---

# Thread Lifecycle

```
New

↓

Runnable

↓

Running

↓

Blocked / Waiting

↓

Runnable

↓

Terminated
```

---

# Creating Multiple Threads

```python
import threading

def worker(n):
    print(f"Worker {n}")

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

---

# Thread Join

`join()` blocks the calling thread until the target thread finishes.

```python
thread.start()

thread.join()

print("Completed")
```

Without `join()`, the main thread may exit before worker threads finish.

---

# Daemon Threads

Daemon threads run in the background.

Example

```python
thread = threading.Thread(target=worker)

thread.daemon = True

thread.start()
```

Daemon threads terminate automatically when the main program exits.

Use Cases

- Logging
- Monitoring
- Cleanup

---

# Non-Daemon Threads

Default thread type.

The process waits for all non-daemon threads to complete before exiting.

---

# Thread Naming

```python
thread = threading.Thread(

    target=worker,

    name="Downloader"
)
```

Useful for debugging and logging.

---

# Thread Identifiers

```python
import threading

print(threading.get_ident())
```

Useful when debugging concurrent applications.

---

# Shared Variables

Threads share global memory.

Example

```python
counter = 0
```

Every thread can read and modify the same variable.

---

# Thread Safety

Thread-safe code behaves correctly when accessed by multiple threads simultaneously.

Unsafe Example

```python
counter += 1
```

This operation is **not atomic**.

---

# Race Condition

Example

```
Counter = 10

↓

Thread A reads 10

↓

Thread B reads 10

↓

Thread A writes 11

↓

Thread B writes 11

Expected: 12

Actual: 11
```

Race conditions occur when multiple threads access shared data without synchronization.

---

# Lock

A `Lock` ensures that only one thread accesses a critical section at a time.

```python
import threading

lock = threading.Lock()

with lock:
    counter += 1
```

Equivalent

```python
lock.acquire()

try:
    counter += 1
finally:
    lock.release()
```

---

# Critical Section

A critical section is code that accesses shared resources.

```
Shared Data

↓

Critical Section

↓

Lock Required
```

---

# Reentrant Lock (RLock)

A thread may acquire the same lock multiple times.

```python
lock = threading.RLock()
```

Useful for recursive functions or nested locking.

---

# Lock vs RLock

| Lock | RLock |
|------|--------|
| Cannot be acquired twice by same thread | Same thread can acquire multiple times |
| Simpler | Slightly more overhead |

---

# Deadlock

Deadlock occurs when two or more threads wait indefinitely for each other.

Example

```
Thread A

↓

Lock 1

↓

Waiting for Lock 2

--------------------

Thread B

↓

Lock 2

↓

Waiting for Lock 1
```

Neither thread can proceed.

---

# Deadlock Prevention

Best Practices

- Acquire locks in a consistent order.
- Keep critical sections short.
- Avoid nested locks when possible.
- Use timeouts for lock acquisition.

---

# Livelock

Threads remain active but make no progress.

Example

```
Thread A yields

↓

Thread B yields

↓

Thread A yields

↓

Thread B yields
```

Unlike deadlocks, threads continue running but never complete useful work.

---

# Starvation

A thread waits indefinitely because other threads continuously receive access to shared resources.

Causes

- Poor scheduling
- High-priority threads monopolizing resources

---

# Semaphore

A semaphore allows a fixed number of threads to access a resource simultaneously.

```python
import threading

semaphore = threading.Semaphore(3)
```

Example

```
Database Connection Pool

Maximum Connections = 3
```

---

# Bounded Semaphore

```python
threading.BoundedSemaphore(5)
```

Raises an error if released more times than acquired.

Useful for resource management.

---

# Event

Threads communicate using events.

```python
event = threading.Event()

event.set()

event.wait()
```

Use Cases

- Signaling
- Task coordination
- Background processing

---

# Condition Variable

Allows threads to wait until a condition becomes true.

```python
condition = threading.Condition()
```

Commonly used in producer-consumer systems.

---

# Producer-Consumer with Queue

Python's `queue.Queue` is thread-safe.

```python
from queue import Queue

queue = Queue()
```

Architecture

```
Producer

↓

Queue

↓

Consumer
```

No explicit locks are required for queue operations.

---

# ThreadPoolExecutor

Creating many threads manually is inefficient.

Python provides

```python
from concurrent.futures import ThreadPoolExecutor
```

Example

```python
from concurrent.futures import ThreadPoolExecutor

def worker(n):
    return n * n

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(worker, [1, 2, 3, 4])

print(list(results))
```

Benefits

- Thread reuse
- Simpler code
- Better resource management

---

# Futures

A `Future` represents the result of an asynchronous computation.

```python
future = executor.submit(worker, 10)

result = future.result()
```

Methods

- `result()`
- `done()`
- `cancel()`
- `exception()`

---

# Exception Handling in Threads

Exceptions raised inside threads do not automatically propagate to the main thread.

When using `Future`, exceptions are re-raised when calling `result()`.

Example

```python
future = executor.submit(worker)

try:
    result = future.result()
except Exception as e:
    print(e)
```

---

# Thread Pools vs Manual Threads

| Manual Threads | ThreadPoolExecutor |
|----------------|--------------------|
| Manual management | Automatic management |
| Higher overhead | Thread reuse |
| More boilerplate | Cleaner API |

---

# Performance Considerations

Advantages

✓ Low creation cost

✓ Shared memory

✓ Efficient for I/O

Limitations

- GIL limits CPU-bound parallelism
- Synchronization overhead
- Context switching

---

# Best Practices

✓ Prefer `ThreadPoolExecutor` over manual thread creation.

✓ Protect shared data with locks.

✓ Minimize lock duration.

✓ Use `queue.Queue` for producer-consumer patterns.

✓ Avoid excessive thread creation.

✓ Design thread-safe code.

---

# Common Mistakes

❌ Updating shared variables without synchronization.

❌ Holding locks longer than necessary.

❌ Ignoring deadlocks.

❌ Creating hundreds of unnecessary threads.

❌ Using threads for CPU-bound computation.

---

# Interview Questions

### Easy

1. What is multithreading?
2. What is `join()`?
3. What is a daemon thread?
4. What is a lock?
5. What is a race condition?

---

### Medium

1. Compare `Lock` and `RLock`.
2. What is thread safety?
3. Explain deadlock and how to prevent it.
4. What is a semaphore?
5. Why use `ThreadPoolExecutor`?

---

### Hard

1. Design a thread-safe banking system.
2. Explain producer-consumer architecture using queues.
3. Compare thread pools and process pools.
4. Design a multithreaded web crawler.
5. Build a thread-safe cache.

---

# Coding Exercises

Easy

- Create multiple threads.
- Synchronize a shared counter using a lock.
- Print thread names and IDs.

Medium

- Build a producer-consumer queue.
- Use `ThreadPoolExecutor` for file downloads.
- Coordinate threads with events.

Hard

- Implement a thread-safe LRU cache.
- Design a multithreaded log processing system.
- Benchmark thread pool performance under different workloads.

---

# Module Summary

Python's `threading` module enables concurrent execution of I/O-bound tasks within a single process. Because threads share memory, synchronization mechanisms such as locks, semaphores, events, and queues are essential for maintaining thread safety. Thread pools simplify concurrent programming by managing worker threads efficiently, while understanding race conditions, deadlocks, and synchronization primitives is crucial for writing reliable multithreaded applications.

---

# Python Developer Knowledge Base
# Module 08 — Concurrency and Performance
# Part 5 — Multiprocessing & Parallel Computing

---

# Why Multiprocessing?

Because of the Global Interpreter Lock (GIL), CPU-bound Python threads cannot execute Python bytecode in parallel.

Multiprocessing solves this problem by creating multiple independent Python processes.

Each process has:

- Its own Python interpreter
- Its own GIL
- Separate memory space
- Independent execution

Example

```
CPU Core 1

↓

Python Process A

--------------------

CPU Core 2

↓

Python Process B

--------------------

CPU Core 3

↓

Python Process C
```

---

# multiprocessing Module

Python provides the built-in `multiprocessing` module.

Example

```python
from multiprocessing import Process

def worker():
    print("Worker running")

if __name__ == "__main__":
    p = Process(target=worker)

    p.start()

    p.join()
```

---

# Why Use `if __name__ == "__main__"`?

On Windows (and with the `spawn` start method), child processes import the main module.

Without the guard, process creation can recurse indefinitely.

Correct

```python
if __name__ == "__main__":
    main()
```

---

# Process Lifecycle

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

↓

Joined
```

---

# Process ID (PID)

Every process has a unique Process ID.

Example

```python
import os

print(os.getpid())
```

Current parent process

```python
os.getppid()
```

---

# Multiple Processes

```python
from multiprocessing import Process

def worker(n):
    print(n)

if __name__ == "__main__":
    processes = []

    for i in range(5):
        p = Process(target=worker, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
```

---

# Process Pool

Creating processes repeatedly is expensive.

Use

```python
from multiprocessing import Pool
```

Example

```python
from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == "__main__":
    with Pool(4) as pool:
        result = pool.map(square, [1,2,3,4])

    print(result)
```

---

# Pool Methods

Common methods

```
map()

starmap()

apply()

apply_async()

imap()

imap_unordered()
```

---

# Pool.map()

```
Input

↓

Worker Processes

↓

Results
```

Maintains input order.

---

# apply()

Runs one task synchronously.

```
Task

↓

Worker

↓

Result
```

---

# apply_async()

Runs asynchronously.

Example

```python
result = pool.apply_async(square, (10,))

print(result.get())
```

---

# ProcessPoolExecutor

Modern interface

```python
from concurrent.futures import ProcessPoolExecutor
```

Example

```python
from concurrent.futures import ProcessPoolExecutor

def square(x):
    return x*x

with ProcessPoolExecutor() as executor:

    result = executor.map(square, range(10))
```

Advantages

✓ Cleaner API

✓ Futures support

✓ Consistent with ThreadPoolExecutor

---

# Inter-Process Communication (IPC)

Processes do not share memory automatically.

Communication mechanisms include

- Queue
- Pipe
- Shared Memory
- Manager
- Socket

---

# Queue

Safe communication between processes.

```python
from multiprocessing import Queue

queue = Queue()
```

Example

```python
queue.put("Hello")

queue.get()
```

Architecture

```
Producer

↓

Queue

↓

Consumer
```

---

# Pipe

Suitable for communication between two processes.

```python
from multiprocessing import Pipe

parent, child = Pipe()
```

Example

```python
parent.send("Hello")

child.recv()
```

---

# Queue vs Pipe

| Queue | Pipe |
|--------|------|
| Multiple producers/consumers | Mainly two endpoints |
| Thread/process safe | Simpler communication |
| Higher flexibility | Lower overhead for simple cases |

---

# Shared Memory

Processes normally have isolated memory.

Python provides shared memory support.

```python
from multiprocessing import shared_memory
```

Useful for

- Large NumPy arrays
- Scientific computing
- Image processing

---

# Shared Value

```python
from multiprocessing import Value

counter = Value('i', 0)
```

The first argument specifies the data type.

Example

```
'i'

↓

Integer
```

---

# Shared Array

```python
from multiprocessing import Array

numbers = Array('i', [1,2,3,4])
```

Allows multiple processes to access shared arrays.

---

# Manager

Managers provide shared objects.

```python
from multiprocessing import Manager

manager = Manager()

shared_list = manager.list()

shared_dict = manager.dict()
```

Supported Types

- List
- Dictionary
- Namespace
- Queue
- Lock

---

# Synchronization Between Processes

Even though memory is separate, shared resources still require synchronization.

Available primitives

- Lock
- RLock
- Semaphore
- Event
- Condition
- Barrier

---

# Process Lock

```python
from multiprocessing import Lock

lock = Lock()
```

Used similarly to threading locks.

---

# Event

```python
event = Event()

event.wait()

event.set()
```

Coordinates processes.

---

# Barrier

Allows multiple processes to wait until everyone reaches a synchronization point.

Example

```
Process A

↓

Barrier

↓

Continue

----------------

Process B

↓

Barrier

↓

Continue
```

---

# Start Methods

Python supports different process start methods.

- spawn
- fork
- forkserver

---

# spawn

- Starts a fresh Python interpreter.
- Default on Windows.
- More portable.
- Higher startup cost.

---

# fork

- Copies the parent process.
- Available on many Unix-like systems.
- Faster startup.
- Can inherit resources unexpectedly.

---

# forkserver

- Starts a dedicated server process.
- Child processes are forked from the server.
- Helps avoid some issues associated with `fork`.

---

# CPU Count

Determine available CPU cores.

```python
import multiprocessing

print(multiprocessing.cpu_count())
```

Useful when sizing process pools.

---

# Choosing Pool Size

General guideline

```
CPU-bound Tasks

↓

Number of CPU Cores
```

Creating significantly more worker processes than cores may increase context switching overhead.

---

# Parallel Processing Patterns

### Data Parallelism

```
Dataset

↓

Split

↓

Worker 1

Worker 2

Worker 3

↓

Merge Results
```

---

### Task Parallelism

```
Task A

↓

Worker 1

Task B

↓

Worker 2

Task C

↓

Worker 3
```

Different workers perform different tasks.

---

# Example Use Cases

Suitable for multiprocessing

- Image processing
- Video encoding
- Data analysis
- Machine learning preprocessing
- Scientific simulations
- Prime number generation

---

# When Not to Use Multiprocessing

Avoid when

- Tasks are very small
- Startup overhead dominates
- Memory usage is constrained
- Workload is primarily I/O-bound

---

# Performance Considerations

Advantages

✓ True parallel execution

✓ Utilizes multiple CPU cores

✓ Bypasses the GIL

Trade-offs

- Higher memory usage
- Process creation overhead
- IPC overhead
- Data serialization costs

---

# Multiprocessing vs Multithreading

| Multiprocessing | Multithreading |
|-----------------|----------------|
| Multiple processes | Multiple threads |
| Separate memory | Shared memory |
| True parallelism | Limited by GIL for Python bytecode |
| Higher overhead | Lower overhead |
| CPU-bound workloads | I/O-bound workloads |

---

# Best Practices

✓ Use process pools instead of manually creating many processes.

✓ Keep tasks sufficiently large to amortize process startup costs.

✓ Minimize inter-process communication.

✓ Avoid transferring large objects repeatedly between processes.

✓ Protect the entry point with `if __name__ == "__main__"`.

✓ Benchmark before optimizing.

---

# Common Mistakes

❌ Forgetting the `__main__` guard.

❌ Creating too many processes.

❌ Sending very large objects through queues repeatedly.

❌ Assuming processes share global variables.

❌ Using multiprocessing for simple I/O-bound tasks.

---

# Interview Questions

### Easy

1. What is multiprocessing?
2. Why does multiprocessing bypass the GIL?
3. What is a process pool?
4. What is IPC?
5. Difference between `Queue` and `Pipe`.

---

### Medium

1. Compare `multiprocessing.Pool` and `ProcessPoolExecutor`.
2. Explain shared memory.
3. Why is `if __name__ == "__main__"` required?
4. Compare `spawn` and `fork`.
5. When should you use multiprocessing?

---

### Hard

1. Design a parallel image processing pipeline.
2. Compare multiprocessing, threading, and AsyncIO for different workloads.
3. Optimize a CPU-intensive application using process pools.
4. Design a distributed computation framework.
5. Explain the trade-offs of shared memory versus message passing.

---

# Coding Exercises

Easy

- Create multiple processes.
- Print process IDs.
- Exchange messages using a `Queue`.

Medium

- Build a parallel file checksum calculator.
- Use `Pool.map()` to process a large dataset.
- Synchronize processes using a `Lock`.

Hard

- Parallelize image transformations using shared memory.
- Implement a multiprocessing-based web crawler with separate worker processes.
- Benchmark sequential, multithreaded, and multiprocessing implementations of a CPU-bound algorithm.

---

# Module Summary

The `multiprocessing` module enables true parallel execution by running independent Python processes, each with its own interpreter and GIL. It is the preferred approach for CPU-bound workloads. Process pools, IPC mechanisms such as queues and pipes, shared memory, and synchronization primitives provide the tools needed to build scalable parallel applications while balancing performance, memory usage, and communication overhead.

---

# Python Developer Knowledge Base
# Module 08 — Concurrency and Performance
# Part 6 — AsyncIO, Event Loop & Coroutines

---

# What is AsyncIO?

AsyncIO is Python's framework for writing asynchronous programs.

It enables a single thread to efficiently manage thousands of concurrent I/O operations.

Examples

- REST APIs
- WebSockets
- Chat servers
- Database connections
- File downloads
- Web scraping
- Microservices

---

# Why AsyncIO?

Traditional synchronous execution

```
Task A

↓

Wait

↓

Task B

↓

Wait

↓

Task C
```

CPU remains idle while waiting.

---

AsyncIO

```
Task A

↓

Waiting

↓

Task B

↓

Waiting

↓

Task C

↓

Resume Task A
```

Waiting time is used productively.

---

# AsyncIO Characteristics

✓ Single-threaded

✓ Event-driven

✓ Non-blocking

✓ Efficient for I/O-bound workloads

✓ Low memory overhead

---

# Synchronous Example

```python
import time

def work():
    time.sleep(2)
    print("Done")

work()
```

The entire program blocks for two seconds.

---

# Asynchronous Example

```python
import asyncio

async def work():
    await asyncio.sleep(2)
    print("Done")

asyncio.run(work())
```

The event loop can execute other tasks while waiting.

---

# What is a Coroutine?

A coroutine is a special function defined using `async def`.

Example

```python
async def greet():
    print("Hello")
```

Calling it

```python
greet()
```

returns a coroutine object—it does **not** execute immediately.

---

# Running a Coroutine

```python
import asyncio

async def greet():
    print("Hello")

asyncio.run(greet())
```

`asyncio.run()` creates an event loop, runs the coroutine, and closes the loop.

---

# async Keyword

Marks a function as asynchronous.

```python
async def fetch_data():
    ...
```

---

# await Keyword

Suspends the current coroutine until another awaitable completes.

```python
await asyncio.sleep(1)
```

While suspended, the event loop can run other coroutines.

---

# Event Loop

The event loop is the core of AsyncIO.

Responsibilities

- Schedule tasks
- Resume suspended coroutines
- Handle I/O events
- Coordinate execution

Architecture

```
Coroutines

↓

Event Loop

↓

Operating System
```

---

# Event Loop Workflow

```
Coroutine A

↓

Waiting

↓

Coroutine B Executes

↓

Waiting

↓

Coroutine C Executes

↓

Resume Coroutine A
```

The event loop continuously switches between ready tasks.

---

# Blocking vs Non-Blocking

Blocking

```python
time.sleep(2)
```

Non-blocking

```python
await asyncio.sleep(2)
```

Using blocking functions inside async code can pause the entire event loop.

---

# Awaitables

Objects that can be awaited include:

- Coroutines
- Tasks
- Futures

Example

```python
await some_coroutine()
```

---

# Tasks

A Task wraps a coroutine and schedules it for execution.

```python
task = asyncio.create_task(work())
```

Tasks begin running independently under the event loop.

---

# create_task()

Example

```python
async def work():
    await asyncio.sleep(1)

async def main():

    task = asyncio.create_task(work())

    await task

asyncio.run(main())
```

---

# Running Multiple Tasks

Sequential

```
Task A

↓

Task B

↓

Task C
```

Concurrent

```
Task A

Task B

Task C
```

---

# asyncio.gather()

Run multiple coroutines concurrently.

```python
results = await asyncio.gather(

    task1(),

    task2(),

    task3()
)
```

Returns results in the same order as the input coroutines.

---

# gather() Example

```python
async def fetch(n):

    await asyncio.sleep(1)

    return n

async def main():

    result = await asyncio.gather(

        fetch(1),

        fetch(2),

        fetch(3)
    )

    print(result)
```

Output

```
[1, 2, 3]
```

---

# asyncio.wait()

Wait for multiple tasks with more control.

Useful for

- Waiting for the first completed task
- Waiting with timeouts
- Handling partial completion

---

# Futures

A Future represents a result that will become available later.

Example

```
Task Running

↓

Future

↓

Completed Result
```

Tasks are built on top of futures.

---

# Cancellation

Tasks can be cancelled.

```python
task.cancel()
```

Cancellation raises

```
asyncio.CancelledError
```

Coroutines should handle cancellation gracefully when appropriate.

---

# Timeouts

```python
await asyncio.wait_for(

    fetch_data(),

    timeout=5
)
```

Raises

```
TimeoutError
```

if the operation exceeds the specified duration.

---

# Async Context Manager

Use `async with` for asynchronous resource management.

Example

```python
async with session.get(url) as response:
    data = await response.text()
```

Common use cases

- HTTP clients
- Database connections
- Network streams

---

# Async Iteration

Asynchronous iterables use `async for`.

```python
async for item in stream:
    print(item)
```

Useful for streaming large datasets or consuming asynchronous data sources.

---

# Async Generators

Example

```python
async def numbers():

    for i in range(5):

        yield i
```

Consume with

```python
async for n in numbers():
    print(n)
```

---

# Async Queue

```python
queue = asyncio.Queue()
```

Producer

```python
await queue.put(item)
```

Consumer

```python
item = await queue.get()
```

Useful for coordinating asynchronous producer-consumer workflows.

---

# Producer-Consumer Pattern

```
Producer

↓

Async Queue

↓

Consumer
```

Supports backpressure and coordinated task processing.

---

# Mixing Blocking Code

Avoid

```python
time.sleep(2)
```

Inside async functions.

Instead

```python
await asyncio.sleep(2)
```

Blocking operations freeze the event loop.

---

# Running Blocking Code

For CPU-bound or blocking functions

```python
await asyncio.to_thread(blocking_function)
```

or use an executor.

This prevents blocking the event loop.

---

# AsyncIO vs Threads

| AsyncIO | Threads |
|----------|----------|
| Single thread | Multiple threads |
| Event loop | OS scheduler |
| Lower memory usage | Higher memory usage |
| Ideal for I/O | Good for I/O |
| No thread synchronization | Shared-memory synchronization required |

---

# AsyncIO vs Multiprocessing

| AsyncIO | Multiprocessing |
|----------|-----------------|
| I/O-bound workloads | CPU-bound workloads |
| One process | Multiple processes |
| Low overhead | Higher overhead |
| Does not bypass GIL for Python bytecode | Bypasses GIL |

---

# Common AsyncIO Libraries

- aiohttp
- httpx (async client)
- asyncpg
- aiomysql
- Motor (MongoDB)
- FastAPI
- websockets

---

# Best Practices

✓ Use AsyncIO for I/O-bound applications.

✓ Replace blocking calls with asynchronous equivalents.

✓ Use `asyncio.gather()` for independent concurrent operations.

✓ Handle task cancellation appropriately.

✓ Reuse connections where possible.

✓ Avoid long-running CPU work in the event loop.

---

# Common Mistakes

❌ Calling blocking functions inside async code.

❌ Forgetting `await`.

❌ Creating tasks without awaiting or managing them.

❌ Using AsyncIO for CPU-intensive computation.

❌ Mixing synchronous and asynchronous APIs carelessly.

---

# Interview Questions

### Easy

1. What is AsyncIO?
2. What is a coroutine?
3. Difference between `async` and `await`.
4. What is the event loop?
5. What is a task?

---

### Medium

1. Compare AsyncIO and multithreading.
2. Explain `asyncio.gather()`.
3. What happens if you call `time.sleep()` inside an async function?
4. What is an async context manager?
5. Explain task cancellation.

---

### Hard

1. Design an asynchronous web crawler.
2. Explain how FastAPI handles thousands of concurrent requests.
3. Compare AsyncIO, threading, and multiprocessing for various workloads.
4. Design a scalable WebSocket server.
5. Build a producer-consumer pipeline using `asyncio.Queue`.

---

# Coding Exercises

Easy

- Write an async function using `asyncio.sleep()`.
- Execute multiple coroutines with `asyncio.gather()`.

Medium

- Build an asynchronous file downloader.
- Implement an async producer-consumer queue.
- Handle timeouts and cancellations.

Hard

- Build an asynchronous web crawler.
- Implement a concurrent API aggregator using AsyncIO.
- Benchmark synchronous, threaded, and asynchronous implementations of the same I/O-bound workload.

---

# Module Summary

AsyncIO provides an efficient framework for handling high-concurrency I/O-bound workloads using coroutines and an event loop. By suspending tasks during waiting periods and resuming them when resources become available, AsyncIO achieves excellent scalability with minimal overhead. Concepts such as coroutines, tasks, `async`/`await`, event loops, asynchronous queues, and cancellation are fundamental for modern Python frameworks like FastAPI and other asynchronous applications.

---

# Python Developer Knowledge Base
# Module 08 — Concurrency and Performance
# Part 7 (Final) — Performance Profiling, Memory Optimization & Best Practices

---

# Why Performance Matters

Performance determines how efficiently an application uses:

- CPU
- Memory
- Disk
- Network
- Database

Goals

- Lower response time
- Higher throughput
- Reduced resource usage
- Better scalability

---

# Performance Optimization Process

Never optimize blindly.

Recommended workflow

```
Measure

↓

Profile

↓

Identify Bottlenecks

↓

Optimize

↓

Measure Again
```

Premature optimization often increases complexity without measurable benefits.

---

# Benchmarking

Benchmarking measures execution time under controlled conditions.

Example

```python
import time

start = time.perf_counter()

# Code here

end = time.perf_counter()

print(end - start)
```

Use multiple runs to obtain reliable measurements.

---

# timeit Module

Designed specifically for benchmarking small code snippets.

Example

```python
import timeit

result = timeit.timeit(

    "sum(range(1000))",

    number=10000
)

print(result)
```

Advantages

- Repeated execution
- More accurate timing
- Reduced measurement noise

---

# cProfile

Built-in profiler for identifying CPU bottlenecks.

Run

```bash
python -m cProfile app.py
```

Output includes

- Function calls
- Total execution time
- Cumulative time
- Call counts

---

# Reading cProfile Output

Important columns

- ncalls
- tottime
- percall
- cumtime

Focus first on functions with high cumulative execution time.

---

# Profiling Workflow

```
Application

↓

cProfile

↓

Slow Functions

↓

Optimize

↓

Re-profile
```

---

# Memory Profiling

CPU is not the only bottleneck.

Memory usage affects

- Performance
- Scalability
- Stability

---

# tracemalloc

Built-in module for tracking memory allocations.

Example

```python
import tracemalloc

tracemalloc.start()

# Code here

snapshot = tracemalloc.take_snapshot()
```

Useful for identifying memory growth and allocation hotspots.

---

# memory_profiler

Example

```python
from memory_profiler import profile

@profile
def process():
    ...
```

Provides line-by-line memory usage (requires the external package).

---

# Memory Leak

A memory leak occurs when memory is no longer needed but is still referenced.

Example

```
Object Created

↓

Reference Retained

↓

Garbage Collector Cannot Free It
```

Symptoms

- Increasing memory usage
- Slower performance
- Potential crashes

---

# Garbage Collection

Python uses

- Reference counting
- Cyclic garbage collector

Useful module

```python
import gc

gc.collect()
```

Manual collection is rarely required in normal applications.

---

# Lazy Evaluation

Compute values only when needed.

Example

```python
range(1000000)
```

`range` does not allocate a list of one million integers.

Advantages

- Lower memory usage
- Faster startup
- Better scalability

---

# Generators

Generators produce values one at a time.

Example

```python
def numbers():

    for i in range(1000000):

        yield i
```

Memory usage remains small regardless of sequence size.

---

# List vs Generator

List

```python
[x for x in range(1000000)]
```

Generator

```python
(x for x in range(1000000))
```

| List | Generator |
|------|-----------|
| Stores all values | Produces values on demand |
| Higher memory usage | Lower memory usage |
| Faster repeated access | Single-pass iteration |

---

# functools.lru_cache

Memoization stores results of expensive function calls.

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

- Avoids repeated computation
- Improves performance for pure functions

---

# Caching

Common cache layers

```
Application

↓

Redis

↓

Database
```

Types

- In-memory cache
- Redis
- CDN
- Browser cache

---

# Database Optimization

Common techniques

- Indexing
- Query optimization
- Connection pooling
- Pagination
- Avoiding N+1 queries

Database performance often dominates API latency.

---

# Efficient Data Structures

Choose appropriate data structures.

| Operation | Preferred Structure |
|-----------|---------------------|
| Fast lookup | Dictionary (`dict`) |
| Membership testing | Set (`set`) |
| Ordered sequence | List (`list`) |
| Queue | `collections.deque` |

Selecting the right data structure can significantly improve performance.

---

# Avoid Unnecessary Work

Bad

```python
for item in items:
    expensive_function(item)
```

If results are reused, consider caching or precomputing where appropriate.

---

# Vectorized Operations

For numerical computation, vectorized libraries (e.g., NumPy) are typically much faster than explicit Python loops because they execute optimized native code.

---

# Batch Processing

Instead of

```
1000 Database Inserts
```

Perform

```
1 Batch Insert
```

Advantages

- Fewer network round trips
- Better throughput
- Lower database overhead

---

# Connection Pooling

Instead of creating a database connection for every request

```
Connection Pool

↓

Reusable Connections

↓

Database
```

Benefits

- Lower latency
- Reduced connection overhead

---

# Performance Anti-Patterns

Avoid

- Premature optimization
- Excessive object creation
- Unnecessary copying
- Large temporary lists
- Blocking operations in AsyncIO
- Overusing threads or processes
- Repeated database queries inside loops

---

# Choosing the Right Concurrency Model

| Workload | Best Choice |
|----------|-------------|
| CPU-bound computation | Multiprocessing |
| Network I/O | AsyncIO |
| Database queries | AsyncIO or Threads |
| File I/O | AsyncIO or Threads |
| Image processing | Multiprocessing |
| Background jobs | Process Pool / Celery Workers |
| Real-time WebSockets | AsyncIO |

---

# Concurrency Decision Matrix

```
Is the workload CPU-bound?

        │
        ├── Yes
        │      ↓
        │  Multiprocessing
        │
        └── No
               ↓
        Is it I/O-bound?

               │
               ├── Yes
               │      ↓
               │ AsyncIO or Threads
               │
               └── No
                      ↓
             Sequential execution may be sufficient
```

---

# Performance Monitoring

Track

- CPU usage
- Memory usage
- Request latency
- Throughput
- Error rate
- Database query time
- Queue length

Popular tools

- Prometheus
- Grafana
- OpenTelemetry

---

# Scaling Strategies

Vertical Scaling

```
More CPU

More RAM
```

Horizontal Scaling

```
Load Balancer

↓

Server A

Server B

Server C
```

Horizontal scaling improves resilience and capacity.

---

# Best Practices

✓ Measure before optimizing.

✓ Use profiling tools to locate bottlenecks.

✓ Prefer generators for large data streams.

✓ Cache expensive computations when appropriate.

✓ Use efficient algorithms and data structures.

✓ Batch database operations.

✓ Choose the correct concurrency model.

✓ Continuously monitor production systems.

---

# Common Mistakes

❌ Optimizing without profiling.

❌ Loading huge datasets into memory unnecessarily.

❌ Ignoring database performance.

❌ Using multiprocessing for tiny tasks.

❌ Blocking the AsyncIO event loop.

❌ Creating excessive threads or processes.

❌ Recomputing identical results repeatedly.

---

# Performance Cheat Sheet

| Goal | Technique |
|------|-----------|
| Reduce execution time | Profile, optimize algorithms |
| Reduce memory usage | Generators, lazy evaluation |
| Speed repeated calculations | `lru_cache` |
| Improve database performance | Indexing, batching |
| Increase CPU utilization | Multiprocessing |
| Improve I/O throughput | AsyncIO |
| Scale services | Load balancing |

---

# Interview Questions

### Easy

1. What is profiling?
2. Difference between benchmarking and profiling.
3. What is lazy evaluation?
4. What is a generator?
5. What is memoization?

---

### Medium

1. Explain `cProfile`.
2. Compare lists and generators.
3. How would you detect a memory leak?
4. When should you use `lru_cache`?
5. Compare `timeit` and `perf_counter()`.

---

### Hard

1. Optimize an API handling millions of requests per day.
2. Design a high-performance data processing pipeline.
3. Compare profiling strategies for CPU and memory bottlenecks.
4. Explain how to optimize a database-heavy application.
5. Design a scalable architecture for concurrent task processing.

---

# Coding Exercises

Easy

- Benchmark two implementations using `timeit`.
- Convert a list-producing function into a generator.
- Cache an expensive recursive function with `lru_cache`.

Medium

- Profile an application with `cProfile`.
- Identify and reduce memory usage using `tracemalloc`.
- Batch database-like operations in a simulation.

Hard

- Build a concurrent file processing pipeline and profile it.
- Optimize a slow API endpoint using caching and profiling.
- Compare sequential, threaded, multiprocessing, and AsyncIO implementations of the same workload.

---

# Module Summary

Building high-performance Python applications requires measuring before optimizing, identifying bottlenecks with profiling tools, and selecting the appropriate concurrency model for the workload. Techniques such as generators, lazy evaluation, memoization, batching, efficient data structures, caching, and connection pooling improve both speed and memory efficiency. Combined with proper monitoring and scalability strategies, these practices enable production-ready, performant systems.

---

