# Python Developer Knowledge Base
# Module 11 — System Design
# Part 1 — System Design Fundamentals

---

# Module Overview

This module covers the principles of designing scalable software systems.

Topics include

- System Design Fundamentals
- Scalability
- Load Balancing
- Caching
- Databases
- API Design
- Microservices
- Distributed Systems
- Message Queues
- CAP Theorem
- Security
- Reliability
- Monitoring
- Real-world Architectures

---

# What is System Design?

System design is the process of defining the architecture, components, interfaces, and data flow of a software system.

It answers questions like:

- How will the application scale?
- How will data be stored?
- How will services communicate?
- How will failures be handled?
- How can performance be improved?

---

# Goals of Good System Design

A good system should be

✓ Scalable

✓ Reliable

✓ Available

✓ Maintainable

✓ Secure

✓ Fault Tolerant

✓ Performant

✓ Cost Efficient

---

# Functional Requirements

Functional requirements describe **what the system should do**.

Examples

- User login
- Upload files
- Search products
- Process payments
- Generate reports

---

# Non-Functional Requirements

Non-functional requirements describe **how the system should perform**.

Examples

- Support 1 million users
- Response time under 200 ms
- 99.99% uptime
- High security
- Fault tolerance
- Scalability

---

# Example

Instagram

Functional

- Upload image
- Like post
- Comment
- Follow users

Non-functional

- Millions of users
- Low latency
- High availability
- Durable storage

---

# Basic Architecture

```
Users

↓

Frontend

↓

Backend API

↓

Database
```

This is the simplest web application architecture.

---

# Three-Tier Architecture

```
Presentation Layer

↓

Business Logic Layer

↓

Data Layer
```

### Presentation Layer

- UI
- Mobile App
- Web Browser

### Business Layer

- FastAPI
- Flask
- Django

### Data Layer

- PostgreSQL
- MySQL
- MongoDB

---

# Request Lifecycle

```
Browser

↓

API

↓

Business Logic

↓

Database

↓

API

↓

Browser
```

---

# Components of a Backend System

Typical backend includes

- API Server
- Database
- Cache
- Authentication
- Logging
- Monitoring
- Message Queue
- Storage

---

# Client-Server Architecture

```
Client

↓

Network

↓

Server
```

Client examples

- Browser
- Mobile App
- Desktop App

Server responsibilities

- Process requests
- Execute business logic
- Return responses

---

# Stateless Systems

Each request is independent.

```
Request 1

↓

Server

↓

Response

Request 2

↓

Server

↓

Response
```

Advantages

✓ Easy scaling

✓ Load balancing

✓ Simpler deployments

---

# Stateful Systems

Server stores session information.

```
Client

↓

Server

↓

Session Stored
```

Disadvantages

- Harder scaling
- Sticky sessions
- Complex failover

Modern APIs generally prefer stateless designs.

---

# Horizontal Scaling

Increase the number of servers.

```
Server

↓

2 Servers

↓

10 Servers
```

Benefits

- Better availability
- Higher capacity
- Fault tolerance

---

# Vertical Scaling

Increase server resources.

```
2 CPU

↓

8 CPU

↓

32 GB RAM
```

Limitations

- Hardware limits
- More expensive
- Single point of failure

---

# Scalability

Scalability is the ability to handle increasing load efficiently.

Two approaches

- Vertical Scaling
- Horizontal Scaling

Most modern distributed systems favor horizontal scaling.

---

# Throughput

Throughput measures the amount of work completed per unit time.

Examples

- Requests per second
- Transactions per minute
- Messages per second

Higher throughput generally indicates better capacity.

---

# Latency

Latency is the time required to complete a request.

Example

```
Client

↓

150 ms

↓

Server

↓

Response
```

Lower latency improves user experience.

---

# Bandwidth

Bandwidth is the maximum amount of data that can be transferred.

Example

```
100 Mbps

↓

Network Capacity
```

High bandwidth does not necessarily mean low latency.

---

# Availability

Availability measures how often the system is operational.

Common targets

99%

99.9%

99.99%

99.999%

---

# Availability Table

| Availability | Approximate Downtime per Year |
|-------------|-------------------------------|
| 99% | ~3.65 days |
| 99.9% | ~8.8 hours |
| 99.99% | ~52.6 minutes |
| 99.999% | ~5.3 minutes |

---

# Reliability

Reliability means the system consistently performs correctly over time.

Examples

- Correct data
- Successful transactions
- Consistent responses

---

# Fault Tolerance

The ability to continue operating despite failures.

Example

```
Server A

↓

Fails

↓

Server B Continues
```

---

# Redundancy

Duplicate critical components.

Examples

- Multiple servers
- Database replicas
- Backup storage

Redundancy improves availability.

---

# Single Point of Failure (SPOF)

A component whose failure stops the entire system.

Example

```
Users

↓

One Database

↓

Failure

↓

Application Down
```

Design systems to eliminate SPOFs.

---

# High Availability

Achieved through

- Multiple servers
- Load balancing
- Replication
- Health checks
- Automatic failover

---

# Disaster Recovery

Prepare for major failures.

Examples

- Data backups
- Cross-region replication
- Recovery procedures
- Failover plans

---

# Maintainability

A maintainable system is

- Easy to understand
- Easy to modify
- Easy to deploy
- Easy to debug

---

# Observability

Understand system behavior using

- Logs
- Metrics
- Traces

Observability helps detect and diagnose issues.

---

# Trade-offs

Improving one aspect often impacts another.

Examples

