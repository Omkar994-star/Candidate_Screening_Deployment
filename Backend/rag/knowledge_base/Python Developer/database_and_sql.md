# Python Developer Knowledge Base
# Module 05 — Database and SQL

---

# Module Overview

Databases are the backbone of modern software applications. Almost every backend application stores, retrieves, and processes data efficiently using a database.

This module covers:

- Database Fundamentals
- Relational Databases
- Database Design
- SQL Basics
- Constraints
- Keys
- Normalization
- Transactions
- ACID Properties
- Introduction to NoSQL
- Python Database Connectivity

---

# 1. What is a Database?

## Definition

A database is an organized collection of structured or unstructured data that enables efficient storage, retrieval, updating, and management.

Examples

- Banking Systems
- E-commerce Websites
- Hospital Management
- Social Media
- Inventory Systems

---

# Why Databases?

Without databases

❌ Data duplication

❌ Slow searching

❌ Poor consistency

❌ Difficult updates

Databases provide

✓ Fast retrieval

✓ Data integrity

✓ Security

✓ Scalability

✓ Concurrent access

---

# Database Management System (DBMS)

A DBMS is software used to create, manage, and interact with databases.

Responsibilities

- Data Storage
- Query Processing
- Security
- Backup
- Recovery
- Concurrency Control

Examples

- PostgreSQL
- MySQL
- SQLite
- Oracle
- Microsoft SQL Server

---

# Database vs DBMS

| Database | DBMS |
|-----------|------|
| Collection of data | Software managing data |
| Stores information | Provides operations on data |
| Passive | Active system |

---

# Types of Databases

## Relational Database (RDBMS)

Stores data in tables.

Example

```
Students

+----+--------+------+

| ID | Name   | Age  |

+----+--------+------+

| 1  | Alice  | 21   |

| 2  | Bob    | 22   |

+----+--------+------+
```

Examples

- PostgreSQL
- MySQL
- SQLite

---

## NoSQL Database

Stores data in flexible formats.

Types

- Document
- Key-Value
- Column Family
- Graph

Examples

- MongoDB
- Redis
- Cassandra
- Neo4j

---

# Relational Database Concepts

A relational database stores information using

- Tables
- Rows
- Columns

Example

```
Employees

ID

Name

Department

Salary
```

Each row represents one record.

Each column represents one attribute.

---

# Table

A table represents an entity.

Example

```
Employees
```

Columns

```
EmployeeID

Name

Salary

Department
```

---

# Row (Record)

Represents one object.

Example

```
101

Alice

90000

Engineering
```

---

# Column (Field)

Represents one property.

Example

```
Salary
```

---

# Schema

A schema defines the structure of a database.

Includes

- Tables
- Columns
- Data Types
- Constraints
- Relationships

---

# Data Types

Common SQL Data Types

| Type | Description |
|------|-------------|
| INT | Integer |
| BIGINT | Large integer |
| DECIMAL | Fixed precision number |
| FLOAT | Floating point |
| CHAR | Fixed-length string |
| VARCHAR | Variable-length string |
| TEXT | Large text |
| DATE | Date |
| TIME | Time |
| TIMESTAMP | Date and time |
| BOOLEAN | True/False |

---

# Keys

Keys uniquely identify records and establish relationships.

---

# Primary Key

Uniquely identifies each row.

Properties

✓ Unique

✓ Not NULL

Example

```
EmployeeID
```

---

# Composite Primary Key

Uses multiple columns.

Example

```
(StudentID, CourseID)
```

---

# Candidate Key

A column (or set of columns) that can uniquely identify a record.

Example

```
Email

EmployeeID
```

---

# Alternate Key

A candidate key that is not chosen as the primary key.

---

# Foreign Key

Creates relationships between tables.

Example

Employees

```
DepartmentID
```

references

Departments

```
DepartmentID
```

---

# Unique Constraint

Ensures all values are unique.

Example

```
Email
```

---

# NOT NULL Constraint

Prevents NULL values.

Example

```
Name VARCHAR(100) NOT NULL
```

---

# DEFAULT Constraint

Provides default values.

Example

```sql
status VARCHAR(20)

DEFAULT 'ACTIVE'
```

---

# CHECK Constraint

Restricts allowed values.

Example

```sql
salary > 0
```

---

# Entity Relationship (ER)

Example

```
Department

↓

1

↓

Many

Employees
```

---

# Cardinality

One-to-One

```
Person

↓

Passport
```

---

One-to-Many

```
Department

↓

Employees
```

---

Many-to-Many

```
Students

↓

Courses
```

Uses

```
Enrollment Table
```

---

# Referential Integrity

Ensures foreign keys reference valid records.

Example

Employee cannot reference a department that does not exist.

---

# Database Design Principles

Good database design

✓ Minimize redundancy

✓ Maintain consistency

✓ Ensure integrity

✓ Optimize queries

✓ Support scalability

---

# Introduction to Normalization

Normalization organizes data to reduce redundancy and improve integrity.

Goals

- Eliminate duplicate data
- Avoid update anomalies
- Improve consistency

Normal Forms

- 1NF
- 2NF
- 3NF
- BCNF

(Detailed discussion in Part 4.)

---

# SQL Overview

SQL

Structured Query Language

Used for

- Creating databases
- Creating tables
- Inserting data
- Updating data
- Querying data
- Deleting data

Categories

- DDL
- DML
- DCL
- TCL

---

# SQL Statement Example

```sql
SELECT

name,

salary

FROM Employees

WHERE salary > 50000;
```

---

# Database Connectivity in Python

