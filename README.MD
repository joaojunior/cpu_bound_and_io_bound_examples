# 1. Introduction

This repo contains the code used in the hands-on session at [Catenamedia](https://www.catenamedia.com/).

The main objective of this hands-on is show options to resolve CPU-bounds and I/O bounds problems in **python**. Also we will discuss about this
options and the trade-off of each solution.

In the CPU-Bounds problems we will show the **[merge-sort](https://en.wikipedia.org/wiki/Merge_sort)** algorithm and show the code for it with and without threads. Also, we
will make a benchmark of this solution with [cpython](https://github.com/python/cpython) and [pypy](https://pypy.org/) python's interpreter.

In the I/O Bound problems we will create a crawler and a parser for an API. We will create the sequential code and the code with threads and asyncio.

# 2. CPU-Bound problem

We will use the merge-sort algorithm to show the CPU-Problem and options to resolve this type of problem in python. First we will see the code in python of this algorithm without threads.
After we will implement this algorithm with threads, using the module [threading](https://docs.python.org/3.7/library/threading.html). Then, we will make a benchmark of this two implementations using the cpython and the pypy python's interpreter. The objective
of this is compare how threads are executing in cpython and in pypy interpreter.

Also, we will discuss about use [multiprocessing](https://docs.python.org/3.7/library/multiprocessing.html) to resolve this problem, and why is difficult to use it in this problem.

The python code of the merge-sort algorithm presents in this repo is based on the code found in [https://www.geeksforgeeks.org/merge-sort/](https://www.geeksforgeeks.org/merge-sort/)

The python code without threads is in the branch [merge_sort](https://github.com/joaojunior/cpu_bound_and_io_bound_examples/tree/merge_sort). And the python code with threads is in the thread [merge_sort_with_threads](https://github.com/joaojunior/cpu_bound_and_io_bound_examples/tree/merge_sort_with_threads).


## 2.1 Merge-sort

The merge sort algorithm sort an array recursively. In each pass of the algorithm, if the size of the array is greater than 1, it divide the array in middle and create two new arrays. After, we call the merge-sort algorithm again with
this two new arrays. Finally, we combine this two sorted arrays in only one sorted array.


# 3. I/O Bound problem

The main objective here is show that threads in Python(cpython) are concurrent and not parallel for I/O bound problems.

For it, we will create a crawler to get the data from the api [http://api.population.io/](http://api.population.io/).
This api has data about population in all countries.

We will discuss about the sequential code, concurrent code with threads and asyncio for this type of problem in python.
With it we will show and discuss about new libraries in python to work with non blocking I/O.

## 3.1 Problem

With the data about quantity of women and men in Malta, we would like to calculate the rate between women and men in all years, start
in 1950 and finish in 2018.

## 3.2 Code examples

- The branch [crawler](https://github.com/joaojunior/cpu_bound_and_io_bound_examples/tree/crawler) has the python code of the crawler. The objective
here is show the api, the response and how to make http requests with python.

- The branch [crawler_with_threads](https://github.com/joaojunior/cpu_bound_and_io_bound_examples/tree/crawler_with_threads) has the python code of the crawler
with threads. The objective here is implement the threads in the code of the previous example.

- The branch [crawler_and_parser](https://github.com/joaojunior/cpu_bound_and_io_bound_examples/tree/crawler_and_parser) has the python code of the crawler
and the parser. The objective here is show the problem that we will resolve.

- The branch [crawler_and_parser_with_threads](https://github.com/joaojunior/cpu_bound_and_io_bound_examples/tree/crawler_and_parser_with_threads) has the python code of the crawler and the parser with threads. The objective here is show how to use threads when we need to use the response of the method.

- The branch [crawler_and_parser_with_asyncio](https://github.com/joaojunior/cpu_bound_and_io_bound_examples/tree/crawler_and_parser_with_asyncio) has the python code of the crawler and the parser with asyncio. Here, we have the same objective as the last example, but using asyncio library for non-blocking I/O.
in the code of the previous example.

# 4. Exercises
1. Write the merge-sort algorithm with asyncio library.
2. The asyncio improve the performance of the merge-sort algorithm(comparing with threads)? How can you explain the results?
3. Is asyncio a good library to resolve CPU bound problems? Why?
4. Theads in python(using cpython interpreter) are parallel or concurrent for CPU bound problems? Why?
5. For I/O bound problems, the threads and asyncio are concurrent programming? Why?
6. Make 1 million of requests with threads and asyncio with batch size of 100, 1k and 10k and compare the performance.
7. Change the parser(see the code of the crawler) in two functions: one to calculate the amount of men and another to calculate the amount of women and call this two functions with threads and with asyncio.

# 5. References

- [Merge sort algorithm](https://en.wikipedia.org/wiki/Merge_sort)
- [Understanding the Python GIL - by David Beazley](http://www.dabeaz.com/GIL/)
- [Async IO in Python: A Complete Walkthrough - by Brad Solomon](https://realpython.com/async-io-python/)
- [Asynchronous Python for the Complete Beginner - by Miguel Grinberg](https://www.youtube.com/watch?v=iG6fr81xHKA)
- [Creating a faster crawler - by Joao Junior](http://joaojunior.org/presentations/creating-a-faster-crawler/)
- [Module threading in python](https://docs.python.org/3.7/library/threading.html)
- [Module asyncio in python](https://docs.python.org/3/library/asyncio.html)
- [Library AIOHTTP](https://aiohttp.readthedocs.io/en/stable/)
- [Awesome asyncio](https://github.com/timofurrer/awesome-asyncio)

