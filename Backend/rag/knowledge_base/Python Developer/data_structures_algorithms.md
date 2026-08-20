# Python Developer Knowledge Base
# Module 04 — Data Structures and Algorithms

---

# Module Overview

Data Structures and Algorithms (DSA) form the foundation of efficient software development. They enable developers to organize data effectively and solve computational problems with optimal time and space complexity.

This module covers:

- Algorithm Analysis
- Time Complexity
- Space Complexity
- Big O, Big Ω, Big Θ
- Arrays
- Strings
- Complexity Analysis
- Common Interview Patterns
- Python Implementations

---

# 1. What is a Data Structure?

## Definition

A data structure is a specialized way of organizing and storing data so that it can be accessed and modified efficiently.

Goals

- Fast insertion
- Fast deletion
- Fast searching
- Efficient memory usage

Examples

- Array
- List
- Stack
- Queue
- Hash Table
- Tree
- Graph
- Heap

---

# Why Data Structures Matter

Choosing the right data structure directly impacts application performance.

Example

Finding an element in:

- List → O(n)
- Hash Table → O(1) average
- Balanced BST → O(log n)

A poor choice can make an application significantly slower.

---

# 2. What is an Algorithm?

## Definition

An algorithm is a finite sequence of well-defined steps to solve a problem.

Characteristics

- Input
- Output
- Definiteness
- Finiteness
- Effectiveness

Example

Find the maximum number in a list:

```python
def find_max(arr):
    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num

    return maximum
```

---

# Characteristics of a Good Algorithm

✓ Correct

✓ Efficient

✓ Readable

✓ Scalable

✓ Handles edge cases

---

# 3. Algorithm Analysis

Algorithm analysis measures:

- Execution time
- Memory usage
- Scalability

Two important metrics:

- Time Complexity
- Space Complexity

---

# Time Complexity

Time complexity describes how the running time of an algorithm grows with input size.

Notation

```
Input Size (n)

↓

Operations

↓

Growth Rate
```

---

# Common Time Complexities

| Complexity | Name | Example |
|------------|------|----------|
| O(1) | Constant | Dictionary lookup |
| O(log n) | Logarithmic | Binary Search |
| O(n) | Linear | Linear Search |
| O(n log n) | Linearithmic | Merge Sort |
| O(n²) | Quadratic | Bubble Sort |
| O(2ⁿ) | Exponential | Recursive Fibonacci |
| O(n!) | Factorial | Traveling Salesman (Brute Force) |

---

# Big O Notation

Big O describes the **upper bound** (worst-case performance).

Example

```python
for i in range(n):
    print(i)
```

Operations

```
n
```

Complexity

```
O(n)
```

---

# Big Ω (Omega)

Represents the **best-case** complexity.

Example

Linear search:

Finding the first element

```
O(1)
```

---

# Big Θ (Theta)

Represents the **average or tight bound**.

```
Best ≤ Average ≤ Worst
```

---

# Simplifying Complexity

Ignore:

- Constants
- Lower-order terms

Examples

```
O(2n)

↓

O(n)
```

```
O(n² + n)

↓

O(n²)
```

```
O(100)

↓

O(1)
```

---

# Space Complexity

Measures additional memory required.

Example

```python
numbers = [1,2,3]
```

Extra memory

```
O(n)
```

Example

```python
total = 0
```

Extra memory

```
O(1)
```

---

# Complexity Examples

### Constant Time

```python
print(arr[0])
```

Complexity

```
O(1)
```

---

### Linear Time

```python
for x in arr:
    print(x)
```

Complexity

```
O(n)
```

---

### Quadratic Time

```python
for i in arr:
    for j in arr:
        print(i, j)
```

Complexity

```
O(n²)
```

---

### Logarithmic Time

Binary Search repeatedly halves the search space.

```
1024

↓

512

↓

256

↓

128

↓

64

↓

32

↓

16

↓

8

↓

4

↓

2

↓

1
```

Complexity

```
O(log n)
```

---

# Amortized Complexity

Some operations are expensive occasionally but cheap on average.

Example

Python list append:

```python
numbers.append(10)
```

Average

```
O(1)
```

Occasionally resizing occurs, but the average cost remains constant.

---

# 4. Arrays

## Definition

An array is a contiguous block of memory storing elements of the same logical type.

In Python, the built-in `list` is a dynamic array.

Example

```python
numbers = [10, 20, 30, 40]
```

---

# Characteristics

- Ordered
- Index-based access
- Dynamic resizing
- Allows duplicate values

---

# Accessing Elements

```python
numbers = [10,20,30]

print(numbers[1])
```

Output

```
20
```

Complexity

```
O(1)
```

---

# Updating Elements

```python
numbers[2] = 99
```

Complexity

```
O(1)
```

---

# Appending

```python
numbers.append(50)
```

Average complexity

```
O(1)
```

Worst case (resize)

```
O(n)
```

---

# Inserting

```python
numbers.insert(0, 100)
```

Complexity

```
O(n)
```

Reason

All elements must shift.

---

# Deleting

```python
numbers.pop()
```

End of list

```
O(1)
```

Beginning

```python
numbers.pop(0)
```

Complexity

```
O(n)
```

---

# Searching

Linear search

```python
target = 30

for num in numbers:

    if num == target:

        print("Found")
```

Complexity

```
O(n)
```

---

# Python List Operations