- Performance vs Cost
- Consistency vs Availability
- Simplicity vs Flexibility

System design is about making informed trade-offs.

---

# Best Practices

✓ Gather requirements first.

✓ Separate functional and non-functional requirements.

✓ Design for scalability.

✓ Eliminate single points of failure.

✓ Prefer stateless services.

✓ Monitor system health.

✓ Plan for failures.

---

# Common Mistakes

❌ Ignoring non-functional requirements.

❌ Optimizing too early.

❌ Designing without scalability in mind.

❌ Creating unnecessary complexity.

❌ Assuming hardware never fails.

---

# Interview Questions

### Easy

1. What is system design?
2. Difference between functional and non-functional requirements.
3. What is scalability?
4. What is latency?
5. What is throughput?

---

### Medium

1. Compare vertical and horizontal scaling.
2. Explain stateless vs stateful systems.
3. What is high availability?
4. What is fault tolerance?
5. What is a single point of failure?

---

### Hard

1. Design a highly available backend architecture.
2. Explain trade-offs between scalability and consistency.
3. Build a resilient architecture for a payment system.
4. How would you remove single points of failure?
5. Design a system capable of serving millions of users.

---

# Coding / Design Exercises

Easy

- Draw a three-tier architecture.
- Identify functional and non-functional requirements for a blog application.

Medium

- Design a scalable REST API architecture.
- Compare vertical and horizontal scaling for an e-commerce application.

Hard

- Design the architecture for a social media platform.
- Design a highly available backend for an online banking application.

---

# Module Summary

System design focuses on creating software architectures that meet both functional and non-functional requirements. Core principles include scalability, availability, reliability, fault tolerance, maintainability, and observability. Understanding these concepts provides the foundation for designing distributed systems that can serve large numbers of users while remaining resilient, efficient, and easy to operate.

---

# Python Developer Knowledge Base
# Module 11 — System Design
# Part 2 — Scalability, Load Balancers & High Availability

---

# What is Scalability?

Scalability is the ability of a system to handle increasing workload without significantly degrading performance.

Examples of increased workload

- More users
- More requests
- More data
- More background jobs
- Higher network traffic

Goal

```
More Load

↓

Maintain Performance
```

---

# Why Systems Need to Scale

Example

```
100 Users

↓

1,000 Users

↓

100,000 Users

↓

10 Million Users
```

A system designed for 100 users may fail under millions of users without scalability.

---

# Types of Scaling

There are two primary scaling strategies.

- Vertical Scaling
- Horizontal Scaling

---

# Vertical Scaling (Scale Up)

Increase the resources of a single server.

```
Server

↓

2 CPU

↓

8 CPU

↓

32 GB RAM
```

Advantages

✓ Simple

✓ No application changes

✓ Easier database management

Disadvantages

✗ Hardware limits

✗ Expensive

✗ Single point of failure

---

# Horizontal Scaling (Scale Out)

Increase the number of servers.

```
Server

↓

2 Servers

↓

4 Servers

↓

16 Servers
```

Advantages

✓ Better fault tolerance

✓ High availability

✓ Supports massive workloads

✓ Easier incremental scaling

Disadvantages

✗ More operational complexity

✗ Requires distributed system design

Modern cloud applications primarily use horizontal scaling.

---

# Comparing Vertical and Horizontal Scaling

| Feature | Vertical | Horizontal |
|---------|----------|------------|
| Cost | Higher for large upgrades | Incremental |
| Availability | Lower | Higher |
| Complexity | Lower | Higher |
| Scalability Limit | Hardware limit | Practically unlimited |
| Fault Tolerance | Poor | Excellent |

---

# Stateless Applications

Stateless services are easier to scale.

```
Request

↓

Any Server

↓

Response
```

Since no session data is stored locally, requests can be routed to any instance.

---

# Stateful Applications

Stateful services maintain client session information.

```
Client

↓

Server

↓

Session Stored
```

Challenges

- Sticky sessions
- Harder failover
- More difficult horizontal scaling

---

# Load Balancer

A load balancer distributes incoming requests across multiple servers.

```
Users

↓

Load Balancer

↓

Server A

Server B

Server C
```

Benefits

✓ Better performance

✓ High availability

✓ Fault tolerance

✓ Scalability

---

# Types of Load Balancers

### Layer 4 (Transport Layer)

Routes traffic based on

- IP Address
- TCP Port

Fast and efficient.

---

### Layer 7 (Application Layer)

Routes traffic based on

- URL
- HTTP Headers
- Cookies
- Hostname

Supports intelligent request routing.

---

# Load Balancing Algorithms

Common algorithms

- Round Robin
- Least Connections
- Least Response Time
- Weighted Round Robin
- IP Hash

---

# Round Robin

Requests are distributed equally.

```
Request 1 → Server A

Request 2 → Server B

Request 3 → Server C

Request 4 → Server A
```

Simple and commonly used.

---

# Least Connections

Routes requests to the server with the fewest active connections.

Useful when request durations vary significantly.

---

# Weighted Round Robin

Assigns different capacities to servers.

Example

```
Server A Weight = 3

Server B Weight = 1
```

Server A receives more traffic.

---

# IP Hash

The client's IP determines the destination server.

Useful for maintaining session affinity.

---

# Health Checks

The load balancer continuously checks server health.

```
Server A

Healthy

✓ Receives Traffic

Server B

Unhealthy

✗ Removed from Rotation
```

---

# Failover

If one server fails

```
Users

↓

Load Balancer

↓

Server A (Failed)

↓

Traffic → Server B
```

