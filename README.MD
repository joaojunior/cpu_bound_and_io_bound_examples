# Introduction

This repo contains the code used in the hands-on session at [Catenamedia](https://www.catenamedia.com/).

The main objective of this hands-on is show options to resolve CPU-bounds and I/O bounds problems in **python**.

In the CPU-Bounds problems we will show the **[merge-sort](https://en.wikipedia.org/wiki/Merge_sort)** algorithm and show the code for it with and without threads. Also, we
will make a benchmark of this solution with [cpython](https://github.com/python/cpython) and [pypy](https://pypy.org/) python's interpreter.

# CPU-Bound problem

We will use the merge-sort algorithm to show the CPU-Problem and options to resolve this type of problem in python. First we will see the code in python of this algorithm without threads.
After we will implement this algorithm with threads, using the module [threading](https://docs.python.org/3.7/library/threading.html). Then, we will make a benchmark of this two implementations using the cpython and the pypy python's interpreter. The objective
of this is compare how threads are executing in cpython and in pypy interpreter.

Also, we will discuss about use [multiprocessing](https://docs.python.org/3.7/library/multiprocessing.html) to resolve this problem, and why is difficult to use it in this problem.

The python code of the merge-sort algorithm presents in this repo is based on the code found in [https://www.geeksforgeeks.org/merge-sort/](https://www.geeksforgeeks.org/merge-sort/)

The python code without threads is in the branch merge_sort. And the python code with threads is in the thread merge_sort_with_threads.


## Merge-sort

The merge sort algorithm sort an array recursively. In each pass of the algorithm, if the size of the array is greater than 1, it divide the array in middle and create two new arrays. After, we call the merge-sort algorithm again with
this two new arrays. Finally, we combine this two sorted arrays in only one sorted array.


# I/O Bound problem