| Operation | Complexity |
|-----------|------------|
| Index Access | O(1) |
| Append | O(1) amortized |
| Insert at Beginning | O(n) |
| Pop End | O(1) |
| Pop Beginning | O(n) |
| Search | O(n) |

---

# Advantages

✓ Fast random access

✓ Simple implementation

✓ Cache-friendly

✓ Efficient iteration

---

# Disadvantages

❌ Slow insertion at beginning

❌ Slow deletion at beginning

❌ Costly resizing in worst case

---

# Common Interview Problems (Arrays)

Easy

- Find maximum element
- Find minimum element
- Reverse an array
- Find second largest element
- Remove duplicates from a sorted array

Medium

- Rotate array
- Merge sorted arrays
- Product of array except self
- Move zeros to end
- Majority element

Hard

- Trapping Rain Water
- Maximum Subarray
- Median of Two Sorted Arrays
- First Missing Positive
- Sliding Window Maximum

---

# 5. Strings

## Definition

A string is an immutable sequence of Unicode characters.

Example

```python
text = "Python"
```

---

# String Characteristics

- Ordered
- Immutable
- Indexable
- Iterable

---

# Accessing Characters

```python
text = "Python"

print(text[2])
```

Output

```
t
```

Complexity

```
O(1)
```

---

# String Slicing

```python
text = "Python"

print(text[1:4])
```

Output

```
yth
```

Complexity

```
O(k)
```

Where `k` is the slice length.

---

# String Concatenation

```python
first = "Hello"

second = "World"

print(first + " " + second)
```

Complexity

```
O(n + m)
```

---

# String Immutability

```python
text = "Python"

text[0] = "J"
```

Produces

```
TypeError
```

Instead

```python
text = "J" + text[1:]
```

---

# Common String Operations

| Operation | Complexity |
|-----------|------------|
| Index Access | O(1) |
| Length | O(1) |
| Slice | O(k) |
| Concatenation | O(n + m) |
| Search (`in`) | O(n) average |
| Replace | O(n) |

---

# Common Interview Problems (Strings)

Easy

- Reverse a string
- Check palindrome
- Count vowels
- Remove spaces
- Character frequency

Medium

- Longest common prefix
- Group anagrams
- String compression
- Longest substring without repeating characters
- Valid parentheses

Hard

- Minimum window substring
- Edit distance
- Regular expression matching
- Wildcard matching
- Rabin-Karp pattern search

---

# Best Practices

✓ Choose the appropriate data structure for the problem.

✓ Analyze time and space complexity before coding.

✓ Favor built-in Python operations when they improve readability and performance.

✓ Consider edge cases such as empty inputs and large datasets.

---

# Common Mistakes

❌ Ignoring algorithm complexity.

❌ Using nested loops unnecessarily.

❌ Modifying immutable objects incorrectly.

❌ Choosing lists where a set or dictionary would be more efficient.

---

# Interview Questions

### Easy

1. What is Big O notation?
2. Difference between array and linked list.
3. Why are Python strings immutable?
4. What is amortized complexity?
5. What is the complexity of list append?

### Medium

1. Explain Big O, Big Ω, and Big Θ.
2. Why is `pop(0)` slower than `pop()`?
3. Compare arrays and hash tables.
4. How does Python implement dynamic arrays?
5. Explain cache locality.

### Hard

1. Analyze the complexity of Python list resizing.
2. Explain amortized analysis with examples.
3. Compare contiguous memory with linked allocation.
4. Why are arrays cache-friendly?
5. Discuss trade-offs between arrays, linked lists, and deques.

---

# Summary

Efficient software development begins with selecting the right data structures and understanding algorithm complexity. Arrays and strings are foundational structures that appear in almost every coding interview. Mastering their operations, performance characteristics, and common problem-solving patterns is essential before progressing to more advanced structures such as linked lists, trees, graphs, and heaps.

---

# 6. Linked Lists

---

# Definition

A linked list is a linear data structure where elements (called **nodes**) are connected using references (pointers).

Unlike arrays, elements are **not stored in contiguous memory**.

Structure

```
+------+    +------+    +------+
| 10 | •|-->| 20 | •|-->| 30 | X|
+------+    +------+    +------+
```

Each node contains:

- Data
- Reference to the next node

---

# Why Linked Lists?

Arrays are efficient for indexing but expensive for insertions and deletions in the middle.

Linked lists provide:

✓ Efficient insertion

✓ Efficient deletion

✓ Dynamic memory allocation

---

# Node Structure

```python
class Node:

    def __init__(self, data):

        self.data = data

        self.next = None
```

---

# Singly Linked List

Each node points only to the next node.

```
Head

↓

10 → 20 → 30 → None
```

---

# Traversal

```python
current = head

while current:

    print(current.data)

    current = current.next
```

Complexity

```
O(n)
```

---

# Insertion at Beginning

```python
new_node.next = head

head = new_node
```

Complexity

```
O(1)
```

---

# Insertion at End

Requires traversal.

Complexity

```
O(n)
```

---

# Deletion

Delete first node

```
head = head.next
```

Complexity

```
O(1)
```

Delete middle node

Requires traversal.

```
O(n)
```

---

# Doubly Linked List

Each node stores

- Previous
- Next

Structure

```
None

←

10

⇄

20

⇄

30

→

None
```

Advantages

- Reverse traversal
- Easier deletion

Disadvantages

- Extra memory