The system continues operating without user intervention.

---

# Auto Scaling

Automatically adjusts the number of servers based on demand.

Example

```
10% CPU

↓

2 Servers

80% CPU

↓

6 Servers
```

Cloud providers support automatic scaling policies.

---

# Reverse Proxy

A reverse proxy sits between clients and backend servers.

```
Client

↓

Reverse Proxy

↓

Application Servers
```

Common reverse proxies

- Nginx
- HAProxy
- Traefik
- Envoy

---

# Reverse Proxy Responsibilities

- SSL termination
- Compression
- Caching
- Request routing
- Load balancing
- Security

---

# Forward Proxy vs Reverse Proxy

| Forward Proxy | Reverse Proxy |
|---------------|---------------|
| Represents clients | Represents servers |
| Used by users | Used by backend infrastructure |
| Controls outgoing traffic | Controls incoming traffic |

---

# Content Delivery Network (CDN)

A CDN caches static content closer to users.

```
User

↓

Nearest CDN Node

↓

Static Content
```

Examples

- Images
- CSS
- JavaScript
- Videos

---

# CDN Benefits

✓ Lower latency

✓ Reduced server load

✓ Faster downloads

✓ Global availability

---

# Cache Hierarchy

```
Browser Cache

↓

CDN

↓

Reverse Proxy Cache

↓

Application Cache

↓

Database
```

Each cache layer reduces load on the next layer.

---

# Session Management

Approaches

- Stateless JWT
- Redis session store
- Sticky sessions

Modern REST APIs often favor stateless authentication.

---

# Sticky Sessions

The same client is always routed to the same server.

```
Client

↓

Server B

↓

Future Requests

↓

Server B
```

Useful for legacy stateful systems but reduces flexibility.

---

# High Availability (HA)

A highly available system minimizes downtime.

Typical architecture

```
Users

↓

Load Balancer

↓

Multiple Application Servers

↓

Database Cluster
```

---

# Redundancy

Duplicate critical components.

Examples

- Multiple load balancers
- Multiple application servers
- Database replicas
- Redundant storage

---

# Single Point of Failure

Bad design

```
Users

↓

One Load Balancer

↓

One Database
```

Failure stops the system.

Good design eliminates single points of failure.

---

# Availability Zones

Cloud providers divide regions into isolated zones.

```
Region

↓

Zone A

Zone B

Zone C
```

Deploying across zones improves resilience.

---

# Multi-Region Deployment

```
Region A

↓

Load Balancer

↓

Region B
```

Benefits

- Disaster recovery
- Lower latency
- Geographic redundancy

---

# Traffic Routing

Traffic may be routed based on

- Geography
- Latency
- Health
- Capacity

---

# Scaling Databases

Strategies

- Read replicas
- Sharding
- Partitioning
- Caching

Database scaling is often more challenging than application scaling.

---

# Best Practices

✓ Design stateless services.

✓ Use load balancers.

✓ Enable health checks.

✓ Implement auto scaling.

✓ Deploy across multiple availability zones.

✓ Cache static assets with a CDN.

✓ Remove single points of failure.

---

# Common Mistakes

❌ Relying on one application server.

❌ Ignoring health checks.

❌ Using sticky sessions unnecessarily.

❌ Forgetting redundancy.

❌ Scaling the application while ignoring database bottlenecks.

---

# Real-World Example

Large-scale web application

```
Users

↓

Global CDN

↓

Global Load Balancer

↓

Regional Load Balancer

↓

Application Servers

↓

Redis Cache

↓

Database Cluster

↓

Object Storage
```

---

# Interview Questions

### Easy

1. What is horizontal scaling?
2. What is a load balancer?
3. What is a reverse proxy?
4. What is a CDN?
5. Why are health checks important?

---

### Medium

1. Compare Layer 4 and Layer 7 load balancers.
2. Explain Round Robin and Least Connections.
3. Why are stateless applications easier to scale?
4. What are sticky sessions?
5. How does auto scaling work?

---

### Hard

1. Design a load balancing strategy for a global application.
2. Explain how Netflix handles scalability.
3. Design a highly available architecture for an online banking platform.
4. Compare CDN caching with application caching.
5. Explain how to eliminate single points of failure in a distributed system.

---

# Design Exercises

Easy

- Draw a load-balanced architecture.
- Compare vertical and horizontal scaling.

Medium

- Design a scalable REST API serving one million users.
- Build a high-availability deployment using multiple application servers.

Hard

- Design a globally distributed social media platform.
- Create a disaster-resistant architecture spanning multiple cloud regions.

---

# Module Summary

Scalability enables systems to handle increasing workloads efficiently through vertical or horizontal scaling. Load balancers distribute requests across multiple servers, reverse proxies provide routing and security, and CDNs reduce latency by caching content near users. High availability is achieved through redundancy, health checks, auto scaling, and multi-zone deployments, ensuring reliable and resilient systems capable of serving millions of users.

---

# Python Developer Knowledge Base
# Module 11 — System Design
# Part 3 — Caching, Databases & Storage Systems

---

# Why Caching?

Accessing a database is significantly slower than accessing data from memory.

Without cache

```
User

↓

Application

↓

Database

↓

Response
```

With cache

```
User

↓

Application

↓

Cache

↓

Response
```

If the data is not in cache (cache miss), the application retrieves it from the database and stores it in the cache for future requests.

---

# Benefits of Caching

✓ Faster response times

✓ Reduced database load

✓ Improved scalability

✓ Lower infrastructure costs

✓ Better user experience

