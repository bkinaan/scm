# TO COMPLETE:

## Advanced Conditional Statements

List Comprehension
Python Dictionary Comprehension
Lambda Operator
Filter
Reduce
Map
Recursive Functions

## Regular Expressions

Advanced Regular Expressions - 2
Check whether a string starts and ends with the same character or not
_Password validation in Python_
Extracting email addresses using regular expressions in Python
Validating UPI IDs using Regular Expressions

## Object Oriented Programming

Inheritance
Encapsulation
Polymorphism
Operator Overloading

## Iterables, Iterators and Generators

Difference between iterable and iterator
Python `**iter**()` and `**next**()`
Generators in Python

## Closures and Decorators

how to define closures in Python?
how to develop a simple decorator in Python?
how to define a decorator that accepts one or more arguments?
Implement monkey patching
@staticmethod
@classmethod

## Memory Management

Memory Management
Garbage Collection
How does reference counting work in Python?
How dynamic typing works?
Mutable & Immutable objects
Memory Profiling
Deep Copy vs Shallow Copy
Optimization Tips for Python Code
How Python store the integers in the memory?

## Testing

Testing with Pytest
DocTests

# COMPLETED:

## Class and Object in Python

In `contacts/models.py`, the `Contact` **class** represents a Contact **object**.

## UnitTests

Within `tests/test_manager`, **UnitTests** are utlized to ensure the program is operating properly. The `run_tests` script also allows these tests to be run.

## Decorators

(how to define a class as a decorator?)

Within `contacts/models.py`, the Contact class includes an `@total_ordering` **decorator** which provides the remaining comparator functions using the provided `__eq__` and `__lt__` functions.

## Data Abstraction

When creating a contact in main using the manager, the process of creating the contact using the constructor is **abstracted** and done in the manager class instead.

## Advanced Regular Expressions - 1

Under the contacts directory, validators.py contains regex validations when adding or updating information for a contact.