---

# Circular Linked List

Last node points back to the first node.

```
10

↓

20

↓

30

↓

10
```

Applications

- Round-robin scheduling
- Circular buffers
- Multiplayer games

---

# Linked List Complexities

| Operation | Complexity |
|-----------|------------|
| Access | O(n) |
| Search | O(n) |
| Insert Beginning | O(1) |
| Insert End | O(n) |
| Delete Beginning | O(1) |
| Delete Middle | O(n) |

---

# Advantages

✓ Dynamic size

✓ Fast insertions

✓ Fast deletions

---

# Disadvantages

❌ No random access

❌ Extra memory for pointers

❌ Poor cache locality

---

# Common Interview Problems

Easy

- Reverse linked list
- Find middle node
- Count nodes

Medium

- Detect cycle
- Merge sorted lists
- Remove nth node

Hard

- Reverse in groups
- LRU Cache
- Copy list with random pointer

---

# 7. Stack

---

# Definition

A stack follows the

```
LIFO

Last In

First Out
```

Example

```
Push 10

Push 20

Push 30

↓

Pop

30
```

---

# Operations

Push

```python
stack.append(10)
```

Pop

```python
stack.pop()
```

Peek

```python
stack[-1]
```

---

# Complexity

| Operation | Complexity |
|-----------|------------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |

---

# Applications

- Undo functionality
- Browser history
- Function calls
- Expression evaluation
- DFS

---

# Common Problems

- Valid Parentheses
- Next Greater Element
- Min Stack
- Largest Rectangle in Histogram

---

# 8. Queue

---

# Definition

Queue follows

```
FIFO

First In

First Out
```

Example

```
10

↓

20

↓

30

↓

Remove

10
```

---

# Queue using deque

```python
from collections import deque

queue = deque()

queue.append(10)

queue.append(20)

queue.popleft()
```

---

# Complexity

| Operation | Complexity |
|-----------|------------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Front | O(1) |

---

# Applications

- Scheduling
- Task processing
- BFS
- Printer queue

---

# Priority Queue

Elements removed based on priority.

Python

```python
import heapq

heap = []

heapq.heappush(heap, 10)

heapq.heappush(heap, 5)

print(heapq.heappop(heap))
```

Output

```
5
```

---

# Deque

Double-ended queue.

Supports insertion/removal from both ends.

```python
from collections import deque

dq = deque()

dq.append(10)

dq.appendleft(5)

dq.pop()

dq.popleft()
```

Complexity

```
O(1)
```

Applications

- Sliding window
- LRU cache
- Task scheduling

---

# Queue Complexities

| Operation | Complexity |
|-----------|------------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Peek | O(1) |

---

# 9. Hash Tables

---

# Definition

A hash table stores key-value pairs using a **hash function**.

Python implementation

```
dict
```

Example

```python
student = {

    "name": "Alice",

    "marks": 95
}
```

---

# Hash Function

Converts key

↓

Hash Code

↓

Index

```
"John"

↓

hash()

↓

14567

↓

Bucket
```

---

# Dictionary Operations

Insert

```python
student["age"] = 22
```

Search

```python
student["name"]
```

Delete

```python
del student["marks"]
```

---

# Complexity

Average

| Operation | Complexity |
|-----------|------------|
| Insert | O(1) |
| Search | O(1) |
| Delete | O(1) |

Worst case

```
O(n)
```

---

# Hash Collision

Two keys generate the same hash index.

```
Key A

↓

Bucket 3

Key B

↓

Bucket 3
```

---

# Collision Resolution

Separate Chaining

```
Bucket

↓

Node

↓

Node

↓

Node
```

Open Addressing

- Linear probing
- Quadratic probing
- Double hashing

---

# Python Dictionary Internals

Python dictionaries use

- Hash table
- Open addressing
- Dynamic resizing

Characteristics

✓ Ordered (Python 3.7+)

✓ Fast lookup

✓ Fast insertion

---

# Set

A set stores unique elements.

Example

```python
numbers = {1,2,3,4}
```

---

# Operations

Add

```python
numbers.add(5)
```

Remove

```python
numbers.remove(2)
```

Membership

```python
3 in numbers
```

Average complexity

```
O(1)
```

---

# Dictionary vs Set

Dictionary

```
Key

↓

Value
```

Set

```
Value only
```

---

# Advantages of Hash Tables

✓ Extremely fast lookup

✓ Efficient insertion

✓ Efficient deletion

✓ Ideal for caching

---

# Disadvantages

❌ Unordered in many languages

❌ Hash collisions

❌ Extra memory

---

# Real-world Applications

Linked List

- Music playlist
- Browser navigation

Stack

- Undo/Redo
- Expression parsing

Queue

- Task queues
- Job scheduling

Deque

- Sliding window algorithms
- LRU Cache

Hash Table

- Database indexing
- Session storage
- Caching
- Symbol tables

---

# Common Interview Problems

Linked List

- Reverse List
- Detect Cycle
- Merge Two Lists

Stack

- Balanced Parentheses
- Daily Temperatures
- Evaluate Postfix Expression

Queue

- Implement Stack using Queue
- Implement Queue using Stacks
- Circular Queue

Hash Table

- Two Sum
- Group Anagrams
- Top K Frequent Elements
- Longest Consecutive Sequence
- LRU Cache

---

# Best Practices

✓ Use `dict` for fast lookups.