Python provides multiple libraries.

SQLite

```python
import sqlite3
```

PostgreSQL

```python
import psycopg2
```

MySQL

```python
import mysql.connector
```

SQLAlchemy ORM

```python
from sqlalchemy import create_engine
```

---

# SQLite Example

```python
import sqlite3

connection = sqlite3.connect("company.db")

cursor = connection.cursor()

cursor.execute(

    "SELECT * FROM employees"

)

rows = cursor.fetchall()

for row in rows:

    print(row)

connection.close()
```

---

# Common Database Operations

Create

```
INSERT
```

Read

```
SELECT
```

Update

```
UPDATE
```

Delete

```
DELETE
```

Collectively called

```
CRUD
```

---

# Real-world Applications

Relational Databases

- Banking
- ERP
- HR Systems
- Inventory
- E-commerce

NoSQL

- Caching
- Chat Applications
- Analytics
- Recommendation Systems
- IoT

---

# Best Practices

✓ Use meaningful table names.

✓ Define primary keys.

✓ Use foreign keys for relationships.

✓ Choose appropriate data types.

✓ Avoid storing duplicate information.

✓ Design for future scalability.

---

# Common Mistakes

❌ Missing primary keys.

❌ Using incorrect data types.

❌ Storing comma-separated values in one column.

❌ Ignoring referential integrity.

❌ Overusing NULL values.

---

# Interview Questions

### Easy

1. What is a database?
2. Difference between DBMS and RDBMS.
3. What is a primary key?
4. What is a foreign key?
5. What is normalization?

### Medium

1. Explain candidate keys.
2. Compare SQL and NoSQL.
3. What is referential integrity?
4. Difference between schema and database.
5. Explain cardinality.

### Hard

1. Design a database for an e-commerce platform.
2. Explain many-to-many relationships.
3. How would you choose between SQL and NoSQL?
4. Explain data consistency.
5. Discuss trade-offs in database schema design.

---

# Coding Exercises

Easy

- Create a Students table.
- Add primary and foreign keys.
- Insert sample records.

Medium

- Design a Library Management schema.
- Create an Employee-Department relationship.

Hard

- Design a normalized database for an online shopping system.
- Build a blogging database with users, posts, comments, and tags.

---

# Summary

Databases are fundamental to backend development. Understanding relational concepts, keys, constraints, schemas, and database design provides the foundation for writing efficient SQL queries and building scalable applications. A solid grasp of these fundamentals is essential before learning advanced SQL, indexing, transactions, optimization, and ORM frameworks.

---


# 2. SQL Fundamentals

---

# What is SQL?

SQL (Structured Query Language) is the standard language used to interact with relational databases.

SQL is used to:

- Create databases
- Create tables
- Insert data
- Retrieve data
- Update data
- Delete data
- Manage permissions
- Control transactions

---

# SQL Categories

SQL statements are grouped into four major categories.

| Category | Purpose |
|----------|----------|
| DDL | Define database structure |
| DML | Manipulate data |
| DQL | Query data |
| DCL | Control permissions |
| TCL | Manage transactions |

---

# Sample Database

Throughout this module, we'll use the following table.

```sql
Employees

+----+----------+--------+--------+

| ID | Name     | Salary | DeptID |

+----+----------+--------+--------+

| 1  | Alice    | 70000  | 10     |
| 2  | Bob      | 50000  | 20     |
| 3  | Charlie  | 90000  | 10     |
| 4  | David    | 60000  | 30     |

+----+----------+--------+--------+
```

---

# DDL (Data Definition Language)

DDL defines database objects.

Commands

- CREATE
- ALTER
- DROP
- TRUNCATE
- RENAME

---

# CREATE DATABASE

```sql
CREATE DATABASE company;
```

Creates a new database.

---

# CREATE TABLE

```sql
CREATE TABLE Employees (

    ID INT PRIMARY KEY,

    Name VARCHAR(100),

    Salary DECIMAL(10,2),

    DeptID INT
);
```

---

# ALTER TABLE

Add a column

```sql
ALTER TABLE Employees

ADD Email VARCHAR(100);
```

Modify a column

```sql
ALTER TABLE Employees

ALTER COLUMN Salary

TYPE DECIMAL(12,2);
```

(Note: Syntax varies slightly between PostgreSQL, MySQL, SQL Server, etc.)

---

# DROP TABLE

```sql
DROP TABLE Employees;
```

Deletes

- Table
- Data
- Structure

---

# TRUNCATE TABLE

```sql
TRUNCATE TABLE Employees;
```

Removes all rows.

Keeps table structure.

Generally faster than DELETE without a WHERE clause.

---

# DML (Data Manipulation Language)

Manipulates records.

Commands

- INSERT
- UPDATE
- DELETE

---

# INSERT

Insert one row

```sql
INSERT INTO Employees

(ID, Name, Salary, DeptID)

VALUES

(5, 'Eva', 75000, 20);
```

---

Insert multiple rows

```sql
INSERT INTO Employees

VALUES

(6, 'Frank', 65000, 30),

(7, 'Grace', 80000, 10);
```

---

# UPDATE

```sql
UPDATE Employees

SET Salary = 72000

WHERE ID = 1;
```

Without `WHERE`, every row will be updated.

---

# DELETE

Delete one employee

```sql
DELETE FROM Employees

WHERE ID = 5;
```

Delete all records

```sql
DELETE FROM Employees;
```

The table remains.

---

# DQL (Data Query Language)

Primary command

```sql
SELECT
```

---

# SELECT All Columns