---

# Cache Hit and Cache Miss

### Cache Hit

```
User

↓

Cache

↓

Data Found

↓

Response
```

Fastest path.

---

### Cache Miss

```
User

↓

Cache

↓

Data Not Found

↓

Database

↓

Cache Updated

↓

Response
```

---

# Cache Eviction Policies

When cache is full, items must be removed.

Common policies

- LRU (Least Recently Used)
- LFU (Least Frequently Used)
- FIFO (First In, First Out)
- TTL (Time-To-Live)

---

# Time-To-Live (TTL)

Cached data expires after a specified duration.

Example

```
Product Cache

TTL = 10 minutes
```

After expiration, the next request fetches fresh data from the database.

---

# Caching Strategies

Common patterns

- Cache-Aside (Lazy Loading)
- Write-Through
- Write-Back (Write-Behind)
- Write-Around

---

# Cache-Aside

Most commonly used pattern.

Workflow

```
Read Request

↓

Check Cache

↓

Hit → Return Data

↓

Miss

↓

Read Database

↓

Update Cache

↓

Return Data
```

Advantages

✓ Simple

✓ Efficient

Disadvantages

- First request is slower.

---

# Write-Through Cache

```
Application

↓

Cache

↓

Database
```

Data is written to the cache and database simultaneously.

Advantages

✓ Cache always contains fresh data.

Disadvantages

- Higher write latency.

---

# Write-Back (Write-Behind)

```
Application

↓

Cache

↓

Response

↓

Background Write

↓

Database
```

Advantages

✓ Very fast writes.

Disadvantages

- Risk of data loss if cache fails before persistence.

---

# Write-Around

```
Application

↓

Database

↓

(No Cache Update)
```

Cache is only populated on future reads.

Useful for write-heavy workloads where recently written data is unlikely to be read immediately.

---

# Redis

Redis is an in-memory data store commonly used for

- Caching
- Session storage
- Pub/Sub
- Rate limiting
- Distributed locks
- Queues

Advantages

✓ Extremely fast

✓ Rich data structures

✓ Persistence options

---

# Redis Data Structures

- String
- Hash
- List
- Set
- Sorted Set (ZSET)
- Stream
- Bitmap
- HyperLogLog

---

# Memcached

Another in-memory cache.

Characteristics

- Simple key-value store
- Very fast
- No persistence
- Fewer data structures than Redis

---

# Redis vs Memcached

| Feature | Redis | Memcached |
|---------|-------|-----------|
| Persistence | Yes (optional) | No |
| Data Structures | Many | Key-Value only |
| Replication | Yes | Limited |
| Pub/Sub | Yes | No |
| Transactions | Yes | No |

Redis is generally preferred for modern applications due to its flexibility.

---

# SQL Databases

Relational databases organize data into tables with predefined schemas.

Examples

- PostgreSQL
- MySQL
- MariaDB
- SQLite
- Oracle Database
- Microsoft SQL Server

Advantages

✓ ACID transactions

✓ Strong consistency

✓ Complex joins

✓ Mature ecosystem

---

# NoSQL Databases

Designed for flexibility and scalability.

Categories

- Document
- Key-Value
- Column-Family
- Graph

Examples

- MongoDB
- Cassandra
- DynamoDB
- Redis
- Neo4j

---

# SQL vs NoSQL

| SQL | NoSQL |
|------|--------|
| Structured schema | Flexible schema |
| ACID transactions | Varies by database |
| Complex joins | Limited joins |
| Strong consistency (often) | Often optimized for scalability |
| Vertical + Horizontal scaling | Primarily horizontal scaling |

---

# Choosing SQL or NoSQL

Choose SQL when

- Transactions are critical.
- Data relationships are complex.
- Strong consistency is required.

Choose NoSQL when

- Schema changes frequently.
- Massive horizontal scaling is required.
- Data is semi-structured or unstructured.

---

# Database Index

An index speeds up data retrieval.

Without index

```
Table Scan

↓

Every Row Checked
```

With index

```
Index

↓

Matching Row
```

Indexes improve read performance but increase storage usage and write overhead.

---

# Types of Indexes

- Primary Index
- Secondary Index
- Composite Index
- Unique Index
- Full-Text Index

---

# Composite Index

Index on multiple columns.

Example

```
(first_name, last_name)
```

Can optimize queries filtering on those columns in the indexed order.

---

# Query Optimization

Good practices

✓ Select only required columns.

✓ Avoid unnecessary `SELECT *`.

✓ Use indexes appropriately.

✓ Analyze slow queries.

✓ Optimize joins.

---

# Replication

Copies data from a primary database to replicas.

```
Primary

↓

Replica 1

↓

Replica 2
```

Benefits

✓ Improved read scalability

✓ Backup options

✓ Higher availability

---

# Read Replica

Writes

```
Primary
```

Reads

```
Replica
```

Common architecture

```
Application

↓

Primary (Writes)

↓

Replicas (Reads)
```

---

# Sharding

Split data across multiple database servers.

```
Users A–M

↓

Shard 1

Users N–Z

↓

Shard 2
```

Benefits

✓ Massive horizontal scaling

Challenges

- Cross-shard queries
- Rebalancing
- Operational complexity

---

# Partitioning

Split a table into smaller partitions within the same database.

Examples

- By date
- By region
- By customer ID

Improves maintenance and some query performance.

---

# Database Connection Pool

Opening a new database connection for every request is expensive.

Connection pooling reuses existing connections.

```
Application

↓

Connection Pool

↓

Database
```

Benefits