✓ Use `set` for uniqueness checks.

✓ Use `deque` instead of list for queue operations.

✓ Avoid using list as a queue (`pop(0)` is O(n)).

✓ Choose linked lists only when frequent insertions/deletions outweigh random access needs.

---

# Common Mistakes

❌ Using list instead of deque for FIFO queues.

❌ Assuming dictionary lookup is always O(1) in the worst case.

❌ Forgetting linked lists do not support indexing.

❌ Ignoring hash collisions.

❌ Using mutable objects as dictionary keys.

---

# Interview Questions

### Easy

1. Difference between stack and queue.
2. Why is `deque` preferred over list for queues?
3. What is a hash table?
4. Difference between `dict` and `set`.
5. Why are dictionary lookups fast?

### Medium

1. Explain hash collisions.
2. How does Python resolve dictionary collisions?
3. Compare linked lists and arrays.
4. When should you use a priority queue?
5. Explain dictionary resizing.

### Hard

1. Design an LRU Cache.
2. Explain Python dictionary internals.
3. Compare chaining vs open addressing.
4. Discuss cache locality in linked lists vs arrays.
5. Design a thread-safe queue.

---

# Summary

Linked lists, stacks, queues, deques, hash tables, dictionaries, and sets are foundational data structures for efficient software development. Understanding their internal organization, operational complexity, and practical trade-offs is essential for solving coding interview problems and building scalable backend systems.

---

# 10. Trees

---

# Definition

A tree is a hierarchical, non-linear data structure consisting of **nodes** connected by **edges**.

Unlike linked lists, a node can have multiple children.

Example

```
        A
      / | \
     B  C  D
    / \
   E   F
```

Terminology

- Root
- Parent
- Child
- Sibling
- Leaf
- Edge
- Height
- Depth
- Level
- Subtree

---

# Important Properties

For a tree with **N nodes**

```
Edges = N - 1
```

A tree contains

- No cycles
- Exactly one path between two nodes

---

# Tree Traversal

Traversal means visiting every node.

Three depth-first traversals

```
Preorder

Root

↓

Left

↓

Right
```

```
Inorder

Left

↓

Root

↓

Right
```

```
Postorder

Left

↓

Right

↓

Root
```

Breadth-first traversal

```
Level Order
```

---

# Binary Tree

A binary tree is a tree where each node has at most two children.

```
       10

      /  \

     5   20

    / \    \

   2   8   25
```

---

# Binary Tree Node

```python
class TreeNode:

    def __init__(self, value):

        self.value = value

        self.left = None

        self.right = None
```

---

# Recursive Traversals

Preorder

```python
def preorder(node):

    if node is None:
        return

    print(node.value)

    preorder(node.left)

    preorder(node.right)
```

---

# Inorder

```python
def inorder(node):

    if node:

        inorder(node.left)

        print(node.value)

        inorder(node.right)
```

---

# Postorder

```python
def postorder(node):

    if node:

        postorder(node.left)

        postorder(node.right)

        print(node.value)
```

---

# Level Order Traversal

Uses a queue.

```python
from collections import deque
```

Complexity

```
O(n)
```

---

# Binary Search Tree (BST)

Definition

For every node

```
Left Subtree

<

Node

<

Right Subtree
```

Example

```
        50

      /    \

    30      70

   / \     / \

20 40   60 80
```

---

# Searching

```python
def search(root, key):

    if root is None:

        return False

    if root.value == key:

        return True

    if key < root.value:

        return search(root.left, key)

    return search(root.right, key)
```

Average Complexity

```
O(log n)
```

Worst

```
O(n)
```

---

# Insertion

Insert while maintaining BST property.

Average

```
O(log n)
```

Worst

```
O(n)
```

---

# Deletion Cases

Case 1

Leaf node

```
Delete directly
```

Case 2

One child

```
Replace with child
```

Case 3

Two children

Replace with

```
Inorder Successor

or

Inorder Predecessor
```

---

# Balanced Trees

Unbalanced BST

```
10

↓

20

↓

30

↓

40
```

Complexity

```
O(n)
```

Balanced Tree

```
      20

     /  \

   10   30

         \

         40
```

Complexity

```
O(log n)
```

---

# AVL Tree

Self-balancing BST.

Maintains

```
Balance Factor

=

Height(Left)

-

Height(Right)
```

Allowed values

```
-1

0

1
```

Uses rotations

- Left
- Right
- Left-Right
- Right-Left

---

# Red-Black Tree

Balanced BST with coloring rules.

Properties

- Red
- Black

Used in

- Java TreeMap
- Linux Kernel
- C++ STL

Advantages

- Guaranteed O(log n)

---

# Heap

Definition

A complete binary tree satisfying heap property.

---

# Max Heap

```
Parent

>

Children
```

Example

```
       50

      /  \

    40   30

   / \

 20 10
```

---

# Min Heap

```
Parent

<

Children
```

Example

```
      10

     /  \

   20   30

  / \

40 50
```

---

# Python Heap

Python provides

```python
heapq
```

which implements a **min heap**.

Example

```python
import heapq

heap = []

heapq.heappush(heap, 30)

heapq.heappush(heap, 10)

heapq.heappush(heap, 20)

print(heapq.heappop(heap))
```

Output

```
10
```

---

# Heap Complexity

| Operation | Complexity |
|-----------|------------|
| Insert | O(log n) |
| Delete | O(log n) |
| Peek | O(1) |
| Heapify | O(n) |