```sql
SELECT *

FROM Employees;
```

---

# SELECT Specific Columns

```sql
SELECT

Name,

Salary

FROM Employees;
```

---

# WHERE Clause

Filters rows.

```sql
SELECT *

FROM Employees

WHERE Salary > 60000;
```

---

# Comparison Operators

| Operator | Meaning |
|-----------|---------|
| = | Equal |
| != or <> | Not equal |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |

---

# Logical Operators

AND

```sql
WHERE Salary > 60000

AND DeptID = 10;
```

OR

```sql
WHERE DeptID = 10

OR DeptID = 20;
```

NOT

```sql
WHERE NOT DeptID = 10;
```

---

# BETWEEN

```sql
SELECT *

FROM Employees

WHERE Salary

BETWEEN 60000 AND 80000;
```

Inclusive.

---

# IN

```sql
WHERE DeptID

IN (10,20);
```

---

# NOT IN

```sql
WHERE DeptID

NOT IN (10,20);
```

---

# LIKE

Pattern matching.

Starts with

```sql
WHERE Name LIKE 'A%';
```

Ends with

```sql
WHERE Name LIKE '%e';
```

Contains

```sql
WHERE Name LIKE '%ar%';
```

Single character

```sql
WHERE Name LIKE '_o%';
```

---

# IS NULL

```sql
SELECT *

FROM Employees

WHERE Email IS NULL;
```

---

# IS NOT NULL

```sql
WHERE Email IS NOT NULL;
```

---

# DISTINCT

Removes duplicates.

```sql
SELECT DISTINCT

DeptID

FROM Employees;
```

---

# ORDER BY

Ascending

```sql
ORDER BY Salary ASC;
```

Descending

```sql
ORDER BY Salary DESC;
```

Multiple columns

```sql
ORDER BY

DeptID,

Salary DESC;
```

---

# LIMIT

PostgreSQL / MySQL

```sql
SELECT *

FROM Employees

LIMIT 5;
```

---

# OFFSET

```sql
SELECT *

FROM Employees

LIMIT 5

OFFSET 10;
```

Useful for pagination.

---

# SQL Aliases

Column alias

```sql
SELECT

Salary AS Income

FROM Employees;
```

Table alias

```sql
SELECT e.Name

FROM Employees e;
```

---

# Aggregate Functions

COUNT

```sql
SELECT COUNT(*)

FROM Employees;
```

---

SUM

```sql
SELECT SUM(Salary)

FROM Employees;
```

---

AVG

```sql
SELECT AVG(Salary)

FROM Employees;
```

---

MIN

```sql
SELECT MIN(Salary)

FROM Employees;
```

---

MAX

```sql
SELECT MAX(Salary)

FROM Employees;
```

---

# GROUP BY

Groups rows.

```sql
SELECT

DeptID,

COUNT(*)

FROM Employees

GROUP BY DeptID;
```

---

Average salary per department

```sql
SELECT

DeptID,

AVG(Salary)

FROM Employees

GROUP BY DeptID;
```

---

# HAVING

Filters grouped results.

```sql
SELECT

DeptID,

AVG(Salary)

FROM Employees

GROUP BY DeptID

HAVING AVG(Salary) > 70000;
```

Difference

WHERE

↓

Before grouping

HAVING

↓

After grouping

---

# SQL Execution Order

Logical processing order

```
FROM

↓

WHERE

↓

GROUP BY

↓

HAVING

↓

SELECT

↓

ORDER BY

↓

LIMIT
```

Understanding this order helps explain why aliases created in `SELECT` are generally unavailable in `WHERE`.

---

# CRUD Summary

| Operation | SQL Command |
|------------|-------------|
| Create | INSERT |
| Read | SELECT |
| Update | UPDATE |
| Delete | DELETE |

---

# Real-world Examples

Get all engineers

```sql
SELECT *

FROM Employees

WHERE DeptID = 10;
```

---

Highest salary

```sql
SELECT MAX(Salary)

FROM Employees;
```

---

Top five highest-paid employees

```sql
SELECT *

FROM Employees

ORDER BY Salary DESC

LIMIT 5;
```

---

Employees earning above average

```sql
SELECT *

FROM Employees

WHERE Salary >

(

SELECT AVG(Salary)

FROM Employees

);
```

(Subqueries are covered in detail in the next module section.)

---

# Best Practices

✓ Always use `WHERE` with `UPDATE` and `DELETE` unless intentionally affecting all rows.

✓ Select only required columns instead of using `SELECT *` in production code.

✓ Use meaningful aliases.

✓ Filter data as early as possible.

✓ Prefer parameterized queries in application code to prevent SQL injection.

---

# Common Mistakes

❌ Forgetting the `WHERE` clause in `UPDATE`.

❌ Forgetting the `WHERE` clause in `DELETE`.

❌ Using `SELECT *` unnecessarily.

❌ Confusing `WHERE` and `HAVING`.

❌ Assuming `NULL = NULL` is true (it is not; use `IS NULL`).

---

# Interview Questions

### Easy

1. What is SQL?
2. Difference between DELETE and TRUNCATE.
3. Difference between WHERE and HAVING.
4. What does DISTINCT do?
5. Explain GROUP BY.

---

### Medium

1. Explain SQL execution order.
2. Difference between DELETE, DROP, and TRUNCATE.
3. Explain aggregate functions.
4. Difference between LIKE and IN.
5. Why should `SELECT *` generally be avoided?

---

### Hard