✓ Lower latency

✓ Better throughput

✓ Reduced database overhead

---

# Object Storage

Stores large binary objects.

Examples

- Images
- Videos
- PDFs
- Backups

Cloud services

- Amazon S3
- Azure Blob Storage
- Google Cloud Storage

Applications usually store metadata in the database and the actual files in object storage.

---

# Blob Storage Pattern

```
User Upload

↓

Object Storage

↓

File URL

↓

Database Metadata
```

---

# Data Archiving

Older, infrequently accessed data can be moved to archival storage.

Benefits

✓ Lower storage cost

✓ Better performance for active datasets

---

# Database Backup

Regular backups are essential.

Backup types

- Full
- Incremental
- Differential

Always test restore procedures.

---

# Database Optimization Checklist

✓ Add indexes carefully.

✓ Monitor slow queries.

✓ Use connection pooling.

✓ Cache frequently accessed data.

✓ Archive historical data.

✓ Replicate for read scalability.

✓ Shard only when necessary.

---

# Best Practices

✓ Use Redis for frequently accessed data.

✓ Keep cache TTL appropriate.

✓ Avoid unnecessary indexes.

✓ Normalize data where appropriate.

✓ Denormalize selectively for performance.

✓ Monitor database metrics.

✓ Plan for growth.

---

# Common Mistakes

❌ Caching everything.

❌ Forgetting cache invalidation.

❌ Over-indexing tables.

❌ Using NoSQL without understanding trade-offs.

❌ Storing large files directly in relational databases.

❌ Ignoring slow query logs.

---

# Interview Questions

### Easy

1. What is caching?
2. What is Redis?
3. Difference between SQL and NoSQL.
4. What is a database index?
5. What is a cache hit?

---

### Medium

1. Compare Cache-Aside and Write-Through caching.
2. Explain replication and read replicas.
3. Compare Redis and Memcached.
4. Why does indexing improve performance?
5. Explain sharding vs partitioning.

---

### Hard

1. Design the caching strategy for an e-commerce platform.
2. Design a database architecture for a social media application.
3. Explain how to scale a relational database to millions of users.
4. Compare SQL and NoSQL for an online messaging application.
5. Design a storage strategy for user-uploaded media.

---

# Design Exercises

Easy

- Draw a cache-aside workflow.
- Design a simple database schema for a blog.

Medium

- Add Redis caching to a REST API.
- Design a read-replica architecture for a reporting system.

Hard

- Design the data layer for a global e-commerce platform.
- Build a scalable storage architecture for billions of images and videos.

---

# Module Summary

Caching significantly improves application performance by reducing database access, with Redis being the most widely used in-memory data store. Relational databases provide strong consistency and transactional guarantees, while NoSQL databases prioritize flexibility and horizontal scalability. Techniques such as indexing, replication, sharding, partitioning, and connection pooling help databases handle increasing workloads efficiently. Object storage complements databases by storing large files separately, creating scalable and cost-effective storage architectures.

---

# Python Developer Knowledge Base
# Module 11 — System Design
# Part 4 — Distributed Systems, CAP Theorem & Event-Driven Architecture

---

# What is a Distributed System?

A distributed system is a collection of independent computers that work together as a single system.

```
Server A

↓

Server B

↓

Server C

↓

One Application
```

Users should not notice that multiple servers are involved.

---

# Why Distributed Systems?

A single server has limitations.

- CPU
- Memory
- Storage
- Network
- Availability

Instead of buying one extremely powerful machine, modern applications distribute work across many machines.

Benefits

✓ Scalability

✓ High Availability

✓ Fault Tolerance

✓ Geographic Distribution

✓ Better Performance

---

# Characteristics of Distributed Systems

- Multiple independent nodes
- Network communication
- Shared goals
- Fault tolerance
- Concurrent processing

---

# Challenges

Distributed systems introduce complexity.

Common challenges

- Network failures
- Partial failures
- Data consistency
- Clock synchronization
- Duplicate requests
- Message ordering
- Distributed transactions

---

# Network Failures

Unlike local function calls, network communication can fail.

Possible issues

```
Timeout

Packet Loss

High Latency

Connection Failure
```

Applications must expect failures.

---

# Partial Failure

Example

```
Server A ✓

Server B ✗

Server C ✓
```

The overall system should continue functioning despite one node failing.

---

# Distributed Communication

Communication styles

- Synchronous
- Asynchronous

---

# Synchronous Communication

```
Client

↓

Service A

↓

Service B

↓

Wait

↓

Response
```

Advantages

✓ Simple

✓ Immediate response

Disadvantages

- Higher latency
- Tight coupling
- Cascading failures

---

# Asynchronous Communication

```
Producer

↓

Queue

↓

Consumer

↓

Response Later
```

Advantages

✓ Decoupling

✓ Better scalability

✓ Fault tolerance

Disadvantages

- More complexity
- Eventual consistency

---

# CAP Theorem

CAP states that a distributed system cannot simultaneously guarantee

```
Consistency

Availability

Partition Tolerance
```

During a network partition, a system can fully satisfy at most **Consistency** or **Availability**, but not both.

---

# Consistency (C)

Every client sees the same data immediately after an update.

Example

```
Update Balance

↓

Every Server

↓

Same Value
```

---

# Availability (A)

Every request receives a response.

The response may not always contain the latest data.

---

# Partition Tolerance (P)

The system continues operating despite network failures between nodes.

Modern distributed systems generally assume partitions can occur.

---

# CAP Trade-offs

### CP Systems

Prioritize