---

# Heap Applications

- Priority Queue
- Dijkstra Algorithm
- Task Scheduling
- Top K Problems
- Median of Stream

---

# Trie

Definition

A trie is a tree specialized for storing strings.

Example

```
cat

car

can
```

Tree

```
      c

      |

      a

   /  |  \

  t   r   n
```

---

# Advantages

✓ Fast prefix search

✓ Auto-complete

✓ Dictionary implementation

---

# Complexity

Insert

```
O(L)
```

Search

```
O(L)
```

Where

```
L

=

Length of word
```

---

# Trie Applications

- Search Engines
- Auto-complete
- Spell Checker
- IP Routing

---

# Segment Tree

Stores information about ranges.

Supports

- Range Sum
- Range Minimum
- Range Maximum

Complexity

Build

```
O(n)
```

Query

```
O(log n)
```

Update

```
O(log n)
```

Applications

- Competitive Programming
- Analytics
- Interval Queries

---

# Fenwick Tree (Binary Indexed Tree)

Efficient structure for prefix sums.

Operations

Update

```
O(log n)
```

Prefix Sum

```
O(log n)
```

Memory

```
O(n)
```

Applications

- Dynamic cumulative sums
- Frequency counting
- Competitive programming

---

# Tree Comparison

| Structure | Search | Insert | Delete |
|------------|--------|--------|--------|
| Binary Tree | O(n) | O(n) | O(n) |
| BST (Average) | O(log n) | O(log n) | O(log n) |
| BST (Worst) | O(n) | O(n) | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) |
| Red-Black Tree | O(log n) | O(log n) | O(log n) |
| Heap | O(n) | O(log n) | O(log n) |
| Trie | O(L) | O(L) | O(L) |

---

# Common Interview Problems

Trees

Easy

- Maximum Depth
- Invert Binary Tree
- Same Tree

Medium

- Lowest Common Ancestor
- Binary Tree Level Order Traversal
- Validate BST
- Kth Smallest Element

Hard

- Serialize and Deserialize Binary Tree
- Binary Tree Maximum Path Sum
- Recover BST

---

# Heap Problems

- K Largest Elements
- Merge K Sorted Lists
- Top K Frequent Elements
- Find Median from Data Stream

---

# Trie Problems

- Implement Trie
- Word Search
- Auto-complete System
- Replace Words

---

# Segment Tree Problems

- Range Sum Query
- Range Minimum Query
- Interval Updates

---

# Best Practices

✓ Use BST for ordered data.

✓ Use heaps for priority-based processing.

✓ Use tries for prefix searches.

✓ Keep trees balanced for logarithmic performance.

✓ Prefer iterative traversals when recursion depth may be large.

---

# Common Mistakes

❌ Assuming all BST operations are O(log n).

❌ Forgetting balancing in BST.

❌ Using recursion without considering stack depth.

❌ Confusing heap order with sorted order.

❌ Choosing a trie for very small datasets where a hash table is simpler.

---

# Interview Questions

### Easy

1. Difference between a binary tree and a BST.
2. What is a heap?
3. Explain inorder traversal.
4. What is a trie?
5. Why is heap peek O(1)?

### Medium

1. Compare AVL and Red-Black Trees.
2. Explain heapify.
3. Why does inorder traversal of a BST produce sorted output?
4. How does a trie perform prefix matching?
5. When should you use a segment tree?

### Hard

1. Design an autocomplete engine using tries.
2. Compare AVL, Red-Black Trees, and B-Trees.
3. Explain heap construction in O(n).
4. Design a scheduler using a priority queue.
5. Implement a range query system using a segment tree.

---

# Summary

Trees are fundamental hierarchical data structures used for representing relationships and enabling efficient searching. Binary Search Trees provide ordered access, balanced trees guarantee logarithmic performance, heaps power priority queues, tries enable fast prefix matching, and segment/Fenwick trees support efficient range queries. Mastery of these structures is essential for advanced coding interviews and high-performance software systems.

---

# 11. Graphs

---

# Definition

A graph is a non-linear data structure consisting of:

- Vertices (Nodes)
- Edges (Connections)

Unlike trees, graphs may contain cycles and multiple paths between nodes.

Example

```
      A
     / \
    B---C
     \
      D
```

---

# Terminology

- Vertex (Node)
- Edge
- Degree
- Path
- Cycle
- Connected Graph
- Disconnected Graph
- Directed Graph
- Undirected Graph
- Weighted Graph
- Unweighted Graph

---

# Types of Graphs

## Undirected Graph

Edges have no direction.

```
A ----- B
```

---

## Directed Graph (Digraph)

Edges have direction.

```
A -----> B
```

---

## Weighted Graph

Edges contain weights.

```
A --5--> B
```

---

## Cyclic Graph

Contains one or more cycles.

```
A

↓

B

↓

C

↓

A
```

---

## Acyclic Graph

Contains no cycles.

Example

```
A

↓

B

↓

C
```

---

# Graph Representation

## Adjacency List

Python representation

```python
graph = {

    "A": ["B", "C"],

    "B": ["A", "D"],

    "C": ["A"],

    "D": ["B"]
}
```

Advantages

✓ Memory efficient

✓ Preferred for sparse graphs

Complexity

```
O(V + E)
```

---

## Adjacency Matrix