1. Explain how SQL processes a query internally.
2. Why can't most column aliases be used in WHERE?
3. Compare GROUP BY and window functions.
4. Design a paginated query for millions of rows.
5. Discuss SQL injection and prevention strategies.

---

# Coding Exercises

Easy

- Create an Employees table.
- Insert five employee records.
- Retrieve employees with salary greater than 50,000.

Medium

- Find the average salary per department.
- Display departments with more than three employees.
- Retrieve the top three highest-paid employees.

Hard

- Find employees earning above the company average.
- Rank departments by average salary.
- Build paginated queries using LIMIT and OFFSET.

---

# Summary

SQL provides the core operations for defining, manipulating, and querying relational data. Understanding DDL, DML, DQL, filtering, grouping, sorting, aggregation, and execution order is essential for backend development and forms the foundation for more advanced topics such as joins, subqueries, window functions, indexing, and query optimization.

---


# 3. Advanced SQL Queries

---

# Introduction

Real-world applications rarely use data from a single table.

Example

```
Employees

Departments

Projects

Orders

Customers
```

These tables are connected using relationships.

SQL provides

- Joins
- Subqueries
- Common Table Expressions (CTEs)
- Window Functions

to query related data efficiently.

---

# Sample Tables

Employees

| EmployeeID | Name | Salary | DepartmentID |
|------------|------|---------|--------------|
| 1 | Alice | 90000 | 1 |
| 2 | Bob | 70000 | 2 |
| 3 | Charlie | 80000 | 1 |
| 4 | David | 65000 | 3 |

Departments

| DepartmentID | DepartmentName |
|---------------|----------------|
| 1 | Engineering |
| 2 | HR |
| 3 | Sales |

---

# SQL Joins

Joins combine rows from multiple tables.

Main Types

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL OUTER JOIN
- CROSS JOIN
- SELF JOIN

---

# INNER JOIN

Returns only matching rows.

```
Employees

↓

Departments

↓

Matching Records
```

Example

```sql
SELECT

e.Name,

d.DepartmentName

FROM Employees e

INNER JOIN Departments d

ON e.DepartmentID = d.DepartmentID;
```

Output

| Name | Department |
|------|------------|
| Alice | Engineering |
| Bob | HR |
| Charlie | Engineering |
| David | Sales |

---

# LEFT JOIN

Returns

- All rows from left table
- Matching rows from right table

Missing matches become NULL.

```sql
SELECT

e.Name,

d.DepartmentName

FROM Employees e

LEFT JOIN Departments d

ON e.DepartmentID = d.DepartmentID;
```

---

# RIGHT JOIN

Returns

- All rows from right table
- Matching rows from left table

```sql
SELECT

e.Name,

d.DepartmentName

FROM Employees e

RIGHT JOIN Departments d

ON e.DepartmentID = d.DepartmentID;
```

---

# FULL OUTER JOIN

Returns

- Left rows
- Right rows
- Matching rows

```sql
SELECT *

FROM Employees e

FULL OUTER JOIN Departments d

ON e.DepartmentID = d.DepartmentID;
```

(Note: MySQL does not support FULL OUTER JOIN directly.)

---

# CROSS JOIN

Cartesian Product

Every row combines with every row.

Example

```
4 Employees

×

3 Departments

=

12 Rows
```

```sql
SELECT *

FROM Employees

CROSS JOIN Departments;
```

---

# SELF JOIN

A table joins itself.

Example

Employee → Manager

```sql
SELECT

e.Name,

m.Name

FROM Employees e

LEFT JOIN Employees m

ON e.ManagerID = m.EmployeeID;
```

---

# Join Comparison

| Join | Returns |
|------|----------|
| INNER | Matching rows |
| LEFT | All left rows |
| RIGHT | All right rows |
| FULL | All rows |
| CROSS | Cartesian product |
| SELF | Table joins itself |

---

# UNION

Combines results.

Duplicates removed.

```sql
SELECT Name

FROM Employees

UNION

SELECT Name

FROM Managers;
```

---

# UNION ALL

Keeps duplicates.

```sql
SELECT Name

FROM Employees

UNION ALL

SELECT Name

FROM Managers;
```

Faster than UNION because no duplicate elimination is required.

---

# Subqueries

Query inside another query.

```
Outer Query

↓

Inner Query
```

---

# Single-row Subquery

Employees earning above average.

```sql
SELECT *

FROM Employees

WHERE Salary >

(

SELECT AVG(Salary)

FROM Employees

);
```

---

# Multi-row Subquery

```sql
SELECT *

FROM Employees

WHERE DepartmentID

IN

(

SELECT DepartmentID

FROM Departments

WHERE DepartmentName='Engineering'

);
```

---

# EXISTS

Returns TRUE if subquery returns at least one row.

```sql
SELECT *

FROM Departments d

WHERE EXISTS

(

SELECT 1

FROM Employees e

WHERE e.DepartmentID=d.DepartmentID

);
```

---

# Correlated Subquery

Inner query depends on outer query.

```sql
SELECT

Name,

Salary

FROM Employees e

WHERE Salary >

(

SELECT AVG(Salary)

FROM Employees

WHERE DepartmentID=e.DepartmentID

);
```

Evaluated once per outer row, which can be slower than equivalent joins or window functions on large datasets.

---

# Common Table Expression (CTE)

Improves readability.

Syntax

```sql
WITH EmployeeCTE AS

(

SELECT *

FROM Employees

)

SELECT *

FROM EmployeeCTE;
```

---

# Multiple CTEs