- Consistency
- Partition Tolerance

May reject requests during partitions.

Examples

- ZooKeeper
- etcd

---

### AP Systems

Prioritize

- Availability
- Partition Tolerance

Clients may temporarily observe stale data.

Examples

- Cassandra
- DynamoDB (configurable behavior)

---

### CA Systems

Consistency + Availability

Possible only when partitions are not a concern, such as on a single machine or tightly coupled environment.

---

# Consistency Models

Different systems offer different consistency guarantees.

Common models

- Strong Consistency
- Eventual Consistency
- Causal Consistency
- Read-Your-Writes Consistency

---

# Strong Consistency

Every read immediately reflects the latest successful write.

```
Write

↓

Read

↓

Latest Value
```

---

# Eventual Consistency

Updates propagate over time.

```
Write

↓

Node A Updated

↓

Node B Updated Later

↓

Eventually Same Data
```

Common in globally distributed systems.

---

# Read-Your-Writes

A user immediately sees their own updates.

Useful for profile edits, settings, and similar user-facing features.

---

# Distributed Transactions

Transactions spanning multiple services or databases.

Traditional ACID transactions become difficult across distributed systems.

---

# Two-Phase Commit (2PC)

Coordinator

↓

Prepare Phase

↓

Commit Phase

Advantages

- Strong consistency

Disadvantages

- Blocking
- Slow
- Coordinator dependency

---

# Saga Pattern

Large transaction

↓

Broken into

↓

Small Local Transactions

↓

Compensating Actions if Failure

Suitable for microservices.

---

# Message Queue

A message queue enables asynchronous communication.

```
Producer

↓

Queue

↓

Consumer
```

Benefits

✓ Loose coupling

✓ Scalability

✓ Retry support

✓ Load leveling

---

# Common Message Brokers

- RabbitMQ
- Apache Kafka
- Amazon SQS
- Google Pub/Sub
- Azure Service Bus

---

# RabbitMQ

Message broker implementing AMQP.

Best for

- Task queues
- Background jobs
- Request/response messaging

Features

- Acknowledgements
- Routing
- Dead-letter queues
- Priorities

---

# Kafka

Distributed event streaming platform.

Designed for

- Massive throughput
- Event streaming
- Log aggregation
- Real-time analytics

Characteristics

- Persistent logs
- Partitioned topics
- Consumer groups

---

# RabbitMQ vs Kafka

| RabbitMQ | Kafka |
|----------|-------|
| Queue-based | Log-based |
| Lower throughput | Extremely high throughput |
| Complex routing | High-volume event streaming |
| Task processing | Streaming pipelines |

---

# Publish–Subscribe (Pub/Sub)

One publisher sends events to multiple subscribers.

```
Publisher

↓

Topic

↓

Subscriber A

↓

Subscriber B

↓

Subscriber C
```

Useful for notifications and event broadcasting.

---

# Event-Driven Architecture

Components communicate through events instead of direct API calls.

```
Order Created

↓

Event Bus

↓

Inventory Service

↓

Notification Service

↓

Billing Service
```

Advantages

✓ Loose coupling

✓ Independent scaling

✓ Easier integration

---

# Event

An event describes something that has already happened.

Examples

- UserRegistered
- PaymentCompleted
- OrderShipped
- PasswordChanged

Events are immutable.

---

# Event Bus

Routes events to interested consumers.

```
Producer

↓

Event Bus

↓

Multiple Consumers
```

---

# Dead Letter Queue (DLQ)

Messages that cannot be processed are moved to a separate queue.

```
Queue

↓

Processing Failed

↓

Dead Letter Queue
```

Prevents endless retries.

---

# Idempotency

Processing the same request multiple times should produce the same final result.

Example

```
Payment Request

↓

Retry

↓

Only One Payment Recorded
```

Critical for distributed systems.

---

# Retry Strategy

Instead of failing immediately

```
Attempt

↓

Retry

↓

Retry

↓

Dead Letter Queue
```

Commonly combined with exponential backoff.

---

# Exponential Backoff

Retry intervals increase after each failure.

Example

```
1 second

↓

2 seconds

↓

4 seconds

↓

8 seconds
```

Reduces pressure on failing services.

---

# CQRS (Command Query Responsibility Segregation)

Separate write operations from read operations.

```
Command API

↓

Database

↓

Read Model

↓

Query API
```

Benefits

- Independent optimization
- Better scalability

---

# Event Sourcing

Store every state change as an event.

Instead of

```
Current Balance = 1000
```

Store

```
Deposit +500

Withdraw -200

Deposit +700
```

Current state is reconstructed from events.

Benefits

- Complete audit trail
- Time travel
- Replay capability

Challenges

- Increased complexity
- Event versioning

---

# Distributed Cache

Applications often share a centralized cache.

```
Application A

↓

Redis Cluster

↓

Application B
```

Provides consistent cached data across instances.

---

# Circuit Breaker Pattern

Prevent repeated requests to failing services.

```
Service Failure

↓

Circuit Opens

↓

Requests Blocked Temporarily
```

Protects downstream services from overload.

---

# Bulkhead Pattern

Isolate resources so one failing component does not affect others.

Example

```
API Workers

Background Workers

Database Workers
```

Separate pools improve resilience.

---

# Best Practices

✓ Prefer asynchronous communication when appropriate.

✓ Make operations idempotent.

✓ Use retries with exponential backoff.

✓ Monitor queues.

✓ Design for eventual consistency where acceptable.

✓ Keep services loosely coupled.

✓ Plan for partial failures.

