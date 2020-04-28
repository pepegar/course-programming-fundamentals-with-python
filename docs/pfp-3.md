---
title: Programming fundamentals with Python
author: Pepe García
email: jgarciah@faculty.ie.edu
date: 2020-04-20
lang: en
---

Programming fundamentals with Python
====================================

https://slides.com/pepegar/pfp-3/live

Plan for today
==============

Learn about dictionaries

Do some exercises with dictionaries

Talk about algorithms

Dictionaries
============

Dictionaries are data structures that map keys to values

Dictionaries: Syntax
====================

    my_dictionary = {
      "key": "value"
    }

Dictionaries: Syntax
====================

    empty_dictionary = {}

One can create an empty dictionary by using opening and closing curly
brackets

Dictionaries: Syntax
====================

    members = {
      "The Ramones": 4,
      "The Beatles": 4,
      "Straycats": 3
    }

Or you can create a dictionary and add key-value pairs to it directly:

Dictionaries: Syntax
====================

Adding  new elements to a dictionary
====================================

As with lists, you can use the following syntax:

``` {.makefile}
in_english = {}

in_english[33] = "thirty three"
in_english[5] = "five"
```

Adding  new elements to a dictionary
====================================

Deleting elements from a dictionary
===================================

As with lists, you can use the pop method!

``` {.makefile}
in_english = {}

in_english[33] = "thorty three"
in_english.pop(33)
in_english[33] = "thirty three"
```

Deleting elements from a dictionary
===================================

Looping dictionaries
====================

As with lists, the easiest way of looping over all elements in a
dictionary is a for loop:

``` {.makefile}
ingredients = {
  "potatoes": 3,
  "celery": 1,
  "onion": 1
}

for key in ingredients:
    print("I have " + ingredients[key] + " " + key)
```

Looping dictionaries
====================

Miscelanea
==========

There are lots of useful things that we can do with dictionaries:

``` {.makefile}
dictionary.keys() # returns all keys as a list
dictionary.values() # returns all values as a list
len(dictionary) # returns the number of elements in a dictionary
key in dictionary # returns true if the dictionary contains the key
key not in dictionary # returns true if the dictionary does not 
                      # contain the key
# and much more :)
```

Miscelanea
==========

Exercises
=========

``` {.makefile}
1. Create a function that receives a text and returns the frequency of
   each word in the text (as a dictionary).

2. Create a function that uses the previously generated dictionary and
   prints a bars diagram of the frequencies.  For example, the
   following:

   #+BEGIN_SRC 
   dictionary = {"a": 4, "hello": 1, "world": 3, "another": 2}
   diagram(dictionary)
   #+END_SRC 

   should print:

   #+BEGIN_SRC 
   a       | ****
   hello   | *
   world   | ***
   another | **
   #+END_SRC   
   
3. re-implement the phonebook example using a dictionary instead of
   two lists.
```