```sql
WITH

HighSalary AS

(

SELECT *

FROM Employees

WHERE Salary>80000

),

Engineering AS

(

SELECT *

FROM Departments

WHERE DepartmentName='Engineering'

)

SELECT *

FROM HighSalary;
```

---

# Recursive CTE

Used for

- Hierarchies
- Organization charts
- Trees

Example

```sql
WITH RECURSIVE EmployeeHierarchy AS

(

...

)
```

Applications

- Folder structures
- Employee hierarchy
- Category trees

---

# Window Functions

Window functions perform calculations across related rows **without collapsing the result into groups**.

Unlike GROUP BY, every row remains in the output.

---

# ROW_NUMBER()

Assigns unique sequence numbers.

```sql
SELECT

Name,

Salary,

ROW_NUMBER()

OVER(

ORDER BY Salary DESC

)

FROM Employees;
```

---

# RANK()

Same rank for ties.

Gaps remain.

```
100

Rank 1

100

Rank 1

90

Rank 3
```

---

# DENSE_RANK()

No gaps.

```
100

Rank 1

100

Rank 1

90

Rank 2
```

---

# PARTITION BY

Creates groups.

```sql
SELECT

Name,

DepartmentID,

Salary,

RANK()

OVER(

PARTITION BY DepartmentID

ORDER BY Salary DESC

)

FROM Employees;
```

Ranks employees within each department.

---

# LAG()

Access previous row.

```sql
SELECT

Salary,

LAG(Salary)

OVER(

ORDER BY Salary

)

FROM Employees;
```

Applications

- Trend analysis
- Difference calculations

---

# LEAD()

Access next row.

```sql
SELECT

Salary,

LEAD(Salary)

OVER(

ORDER BY Salary

)

FROM Employees;
```

---

# FIRST_VALUE()

Returns first value within the window.

---

# LAST_VALUE()

Returns last value within the window (window frame behavior may need adjustment depending on the database).

---

# NTILE()

Splits rows into groups.

Example

```sql
NTILE(4)
```

Quartiles.

---

# Window Function Applications

- Employee ranking
- Sales leaderboard
- Running totals
- Moving averages
- Trend analysis
- Time-series analytics

---

# Running Total

```sql
SELECT

Salary,

SUM(Salary)

OVER(

ORDER BY EmployeeID

)

FROM Employees;
```

---

# Moving Average

```sql
AVG(Salary)

OVER(

ORDER BY EmployeeID

ROWS BETWEEN 2 PRECEDING

AND CURRENT ROW
)
```

---

# Real-world Examples

Top paid employee per department

- RANK()
- PARTITION BY

Customer purchase trends

- LAG()

Monthly revenue

- SUM() OVER()

Employee hierarchy

- Recursive CTE

---

# Best Practices

✓ Use JOIN instead of correlated subqueries where appropriate.

✓ Use CTEs for readability.

✓ Use window functions for ranking and analytics.

✓ Prefer UNION ALL when duplicates do not need to be removed.

✓ Index join columns for better performance.

---

# Common Mistakes

❌ Missing JOIN conditions, producing unintended Cartesian products.

❌ Using correlated subqueries unnecessarily.

❌ Confusing GROUP BY with window functions.

❌ Choosing UNION when UNION ALL is sufficient.

❌ Ignoring NULL values after outer joins.

---

# Interview Questions

### Easy

1. Difference between INNER JOIN and LEFT JOIN.
2. What is a CROSS JOIN?
3. Difference between UNION and UNION ALL.
4. What is a subquery?
5. What is a CTE?

---

### Medium

1. Explain correlated subqueries.
2. Difference between ROW_NUMBER() and RANK().
3. Difference between RANK() and DENSE_RANK().
4. Explain PARTITION BY.
5. When should CTEs be preferred?

---

### Hard

1. Design an employee hierarchy using recursive CTEs.
2. Explain window function execution.
3. Optimize a query with multiple joins.
4. Compare joins, subqueries, and CTEs.
5. Design a sales ranking dashboard using window functions.

---

# Coding Exercises

Easy

- Retrieve employee and department names using INNER JOIN.
- List all departments, including those without employees.
- Use UNION to combine two result sets.

Medium

- Find employees earning above their department average.
- Rank employees within each department.
- Calculate running salary totals.

Hard

- Build an organizational hierarchy with recursive CTEs.
- Compute moving averages for monthly sales.
- Find the second-highest salary in each department using window functions.

---

# Summary

Advanced SQL enables efficient querying across related tables and analytical computations. Joins connect normalized data, subqueries solve nested retrieval problems, CTEs improve readability and recursive processing, and window functions support ranking, running totals, and time-series analysis without losing row-level detail. These features are essential for production database applications and are among the most frequently evaluated SQL topics in technical interviews.

---


# Python Developer Knowledge Base
# Module 05 — Database and SQL
# Part 4 — Database Performance, Transactions & Database Design

---

# 4. Database Indexing

## What is an Index?

An index is a data structure that improves the speed of data retrieval operations.

Without an index

```
Database

↓

Scan every row

↓

Find result
```

With an index

```
Database

↓

Index Lookup

↓

Required Rows
```

Similar to the index of a book.

---

# Why Indexes?

Indexes improve

- SELECT
- WHERE
- ORDER BY
- GROUP BY
- JOIN

They reduce disk I/O and improve query performance.

---

# Trade-offs

Advantages

✓ Faster reads

✓ Faster joins

✓ Better sorting

Disadvantages

❌ Extra storage

❌ Slower INSERT

❌ Slower UPDATE

❌ Slower DELETE

because indexes must also be maintained.

---

# Clustered Index

Rows are physically stored in index order.

