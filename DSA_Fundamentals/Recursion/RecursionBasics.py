"""
Agenda ::

1> What is recursion ?
2> Recursion Tree ?
3> How to approach Recursive Solution

Recursion ::

Function calling itself is called recursion:
def f1():
    ...
    ...
    ...
    f1()

Note : In the recursion problem is solved in terms of problem itsself
        Each time recursion function call to itsself for little simpler version of the original
        problem

How to approach recursive function ?
Q> Write a recursive function to calculate sum of first n natural numbers ?
def f1(n):
    if n == 1:                           1> f1(n) 1+2+3+4+.......+n
        return 1                         2> f1(n-1) +n  1+2+3+.....+n-1+n
    return n +f1(n-1)                    3> n == 1

"""
def f1(n):
    if n == 1:
        return 1
    s = n + f1(n - 1)
    return s
result = f1(3)
print(result)