```
      A B C

A     0 1 1

B     1 0 0

C     1 0 0
```

Advantages

✓ Fast edge lookup

Disadvantages

```
O(V²)
```

memory usage.

---

# Graph Traversal

Two major traversal algorithms

```
BFS

DFS
```

---

# Breadth-First Search (BFS)

Visits nodes level by level.

Uses

```
Queue
```

Example

```
      A

    /   \

   B     C

  / \

 D   E
```

Traversal

```
A

↓

B

↓

C

↓

D

↓

E
```

---

# BFS Implementation

```python
from collections import deque

def bfs(graph, start):

    visited = set()

    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:

            print(node)

            visited.add(node)

            queue.extend(graph[node])
```

Complexity

```
O(V + E)
```

---

# BFS Applications

- Shortest path (unweighted graph)
- Level-order traversal
- Social networks
- GPS navigation
- Web crawling

---

# Depth-First Search (DFS)

Explores one branch completely before backtracking.

Uses

- Recursion
- Stack

Traversal

```
A

↓

B

↓

D

↓

E

↓

C
```

---

# DFS Implementation

```python
def dfs(graph, node, visited):

    if node in visited:
        return

    print(node)

    visited.add(node)

    for neighbor in graph[node]:

        dfs(graph, neighbor, visited)
```

Complexity

```
O(V + E)
```

---

# DFS Applications

- Cycle detection
- Topological sorting
- Maze solving
- Connected components
- Backtracking problems

---

# BFS vs DFS

| Feature | BFS | DFS |
|---------|-----|-----|
| Data Structure | Queue | Stack/Recursion |
| Shortest Path | Yes (Unweighted) | No |
| Memory Usage | Higher | Lower |
| Traversal | Level-by-level | Depth-first |

---

# Topological Sort

Applies only to

```
Directed Acyclic Graph (DAG)
```

Produces a valid ordering where each node appears before its dependents.

Example

```
A

↓

B

↓

C
```

Valid order

```
A

↓

B

↓

C
```

Applications

- Task scheduling
- Build systems
- Dependency resolution

Complexity

```
O(V + E)
```

---

# Shortest Path Problems

Goal

Find minimum-cost path between two vertices.

---

# Dijkstra's Algorithm

Works on

```
Positive edge weights only
```

Uses

```
Priority Queue (Heap)
```

Complexity

Using heap

```
O((V + E) log V)
```

Applications

- GPS routing
- Network routing
- Maps

---

# Bellman-Ford Algorithm

Supports

```
Negative edge weights
```

Detects

```
Negative weight cycles
```

Complexity

```
O(V × E)
```

---

# Floyd-Warshall Algorithm

Finds shortest paths between

```
All pairs of vertices
```

Complexity

```
O(V³)
```

Applications

- Network analysis
- Traffic optimization

---

# Minimum Spanning Tree (MST)

Definition

Connects all vertices with minimum total edge weight.

Contains

```
V - 1 edges
```

---

# Prim's Algorithm

Starts from a node and grows the tree.

Uses

```
Priority Queue
```

Complexity

```
O(E log V)
```

---

# Kruskal's Algorithm

Sorts edges by weight.

Adds edges while avoiding cycles.

Uses

```
Union-Find
```

Complexity

```
O(E log E)
```

---

# Union-Find (Disjoint Set Union)

Efficiently manages disjoint sets.

Operations

Make Set

```
O(1)
```

Find

```
O(α(n))
```

Union

```
O(α(n))
```

where α(n) is the inverse Ackermann function (effectively constant for practical input sizes).

Applications

- Cycle detection
- Kruskal's Algorithm
- Network connectivity
- Connected components

---

# Cycle Detection

Undirected Graph

- DFS
- Union-Find

Directed Graph

- DFS with recursion stack
- Kahn's Algorithm

---

# Connected Components

A connected component is a maximal set of vertices where each vertex is reachable from every other vertex.

Applications

- Social networks
- Image segmentation
- Network analysis

---

# Graph Complexity Summary

| Algorithm | Complexity |
|-----------|------------|
| BFS | O(V + E) |
| DFS | O(V + E) |
| Topological Sort | O(V + E) |
| Dijkstra (Heap) | O((V + E) log V) |
| Bellman-Ford | O(V × E) |
| Floyd-Warshall | O(V³) |
| Prim | O(E log V) |
| Kruskal | O(E log E) |
| Union-Find (Find/Union) | O(α(n)) |

---

# Real-world Applications

Graphs

- Social media connections
- Airline routes
- Road maps
- Recommendation systems
- Knowledge graphs

BFS

- Shortest path in unweighted graphs
- Web crawlers

DFS

- Maze solving
- Dependency analysis

Dijkstra

- GPS navigation
- Routing protocols

Topological Sort

- Build tools
- CI/CD pipelines
- Course scheduling

Union-Find

- Dynamic connectivity
- Network clustering

---

# Common Interview Problems

Easy

- Graph Traversal (BFS/DFS)
- Number of Connected Components
- Find if Path Exists

Medium

- Clone Graph
- Course Schedule
- Number of Islands
- Rotten Oranges
- Pacific Atlantic Water Flow

Hard

- Word Ladder
- Alien Dictionary
- Reconstruct Itinerary
- Critical Connections
- Network Delay Time

---

# Best Practices

✓ Choose adjacency lists for sparse graphs.

✓ Use adjacency matrices for dense graphs with frequent edge lookups.