Characteristics

- One clustered index per table
- Usually created on Primary Key

Example

```
EmployeeID

1

2

3

4

5
```

Rows are stored in this order.

---

# Non-Clustered Index

Stores

```
Indexed Value

↓

Pointer to row
```

Multiple non-clustered indexes can exist.

Example

```
Email

↓

Row Location
```

---

# Composite Index

Uses multiple columns.

Example

```sql
CREATE INDEX idx_emp

ON Employees

(DepartmentID, Salary);
```

Best for queries using both columns in the defined order.

---

# Unique Index

Ensures unique values.

Example

```
Email

Username
```

---

# When to Create Indexes

Good Candidates

- Foreign Keys
- Frequently searched columns
- JOIN columns
- ORDER BY columns
- GROUP BY columns

Avoid

- Very small tables
- Frequently updated columns
- Low-cardinality columns (e.g., boolean flags), unless justified by workload

---

# Query Optimization

## Goal

Retrieve data

- Faster
- Using less memory
- Using fewer CPU resources

---

# Optimization Techniques

✓ Use indexes

✓ Avoid `SELECT *`

✓ Filter early

✓ Use proper joins

✓ Limit returned rows

✓ Avoid unnecessary subqueries

✓ Analyze execution plans

---

# Query Execution Plan

Database optimizer decides

- Scan type
- Join order
- Index usage

Common operations

- Sequential Scan
- Index Scan
- Hash Join
- Merge Join
- Nested Loop Join

Example (PostgreSQL)

```sql
EXPLAIN

SELECT *

FROM Employees

WHERE EmployeeID = 10;
```

---

# Common Performance Problems

❌ Missing indexes

❌ Too many indexes

❌ Functions applied to indexed columns in WHERE clauses

❌ Large result sets

❌ Cartesian products

❌ N+1 query problem in ORMs

---

# Transactions

## Definition

A transaction is a sequence of database operations executed as a single logical unit.

Example

Bank Transfer

```
Debit Account A

↓

Credit Account B

↓

Commit
```

If one operation fails

↓

Rollback

---

# Transaction Commands

Begin

```sql
BEGIN;
```

Commit

```sql
COMMIT;
```

Rollback

```sql
ROLLBACK;
```

---

# ACID Properties

## Atomicity

All operations succeed

or

None succeed.

Example

Money transfer

Both debit and credit occur together.

---

## Consistency

Database remains valid before and after a transaction.

Constraints remain satisfied.

---

## Isolation

Concurrent transactions should not interfere incorrectly with each other.

Handled through isolation levels.

---

## Durability

After COMMIT

Data survives

- Crash
- Restart
- Power failure

through database recovery mechanisms.

---

# Isolation Levels

## Read Uncommitted

Allows dirty reads.

Fast

Less safe.

---

## Read Committed

Prevents dirty reads.

Default in PostgreSQL and many other databases.

---

## Repeatable Read

Ensures repeated reads within a transaction return the same data.

Prevents non-repeatable reads.

---

## Serializable

Highest isolation.

Behaves like transactions execute one after another.

Safest

Slowest

---

# Concurrency Problems

## Dirty Read

Transaction B reads uncommitted data from Transaction A.

---

## Non-Repeatable Read

A row changes between two reads in the same transaction.

---

## Phantom Read

A repeated query returns additional or missing rows because another transaction inserted or deleted matching records.

---

# Locks

Databases use locks to protect data.

Types

- Shared Lock (Read)
- Exclusive Lock (Write)
- Intent Lock (Internal coordination)

---

# Shared Lock

Allows

Read

Blocks conflicting writes.

---

# Exclusive Lock

Allows

Write

Blocks other reads and writes that conflict.

---

# Deadlock

Occurs when two or more transactions wait on each other indefinitely.

Example

Transaction A

Locks Table X

Needs Table Y

Transaction B

Locks Table Y

Needs Table X

↓

Deadlock

Modern databases detect deadlocks and abort one transaction.

---

# MVCC (Multi-Version Concurrency Control)

Used by

- PostgreSQL
- Oracle (different implementation)
- MySQL InnoDB (MVCC support)

Allows readers and writers to work concurrently using row versions.

Advantages

✓ Better concurrency

✓ Fewer read locks

✓ Improved scalability

---

# Normalization

Normalization reduces redundancy and improves consistency.

Goals

- Eliminate duplicate data
- Prevent update anomalies
- Improve integrity

---

# First Normal Form (1NF)

Rules

- Atomic values
- No repeating groups

Incorrect

| Student | Subjects |
|----------|-----------|
| Alice | Math, Physics |

Correct

| Student | Subject |
|----------|----------|
| Alice | Math |
| Alice | Physics |

---

# Second Normal Form (2NF)

Requirements

- Must satisfy 1NF
- No partial dependency on a composite primary key

---

# Third Normal Form (3NF)

Requirements

- Must satisfy 2NF
- No transitive dependency

Example

Instead of storing DepartmentName in every employee row,

Store Department separately and reference it using DepartmentID.

---

# Boyce-Codd Normal Form (BCNF)

A stricter version of 3NF.

Every determinant must be a candidate key.

---

# Denormalization

Purpose

Improve read performance by intentionally introducing redundancy.

Advantages

✓ Faster queries

✓ Fewer joins

Disadvantages

❌ Duplicate data

❌ More complex updates

Often used in analytics and reporting systems.

---

# CAP Theorem

Distributed systems can guarantee only two of the following three properties simultaneously during a network partition.

Consistency (C)

Every client sees the same data.

