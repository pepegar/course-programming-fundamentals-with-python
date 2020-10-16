---
title: Programming fundamentals with Python
subtitle: Session 6
author: Pepe García <jgarciah@faculty.ie.edu>
email: jgarciah@faculty.ie.edu
date: 2020-10-16
lang: en
---

Plan for today
==============

>- Files refresher
>- Learn about JSON

# the **open** function

We can use **open()** to open a file in Python, we only need to pass
the path of the file we want to open.  Let's say there's a file named
hello.txt in my desktop that I want to open and read from Python, I
can do it as follows:

. . .

```python
file = open("/Users/pepe/Desktop/hello.txt")
```

# Reading the contents of a file

Now that we know how to open and close files, we can read the contents
of a file.  Let's do that line by line.

. . .

```python
file = open("/Users/pepe/Desktop/hello.txt")

for line in file:
    print(line)

file.close()
```

. . .

As you can see, we're treating `file` as a list of lines.

# Interlude, **with**

there is a useful Python keyword that one can use to make sure that
the file will always be closed, **with**:

. . .

```python
with open("file_path") as file:

    for line in file:
        #do something with line
        print(line)
```

# Handling files. modes

When opening a file, we can choose in which **mode** we open it
depending on how we're going to use it.

![file modes](./img/file-modes.png){width=100%}

# Writing files

We can write into files in a way similar to the one used for reading
them.

. . .

```python
with open('/Users/pepe/Desktop/goodbye.txt', 'w') as file:
    file.write("goodbye y'all!")
```


# CSV

CSV is a data interchange format used for representing tabular data.

# CSV - how does it look like?

::: columns

:::: column

. . .

>- **syntax** is, just the values separated by commas
>- We separate entries by adding a new line
::::

:::: column
![](./img/csv.png)
::::

:::


# CSV files - reading

The **csv** library is based on the idea of readers and writers.  One
can read all lines in a file like so:

::: columns

:::: column

```python
import csv

with open("file.csv") as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)  #line is a list
```

::::

:::: column

. . .

>- first we open the file normally
>- Then we create a reader using **csv.reader()**
>- Finally, we operate with the reader

::::

:::

# CSV files - writing

writing is not very different from reading:

```python
lines = [
  ["asdf", "qwer"],
  ["hello", "world"]
]

with open("file.csv", "a") as f:
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
```


# JSON

::: columns

:::: column

JSON (http://json.org) is a data interchange format, like CSV

The main difference is that with JSON we can represent arbitrary data, not only tabular data.

::::

:::: column

![](./img/json.png){width=100px}

::::

:::

# JSON - how does it look like?

::: columns

:::: column
![](./img/json-example.png)
::::

:::: column

. . .

>- **syntax** similar to Python data structures
>- supports **primitive** datatypes (**int, str, bool, float**).
>- supports collections of elements with **lists**
>- supports mapping of elements with **dictionaries**
::::

:::

# JSON

Some valid JSON values are:

::: columns

:::: column

```json
[1, 2, 3]
1
true
"potatoes"
{"name":"Pepe","surname":"Garcia"}
```

::::

:::: column

. . .

>- lists
>- integers
>- booleans
>- strings
>- dictionaries
::::

:::

# JSON

JSON is very similar to how we declare our data in Python but the cool
thing about it is that it can be used **from any language**.


# Homework

You will find the data files for these exercises in this repository:  https://github.com/pfp-2020/session-6

>-