✓ Use BFS for shortest paths in unweighted graphs.

✓ Use Dijkstra only with non-negative weights.

✓ Use Union-Find for connectivity problems.

---

# Common Mistakes

❌ Using Dijkstra with negative edge weights.

❌ Forgetting to mark visited nodes.

❌ Using recursion without considering recursion depth.

❌ Confusing trees with graphs.

❌ Choosing an adjacency matrix for very sparse graphs.

---

# Interview Questions

### Easy

1. What is the difference between a tree and a graph?
2. Explain BFS and DFS.
3. What is an adjacency list?
4. What is an adjacency matrix?
5. What is a connected component?

### Medium

1. Compare BFS and DFS use cases.
2. Explain topological sorting.
3. Why does Dijkstra require non-negative weights?
4. How does Union-Find work?
5. Compare Prim's and Kruskal's algorithms.

### Hard

1. Design a route planner for a navigation application.
2. Explain path compression and union by rank.
3. Compare Bellman-Ford and Floyd-Warshall.
4. Design a recommendation system using graph traversal.
5. Solve dynamic connectivity problems efficiently.

---

# Coding Exercises

Easy

- Implement BFS.
- Implement DFS.
- Count connected components.

Medium

- Implement topological sort.
- Detect cycles in directed and undirected graphs.
- Find shortest path using BFS.

Hard

- Implement Dijkstra with `heapq`.
- Implement Kruskal using Union-Find.
- Solve "Network Delay Time" and "Word Ladder".

---

# Summary

Graphs model relationships between entities and are fundamental to many real-world systems, including navigation, social networks, recommendation engines, and dependency management. Mastering graph representations, traversal techniques, shortest-path algorithms, minimum spanning trees, and Union-Find is essential for solving advanced algorithmic problems and succeeding in technical interviews.

---

# 12. Recursion

---

# Definition

Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem.

Every recursive function has:

- Base Case
- Recursive Case

Example

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)
```

Execution

```
factorial(4)

↓

4 × factorial(3)

↓

4 × 3 × factorial(2)

↓

4 × 3 × 2 × factorial(1)

↓

4 × 3 × 2 × 1
```

---

# Advantages

✓ Elegant code

✓ Natural for trees and graphs

✓ Divide-and-conquer algorithms

---

# Disadvantages

❌ Stack overflow

❌ Higher memory usage

❌ Function call overhead

---

# Time Complexity

Depends on recurrence relation.

Example

```
T(n)

=

T(n-1)

+

O(1)

↓

O(n)
```

---

# Common Problems

- Factorial
- Fibonacci
- Binary Tree Traversal
- DFS
- Merge Sort
- Quick Sort

---

# Divide and Conquer

---

# Definition

Break a problem into smaller subproblems, solve them independently, then combine results.

Steps

```
Divide

↓

Conquer

↓

Combine
```

Examples

- Merge Sort
- Quick Sort
- Binary Search

---

# Binary Search

---

# Definition

Searches a sorted array by repeatedly dividing the search space in half.

Example

```
1 3 5 7 9 11 13

Target = 9
```

Python

```python
def binary_search(arr, target):

    left = 0
    right = len(arr)-1

    while left <= right:

        mid = (left + right)//2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1
```

Complexity

```
Time

O(log n)

Space

O(1)
```

---

# Binary Search Variants

- First occurrence
- Last occurrence
- Lower bound
- Upper bound
- Search in rotated array
- Peak element

---

# Sorting Algorithms

---

# Bubble Sort

Idea

Repeatedly swap adjacent elements.

Complexity

| Best | Average | Worst |
|------|---------|-------|
| O(n) | O(n²) | O(n²) |

Stable

✓ Yes

---

# Selection Sort

Idea

Repeatedly select minimum element.

Complexity

```
O(n²)
```

Stable

❌ No

---

# Insertion Sort

Idea

Insert each element into the sorted portion.

Complexity

| Best | Average | Worst |
|------|---------|-------|
| O(n) | O(n²) | O(n²) |

---

# Merge Sort

Divide array into halves.

Merge sorted halves.

Complexity

```
Time

O(n log n)

Space

O(n)
```

Stable

✓ Yes

---

# Quick Sort

Choose pivot.

Partition array.

Recursively sort.

Average

```
O(n log n)
```

Worst

```
O(n²)
```

Space

```
O(log n)
```

---

# Heap Sort

Uses Max Heap.

Complexity

```
O(n log n)
```

Space

```
O(1)
```

---

# Comparison

| Algorithm | Best | Avg | Worst | Stable |
|------------|------|-----|--------|--------|
| Bubble | O(n) | O(n²) | O(n²) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | No |
| Insertion | O(n) | O(n²) | O(n²) | Yes |
| Merge | O(nlogn) | O(nlogn) | O(nlogn) | Yes |
| Quick | O(nlogn) | O(nlogn) | O(n²) | No |
| Heap | O(nlogn) | O(nlogn) | O(nlogn) | No |

---

# Greedy Algorithms

---

# Definition

Always choose the locally optimal solution hoping it leads to the global optimum.

Examples

- Activity Selection
- Huffman Coding
- Fractional Knapsack
- Prim
- Kruskal
- Dijkstra

Advantages

✓ Fast

✓ Simple

Disadvantages

❌ Doesn't always produce optimal results.

---

# Backtracking

---

# Definition

Try a solution.

If it fails,

Backtrack.

Example

```
Choose