Availability (A)

Every request receives a response.

Partition Tolerance (P)

System continues operating despite network failures.

---

# CAP Trade-offs

CP Systems

- Strong consistency
- Lower availability during partitions

Example

Some distributed SQL databases.

AP Systems

- High availability
- Eventual consistency

Example

Many NoSQL databases.

CA Systems

Possible only when network partition tolerance is not a concern.

---

# OLTP vs OLAP

| OLTP | OLAP |
|------|------|
| Many small transactions | Large analytical queries |
| Insert/Update heavy | Read heavy |
| Highly normalized | Often denormalized |
| Banking | Business Intelligence |

---

# Best Practices

✓ Index frequently queried columns.

✓ Avoid unnecessary indexes.

✓ Keep transactions short.

✓ Choose appropriate isolation levels.

✓ Normalize transactional databases.

✓ Denormalize only after measuring performance needs.

✓ Analyze execution plans before optimizing.

---

# Common Mistakes

❌ Indexing every column.

❌ Long-running transactions.

❌ Ignoring execution plans.

❌ Over-normalizing analytical databases.

❌ Using SERIALIZABLE isolation unnecessarily.

❌ Forgetting transaction rollbacks on failures.

---

# Interview Questions

### Easy

1. What is an index?
2. Difference between clustered and non-clustered indexes.
3. What are ACID properties?
4. What is normalization?
5. What is a transaction?

---

### Medium

1. Explain isolation levels.
2. What causes deadlocks?
3. Explain MVCC.
4. Compare OLTP and OLAP.
5. When would you denormalize a database?

---

### Hard

1. Design an indexing strategy for an e-commerce platform.
2. Explain query optimization techniques.
3. Compare 3NF and BCNF.
4. Explain the CAP theorem with examples.
5. Diagnose a slow SQL query using an execution plan.

---

# Coding Exercises

Easy

- Create indexes on frequently searched columns.
- Demonstrate COMMIT and ROLLBACK.

Medium

- Normalize a customer-order schema to 3NF.
- Compare query performance with and without indexes.

Hard

- Optimize a multi-table reporting query.
- Design a transaction-safe money transfer workflow.
- Analyze and resolve a simulated deadlock.

---

# Summary

Efficient database systems depend on proper indexing, optimized queries, well-managed transactions, and sound schema design. Understanding ACID properties, isolation levels, MVCC, normalization, and the CAP theorem enables developers to build reliable, scalable, and high-performance applications. These concepts are fundamental for production backend systems and are frequently evaluated in senior software engineering interviews.

---

# Python Developer Knowledge Base
# Module 05 — Database and SQL
# Part 5 — Production Databases, ORMs, Caching & Python Integration

---

# PostgreSQL

## Overview

PostgreSQL is an open-source, enterprise-grade relational database known for:

- ACID compliance
- Advanced SQL support
- High reliability
- Extensibility
- Excellent concurrency (MVCC)

Common Use Cases

- Banking
- ERP Systems
- SaaS Applications
- Analytics
- Enterprise Backend Systems

Advantages

✓ Advanced indexing

✓ JSON/JSONB support

✓ Full-text search

✓ Window functions

✓ CTEs

✓ Stored procedures

✓ Strong transactional support

---

# MySQL

## Overview

MySQL is one of the world's most widely used relational databases.

Common Use Cases

- Web applications
- CMS platforms
- E-commerce
- Small to medium backend systems

Advantages

✓ Easy to learn

✓ Large ecosystem

✓ Good performance

✓ Mature tooling

---

# PostgreSQL vs MySQL

| Feature | PostgreSQL | MySQL |
|----------|------------|--------|
| SQL Standard Compliance | Excellent | Good |
| JSON Support | JSON & JSONB | JSON |
| Concurrency | Excellent (MVCC) | Good (InnoDB) |
| Window Functions | Yes | Yes |
| CTEs | Yes | Yes |
| Full-text Search | Built-in | Supported |
| Extensibility | High | Moderate |
| Best For | Complex applications | General web applications |

---

# SQLite

## Overview

SQLite is an embedded relational database.

Characteristics

- Serverless
- File-based
- Zero configuration
- Lightweight

Python

```python
import sqlite3
```

Use Cases

- Local applications
- Desktop software
- Mobile applications
- Learning SQL
- Unit testing

Limitations

- Limited write concurrency
- Not ideal for high-traffic production systems

---

# NoSQL Databases

## What is NoSQL?

NoSQL databases store data in formats other than traditional relational tables.

Categories

- Document
- Key-Value
- Column Family
- Graph

Advantages

✓ Flexible schema

✓ Horizontal scaling

✓ High availability

---

# MongoDB

## Document Database

Stores data as BSON documents.

Example

```json
{
    "_id": 1,
    "name": "Alice",
    "skills": ["Python", "FastAPI"],
    "experience": 5
}
```

Advantages

- Flexible schema
- Easy horizontal scaling
- Good for rapidly changing data

Use Cases

- Content management
- Product catalogs
- Event logging
- User profiles

---

# Redis

## In-Memory Database

Redis stores data primarily in memory for extremely fast access.

Supported Data Structures

- Strings
- Lists
- Sets
- Hashes
- Sorted Sets
- Streams

Applications

- Caching
- Session storage
- Rate limiting
- Message queues
- Leaderboards
- Pub/Sub

Example

```python
import redis

client = redis.Redis()

client.set("username", "alice")

print(client.get("username"))
```

---

# Caching

## Why Cache?

Without cache

```
Application

↓

Database

↓

Response
```

