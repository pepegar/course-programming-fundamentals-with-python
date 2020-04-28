---
title: Programming fundamentals with Python
author: Pepe García
email: jgarciah@faculty.ie.edu
date: 2020-04-20
lang: en
---

Programming fundamentals with Python
====================================

https://slides.com/pepegar/pfp-10/live

Plan for today
==============

Learn what are modules and why they exist

Learn about standard library modules

Learn about third party modules

Create our own modules

Modules
=======

Python modules allow us to reuse code written somewhere else

Modules
=======

We, as programmers need to be lazy, and follow the DRY principles. 
That\'s what modules help with.

Modules
=======

To use modules, we need the import statement:

```python
import module
```

Modules
=======

When we import a module, all variables in the module are evaluated, all
functions created, and top level statements executed.

Modules
=======

Modules
=======

But, where does Python search for modules?

sys.path
========

Standard library
================

The stdlib is a set of modules for a lot of different purposes

Python follows a batteries included approach, trying to give us as
programmers everything we need

Standard library
================

We have already used some modules from the standard library before:

sys
===

sys contains functionality related with the current python session

```python
import sys

print(sys.path)

# ['', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python37.zip', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Users/pepe/Library/Python/3.7/lib/python/site-packages', '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.7/lib/python3.7/site-packages']
```

time
====

time module from the standard library contains utilities related to
**time**

```python
import time

while True:
    time.sleep(1)
    print("hello!")
```

math
====

math module contains useful functions and constants for doing numeric
and mathematic operations

```python
import math

math.ceil(3.4)
# 4


math.floor(3.4)
# 3
```

third party libraries
=====================

There are a lot of third party libraries:

<https://pypi.org>

example: matplotlib
===================

matplotlib is a great library for plotting and visualizing data

This library does not usually come installed with python, but we have it
because we installed anaconda! 🐍

matplotlib
==========

Recap
=====

Import modules with import

Create our own modules as files

stdlib contains a lot of useful stuff

third party libs can help when something is not on stdlib

Exercises
=========

Exercise 1
==========

create a more accurate version of **calculate\_volume\_cilinder** and
**calculate\_volume\_sphere** that gets the **pi** constant from the
**math** module

Exercise 2
==========

Investigate how to create histograms using the **matplotlib** library. 
Create a function that uses the **matplotlib** library to plot the
histogram of the grade distribution in an imaginary IE class with 100
students.  Remember that there are 15% pass, 35% proficiency, 35%
excellence, and 15% honors in a class.

Exercise 3
==========

Investigate about packages in Python, read this guide
<https://docs.python.org/3/tutorial/modules.html#packages>.

 

Create the following packages:\
- a **utils** package, containing a **functions** module.  The
**functions** module should contain a function **area\_triangle** that
calculates the area of a triangle.\
- a **data** package, containing a **triangles** module that declares a
variable **triangle\_definitions** with a list of 10 triangle
definitions.  Each triangle definition should be a dictionary like:

**{\"base\": 10, \"height\":2}**

\- a **main.py** file that will use **utils.functions.area\_triangle**
and **data.triangles.triangle\_definitions** to print the areas of all
triangles.

 

If you want to handle this exercise to me, please create a repository in
github named **black-belt-modules** and push your solution there.