↓

Explore

↓

Undo

↓

Try Next
```

Applications

- N Queens
- Sudoku
- Word Search
- Permutations
- Combinations

---

# Dynamic Programming (DP)

---

# Definition

Solve overlapping subproblems once and reuse results.

Characteristics

- Overlapping Subproblems
- Optimal Substructure

Approaches

- Memoization (Top-down)
- Tabulation (Bottom-up)

---

# Fibonacci

Recursive

```
O(2ⁿ)
```

Dynamic Programming

```
O(n)
```

---

# Common DP Problems

Easy

- Climbing Stairs
- Fibonacci

Medium

- Coin Change
- House Robber
- Longest Increasing Subsequence

Hard

- Edit Distance
- Longest Common Subsequence
- Regular Expression Matching

---

# Sliding Window

---

# Definition

Maintain a moving window over an array or string.

Instead of recomputing everything, update the window incrementally.

Example

```
[1 2 3]

↓

[2 3 4]

↓

[3 4 5]
```

Complexity

Usually

```
O(n)
```

Problems

- Maximum Sum Subarray
- Longest Substring Without Repeating Characters
- Minimum Window Substring

---

# Two Pointers

---

# Definition

Use two indices moving through the data.

Example

```
Left →

← Right
```

Applications

- Two Sum (Sorted)
- Remove Duplicates
- Container With Most Water
- Merge Sorted Arrays

Complexity

Usually

```
O(n)
```

---

# Monotonic Stack

---

# Definition

A stack whose elements are always maintained in increasing or decreasing order.

Applications

- Next Greater Element
- Daily Temperatures
- Largest Rectangle in Histogram
- Stock Span

Complexity

```
O(n)
```

---

# Prefix Sum

---

# Definition

Store cumulative sums for efficient range queries.

Example

Array

```
1 2 3 4
```

Prefix

```
1 3 6 10
```

Range Sum

```
prefix[r]

-

prefix[l-1]
```

Complexity

Build

```
O(n)
```

Query

```
O(1)
```

---

# Problem-Solving Patterns

Recognize the pattern before coding.

| Pattern | Typical Problems |
|----------|------------------|
| Binary Search | Sorted arrays, search space |
| Sliding Window | Subarrays, substrings |
| Two Pointers | Sorted arrays, linked lists |
| Fast & Slow Pointers | Cycle detection, middle node |
| DFS | Trees, graphs, backtracking |
| BFS | Shortest path, level order |
| Dynamic Programming | Optimization problems |
| Greedy | Interval scheduling, MST |
| Heap | Top-K, scheduling |
| Prefix Sum | Range queries |
| Monotonic Stack | Next greater/smaller |
| Union-Find | Connectivity |

---

# Complexity Cheat Sheet

| Operation / Algorithm | Complexity |
|------------------------|------------|
| Array Access | O(1) |
| Hash Table Lookup | O(1) Avg |
| Binary Search | O(log n) |
| BFS | O(V + E) |
| DFS | O(V + E) |
| Merge Sort | O(n log n) |
| Quick Sort (Avg) | O(n log n) |
| Heap Insert | O(log n) |
| Trie Search | O(L) |
| Segment Tree Query | O(log n) |
| Prefix Sum Query | O(1) |

---

# Interview Strategy

1. Clarify the problem.
2. Discuss edge cases.
3. Explain brute-force approach.
4. Optimize.
5. Analyze complexity.
6. Write clean code.
7. Test with examples.

---

# Candidate Evaluation Rubric

Evaluate candidates on:

### Problem Understanding

- Clarifies requirements
- Identifies constraints
- Handles edge cases

### Algorithm Selection

- Chooses appropriate data structure
- Selects optimal algorithm
- Explains trade-offs

### Code Quality

- Readable
- Modular
- Pythonic
- Handles errors

### Complexity Analysis

- Correct Big O
- Space optimization
- Scalability awareness

### Communication

- Explains reasoning
- Responds to feedback
- Thinks aloud

---

# Common Interview Questions

Easy

- Reverse a linked list
- Binary search
- Valid parentheses
- Merge two sorted arrays
- Maximum subarray

Medium

- LRU Cache
- Kth Largest Element
- Course Schedule
- Top K Frequent Elements
- Coin Change
- Number of Islands

Hard

- Median of Two Sorted Arrays
- Merge K Sorted Lists
- Serialize Binary Tree
- Regular Expression Matching
- Word Ladder
- Trapping Rain Water
- Sliding Window Maximum
- Alien Dictionary

---

# Recommended Practice Progression

Beginner

- Arrays
- Strings
- Hash Maps
- Stacks
- Queues

Intermediate

- Linked Lists
- Trees
- Heaps
- Binary Search
- Sliding Window
- Two Pointers

Advanced

- Graphs
- Dynamic Programming
- Backtracking
- Union-Find
- Segment Trees
- Tries
- Advanced Graph Algorithms

---

# Module Summary

Data Structures and Algorithms form the foundation of technical interviews and efficient software engineering. A strong understanding of complexity analysis, fundamental data structures, algorithm design techniques, and common problem-solving patterns enables developers to write scalable, maintainable, and high-performance solutions.

For Python developers, mastering these concepts is essential for backend development, system design, AI/ML engineering, and coding interviews at companies ranging from startups to large technology organizations.

---