With cache

```
Application

↓

Redis

↓

Database (only if needed)
```

Benefits

✓ Lower latency

✓ Reduced database load

✓ Better scalability

---

# Cache Strategies

### Cache Aside

Application checks cache first.

If missing

↓

Load from database

↓

Store in cache

---

### Write Through

Write to

- Cache
- Database

simultaneously.

---

### Write Back

Write to cache first.

Database updated later.

Higher performance but more complex.

---

# Object Relational Mapping (ORM)

## What is ORM?

ORM maps database tables to Python objects.

Instead of writing raw SQL

```sql
SELECT *

FROM users;
```

Use Python

```python
users = session.query(User).all()
```

Advantages

✓ Less boilerplate

✓ Database abstraction

✓ Easier maintenance

✓ Improved readability

Disadvantages

❌ Can generate inefficient SQL if used poorly

❌ Learning curve

---

# SQLAlchemy

## Overview

Most popular ORM for Python.

Installation

```bash
pip install sqlalchemy
```

Create Engine

```python
from sqlalchemy import create_engine

engine = create_engine(

    "postgresql://user:password@localhost/db"
)
```

---

# Declarative Model

```python
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    name = Column(String)
```

---

# Session

```python
from sqlalchemy.orm import Session

with Session(engine) as session:

    users = session.query(User).all()
```

---

# CRUD with SQLAlchemy

Insert

```python
user = User(name="Alice")

session.add(user)

session.commit()
```

Query

```python
users = session.query(User).all()
```

Update

```python
user.name = "Bob"

session.commit()
```

Delete

```python
session.delete(user)

session.commit()
```

---

# Alembic

## Database Migrations

Alembic manages schema changes.

Installation

```bash
pip install alembic
```

Common Commands

Initialize

```bash
alembic init migrations
```

Create migration

```bash
alembic revision --autogenerate -m "create users table"
```

Apply migration

```bash
alembic upgrade head
```

Benefits

✓ Version control for schema

✓ Safe deployments

✓ Rollback support

---

# Connection Pooling

## Why?

Creating database connections is expensive.

Connection pools reuse existing connections.

Benefits

✓ Lower latency

✓ Better throughput

✓ Reduced resource usage

SQLAlchemy enables pooling by default for most database drivers.

---

# SQL Injection

## Dangerous Example

```python
query = f"""

SELECT *

FROM users

WHERE username = '{username}'
"""
```

This allows malicious input to alter the SQL query.

---

# Safe Queries

Use parameterized queries.

Example

```python
cursor.execute(

    "SELECT * FROM users WHERE username = %s",

    (username,)
)
```

Or use ORM query APIs.

---

# Database Backups

Common Strategies

- Full backup
- Incremental backup
- Point-in-time recovery (where supported)
- Replication

Best Practices

✓ Test restores regularly

✓ Encrypt backups

✓ Store backups offsite

---

# Monitoring

Monitor

- Slow queries
- Connection count
- CPU
- Memory
- Disk I/O
- Cache hit ratio
- Replication lag

Popular Tools

- pgAdmin
- PostgreSQL EXPLAIN
- MySQL Workbench
- Prometheus
- Grafana

---

# Python Database Best Practices

✓ Use connection pooling.

✓ Keep transactions short.

✓ Use parameterized queries.

✓ Use indexes wisely.

✓ Close sessions and connections properly.

✓ Handle exceptions and roll back failed transactions.

✓ Avoid N+1 query problems in ORMs.

✓ Paginate large result sets.

---

# Common Mistakes

❌ String concatenation in SQL.

❌ Long-running transactions.

❌ Fetching unnecessary columns.

❌ Ignoring indexes.

❌ Opening new database connections for every request.

❌ Storing secrets directly in source code.

---

# Interview Questions

### Easy

1. What is PostgreSQL?
2. Difference between PostgreSQL and MySQL.
3. What is SQLite?
4. What is Redis?
5. What is ORM?

---

### Medium

1. Explain SQLAlchemy architecture.
2. What is Alembic?
3. What is connection pooling?
4. Compare SQL and NoSQL.
5. Explain cache-aside strategy.

---

### Hard

1. Design a scalable caching layer using Redis.
2. Prevent SQL injection in Python applications.
3. Optimize ORM-generated queries.
4. Design a backup and disaster recovery strategy.
5. Compare PostgreSQL, MongoDB, and Redis for a social media platform.

---

# Practical Coding Exercises

Easy

- Connect Python to SQLite.
- Create a table with SQLAlchemy.
- Perform CRUD operations.

Medium

- Build a REST API using SQLAlchemy.
- Add Redis caching to frequently accessed endpoints.
- Create Alembic migrations.

Hard

- Optimize a slow SQLAlchemy query.
- Implement connection pooling in a production API.
- Build a cache-aside implementation with Redis and PostgreSQL.

---

# Production Architecture Example

```
                Client
                   │
                   ▼
            FastAPI / Django
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
     Redis Cache         PostgreSQL
        │                     │
        └──────────┬──────────┘
                   ▼
            SQLAlchemy ORM
                   │
             Connection Pool
```

---

# Module Summary

Modern Python backend applications rely on robust database technologies and efficient data access patterns. PostgreSQL and MySQL provide reliable relational storage, SQLite is ideal for lightweight use cases, MongoDB offers flexible document storage, and Redis delivers high-performance caching. SQLAlchemy and Alembic simplify database interaction and schema evolution, while connection pooling, secure parameterized queries, indexing, and monitoring ensure scalable, secure, and maintainable production systems.

---


