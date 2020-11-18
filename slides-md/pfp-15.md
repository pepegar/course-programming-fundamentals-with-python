---
title: Programming fundamentals with Python
subtitle: Modules and packages
author: Pepe García <jgarciah@faculty.ie.edu>
email: jgarciah@faculty.ie.edu
date: 2020-11-10
lang: en
---

# Plan for today

>- pip
>- PYPI
>- Downloading & using Python libraries

# pip

`pip` is a package manager for Python.  We will use it through the command line,
with one of these two flavours:

>- `pip3`
>- `python3 -m pip`
  
# pip

`pip` is a package manager for Python.  We will use it through the command line,
with one of these two flavours:

- `pip3`
- **`python3 -m pip`** I'll be using this one through today's session.

. . .


\begin{exampleblock}{Hint}

Whenever we use \textbf{\texttt{python3 -m whatever}} we're telling python to execute the
\textbf{\texttt{whatever}} module, pip in our case. 

\end{exampleblock}


# pip

There are a lot of commands available from pip

. . .

>- search packages **`pip search whatever`**
>- install packages **`pip install whatever`**
>- uninstall packages **`pip uninstall whatever`**

. . .

And... what can this **`whatever`** be?  Anything we want to search a library
for.

# pip

Imagine we want to use mergesort but we don't want to implement it, we would do
something like:

```
$ python3 -m pip search mergesort
mergesort (0.0.1)   - merge sort module.
sort-merge (0.0.1)  - Sorting a list of numbers with mergesort
```

. . .

\begin{exampleblock}{Remember}

blocks of code like this, starting with a dollar sign, mean that command was run
in the console

\end{exampleblock}

# pip

```
$ python3 -m pip install mergesort
Collecting mergesort
  Downloading mergesort-0.0.1.tar.gz (779 bytes)
Building wheels for collected packages: mergesort
  Running setup.py clean for mergesort
Failed to build mergesort
Installing collected packages: mergesort
    Running setup.py install for mergesort ... done
Successfully installed mergesort-0.0.1
```

# Troubleshooting

\begin{alertblock}{Where is python installed in your computer?}
    \begin{itemize}
        \item Mac: \texttt{/Users/youruser/opt/anaconda3/bin/python}
        \item Windows: \texttt{C:\textbackslash Users\textbackslash youruser\textbackslash Anaconda3\textbackslash python.exe}
    \end{itemize}
\end{alertblock}

# Troubleshooting (cont..)

It's possible that on your windows computer `python` is not behaving as you
expect.  This tutorial is handy for these cases.

https://www.datacamp.com/community/tutorials/installing-anaconda-windows

# Installing libraries with pip

In order to install libraries using pip we will first need to know which library
to install.  To make this search easier, the Python community maintains Pypi,
the Python Package Index, a website with all the available libraries and
instructions to install them.

**<https://pypi.org>**

# Python Package Index

::: columns
:::: {.column width=70%}
The Python Package Index is a great place to find libraries you may be interested in.
::::
:::: {.column widt=30%}
![](./img/pypi.jpg){width=100px}
::::
:::

. . .

\begin{exampleblock}{Searching in the Python Package Index}

Let's search for some libraries in the Python Package Index...

\end{exampleblock}

# Using libraries

Once we've found the library we want to use in our project, it's time to see how
it's used.  Normally libraries will have some documentation explaining how to
use them.

The place where this doc should be is in the homepage of the library.

# Using libraries

![](./img/hackernews.jpg)

# Using libraries

`hackernews-client` is a library for getting HackerNews
([`http://news.ycombinator.com`](http://news.ycombinator.com)) data
programatically.

# Using libraries - HN

```
$ python3 -m pip install hackernews-client

Collecting hackernews-client
  Using cached hackernews-client-0.1.2b1.tar.gz (8.1 kB)
Building wheels for collected packages: hackernews-client
  Building wheel for hackernews-client (setup.py) ... error
  Running setup.py clean for hackernews-client
Failed to build hackernews-client
Installing collected packages: hackernews-client
    Running setup.py install for hackernews-client ... done
Successfully installed hackernews-client-0.1.2b1
```

# Using libraries - HN

```python
from hackernews import hn # import the hn module from hackernews package






```

# Using libraries - HN

```python
from hackernews import hn

client = hn.NewsClient() # create a client




```

# Using libraries - HN

```python
from hackernews import hn

client = hn.NewsClient()

for story in client.get_best_story(10): # get 10 high score stories
    print(story.title)
```

# Recap

>- pip
>- Python package index
>- installing software for pip