---

# Common Mistakes

❌ Assuming the network is always reliable.

❌ Ignoring duplicate messages.

❌ Building distributed transactions everywhere.

❌ Tight service coupling.

❌ Infinite retry loops.

❌ No dead-letter queue.

---

# Interview Questions

### Easy

1. What is a distributed system?
2. Explain CAP theorem.
3. What is eventual consistency?
4. What is a message queue?
5. Difference between RabbitMQ and Kafka.

---

### Medium

1. Compare synchronous and asynchronous communication.
2. Explain the Saga pattern.
3. What is a dead-letter queue?
4. Why is idempotency important?
5. Explain Pub/Sub architecture.

---

### Hard

1. Design an event-driven e-commerce platform.
2. Compare Kafka and RabbitMQ for different workloads.
3. Design a distributed payment system.
4. Explain CQRS and Event Sourcing.
5. Design a resilient microservices architecture capable of handling millions of events per second.

---

# Design Exercises

Easy

- Draw a Pub/Sub architecture.
- Compare synchronous and asynchronous messaging.

Medium

- Design an order processing pipeline using RabbitMQ.
- Implement retry logic with exponential backoff.

Hard

- Design an event-driven ride-sharing backend.
- Build a globally distributed messaging platform using Kafka.

---

# Module Summary

Distributed systems enable applications to scale beyond a single machine by distributing work across multiple nodes. Because network failures are inevitable, these systems must balance consistency, availability, and partition tolerance, as described by the CAP theorem. Message brokers such as RabbitMQ and Kafka support asynchronous communication, while architectural patterns like Saga, CQRS, Event Sourcing, Circuit Breakers, and Dead Letter Queues improve scalability, resilience, and fault tolerance in modern distributed applications.

---

# Python Developer Knowledge Base
# Module 11 — System Design
# Part 5 (Final) — API Design, Microservices & System Design Case Studies

---

# API Design

An API (Application Programming Interface) defines how different systems communicate.

Good APIs should be

✓ Simple

✓ Consistent

✓ Versioned

✓ Secure

✓ Well documented

✓ Backward compatible

---

# REST

REST (Representational State Transfer) is the most common architectural style for web APIs.

Characteristics

- Resource-based
- Stateless
- Uses HTTP methods
- Cacheable

Example

```
GET    /users

POST   /users

GET    /users/101

PUT    /users/101

DELETE /users/101
```

---

# HTTP Methods

| Method | Purpose |
|---------|---------|
| GET | Read data |
| POST | Create resource |
| PUT | Replace resource |
| PATCH | Partial update |
| DELETE | Remove resource |

---

# REST Best Practices

✓ Use nouns instead of verbs.

✓ Use proper HTTP status codes.

✓ Keep APIs stateless.

✓ Return meaningful error messages.

✓ Support pagination.

✓ Validate inputs.

---

# API Versioning

Example

```
/api/v1/users

/api/v2/users
```

Versioning prevents breaking existing clients.

---

# Pagination

Avoid returning millions of records.

Example

```
GET /products?page=2&limit=20
```

Alternative

Cursor pagination

```
GET /posts?cursor=abc123
```

Cursor pagination scales better for large datasets.

---

# Filtering & Sorting

Filtering

```
GET /products?category=laptop
```

Sorting

```
GET /products?sort=price
```

Search

```
GET /products?q=python
```

---

# HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 429 | Too Many Requests |
| 500 | Internal Server Error |

---

# GraphQL

GraphQL allows clients to request only the data they need.

Example

```
Client

↓

GraphQL Server

↓

Database
```

Advantages

✓ Flexible queries

✓ Reduces over-fetching

✓ Single endpoint

Disadvantages

- More complex caching
- More complex server implementation

---

# gRPC

High-performance RPC framework.

Uses

- Protocol Buffers
- HTTP/2
- Binary serialization

Best suited for

- Internal microservice communication
- Low-latency systems

---

# REST vs GraphQL vs gRPC

| REST | GraphQL | gRPC |
|------|----------|------|
| HTTP/JSON | Flexible queries | Binary protocol |
| Simple | Complex | Very fast |
| Public APIs | Frontend-heavy apps | Service-to-service |

---

# Authentication

Authentication answers

```
Who are you?
```

Examples

- Username/password
- OAuth
- JWT
- API Key
- Multi-factor Authentication

---

# Authorization

Authorization answers

```
What are you allowed to do?
```

Example

```
Admin

↓

Delete User

Regular User

↓

Denied
```

---

# JWT (JSON Web Token)

Typical flow

```
Login

↓

JWT Issued

↓

Client Stores Token

↓

Token Sent

↓

API Validates
```

Advantages

✓ Stateless

✓ Scalable

✓ Widely supported

---

# OAuth2

Delegated authorization.

Example

```
Login with Google

↓

OAuth Provider

↓

Application
```

Useful for third-party identity providers.

---

# Rate Limiting

Protect APIs from abuse.

Example

```
100 Requests

↓

1 Minute

↓

429 Too Many Requests
```

Algorithms

- Token Bucket
- Leaky Bucket
- Fixed Window
- Sliding Window

---

# API Gateway

An API Gateway sits in front of backend services.

Responsibilities

- Authentication
- Routing
- Rate limiting
- Logging
- SSL termination
- Request aggregation

Architecture

```
Client

↓

API Gateway

↓

Microservices
```

---

# Monolith

Single deployable application.

```
Application

↓

Database
```

Advantages

✓ Simpler development

✓ Easier debugging

Disadvantages

- Harder scaling
- Large codebase
- Slower deployments

---

# Microservices

Application split into independent services.

```
User Service

Order Service

Payment Service

Inventory Service
```

Each service owns its business capability.

---

# Advantages of Microservices

✓ Independent deployment

✓ Independent scaling

✓ Technology flexibility

✓ Better fault isolation

---

# Challenges of Microservices

- Network communication
- Distributed transactions
- Monitoring
- Service discovery
- Operational complexity

---

# Service Discovery

Services locate each other dynamically.

```
Service Registry

↓

User Service

↓

Payment Service
```

Examples

- Consul
- Eureka
- Kubernetes DNS

---

# Observability

Three pillars

```
Logs

↓

Metrics

↓

Traces
```

---

# Logging

Record application events.

Examples

- Errors
- Warnings
- Requests
- Audit events

---

# Metrics

Measure application performance.

Examples

- CPU usage
- Memory
- Latency
- Request rate
- Error rate

---

# Distributed Tracing

Track requests across services.

```
Gateway

↓

User Service

↓

Payment Service

↓

Database
```

Helps identify bottlenecks.

---

# Case Study 1 — URL Shortener

Requirements

- Short URLs
- Redirect quickly
- Billions of links

Architecture

```
Client

↓

Load Balancer

↓

API

↓

Cache (Redis)

↓

Database
```

Key considerations

- Unique ID generation
- Caching
- High read throughput

---

# Case Study 2 — Chat Application

Requirements

- Real-time messaging
- Presence
- Notifications

Architecture

```
Client

↓

WebSocket Server

↓

Message Queue

↓

Database
```

Technologies

- WebSockets
- Redis
- Kafka/RabbitMQ

---

# Case Study 3 — Ride-Sharing Platform

Components

- User Service
- Driver Service
- Location Service
- Matching Engine
- Payment Service

Architecture

```
Mobile Apps

↓

API Gateway

↓

Microservices

↓

Redis

↓

Kafka

↓

Databases
```

Challenges

- Real-time location
- Matching latency
- Fault tolerance

---

# Case Study 4 — E-commerce Platform

Components

- Product Catalog
- Search
- Cart
- Orders
- Payments
- Inventory

Architecture

```
Users

↓

CDN

↓

Load Balancer

↓

API Gateway

↓

Microservices

↓

Redis

↓

Databases

↓

Object Storage
```

---

# System Design Interview Framework

1. Clarify requirements.

2. Estimate scale.

3. Design high-level architecture.

4. Define APIs.

5. Design database.

6. Add caching.

7. Add load balancing.

8. Plan scalability.

9. Address failures.

10. Discuss trade-offs.

---

# Capacity Estimation

Estimate

- Daily Active Users
- Requests per second
- Storage growth
- Network bandwidth
- Peak traffic

These estimates guide architectural decisions.

---

# Trade-offs

Examples

| Trade-off | Option A | Option B |
|-----------|----------|----------|
| Consistency vs Availability | Strong consistency | Eventual consistency |
| Simplicity vs Flexibility | Monolith | Microservices |
| Read Speed vs Write Speed | Heavy indexing | Fewer indexes |
| Cost vs Performance | Smaller infrastructure | Larger infrastructure |

There is rarely a universally "correct" design—choices depend on requirements.

---

# Production Architecture Checklist

✓ Stateless services

✓ Load balancers

✓ CDN

✓ Caching

✓ Database replication

✓ Backups

✓ Monitoring

✓ Logging

✓ Tracing

✓ Rate limiting

✓ Authentication

✓ Authorization

✓ Disaster recovery

✓ CI/CD

✓ Automated testing

---

# Best Practices

✓ Start with a simple architecture.

✓ Scale only where necessary.

✓ Cache frequently accessed data.

✓ Monitor everything.

✓ Automate deployments.

✓ Design for failure.

✓ Document APIs.

✓ Keep services loosely coupled.

---

# Common Mistakes

❌ Overengineering early.

❌ Choosing microservices without a clear need.

❌ Ignoring non-functional requirements.

❌ No monitoring or alerting.

❌ Tight coupling between services.

❌ Hardcoding secrets.

---

# Interview Questions

### Easy

1. What is REST?
2. What is JWT?
3. Difference between authentication and authorization.
4. What is an API Gateway?
5. What is a microservice?

---

### Medium

1. Compare REST, GraphQL, and gRPC.
2. Explain rate limiting algorithms.
3. Compare monoliths and microservices.
4. Explain service discovery.
5. Design pagination for a large dataset.

---

### Hard

1. Design a URL shortening service.
2. Design a real-time chat application.
3. Design an e-commerce platform capable of serving millions of users.
4. Design a ride-sharing backend.
5. Explain the trade-offs between monolithic and microservice architectures.

---

# Design Exercises

Easy

- Design a REST API for a blog.
- Add pagination and filtering to a product catalog.

Medium

- Design a scalable authentication service.
- Create a rate-limited public API.

Hard

- Design a globally distributed messaging platform.
- Build a highly available video streaming architecture.
- Design an enterprise-scale payment processing system.

---

# Module Summary

Effective system design combines scalable architecture, efficient APIs, secure authentication, reliable communication, and strong observability. REST, GraphQL, and gRPC each address different communication needs, while microservices enable independent deployment and scaling when justified by system complexity. Real-world architectures rely on caching, load balancing, asynchronous messaging, monitoring, and fault tolerance to deliver reliable services at scale. Successful system design requires balancing technical trade-offs based on functional and non-functional requirements.

---

