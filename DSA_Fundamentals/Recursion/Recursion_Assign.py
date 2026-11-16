"""
Assignment-18: Simple problems on recursion

Write a recursive function to print first N natural numbers.
Write a recursive function to print first N natural numbers in reverse order.
Write a recursive function to print first N odd natural numbers.
Write a recursive function to print first N even natural numbers.
Write a recursive function to print first N odd natural numbers in reverse order.
Write a recursive function to print first N even natural numbers in reverse order.
"""
def printN(n):
    if n > 0:
        printN(n-1)
        print(n, end=' ')
printN(10)
def printNreverse(n):
    if n > 0:
        print(n, end=' ')
        printNreverse(n-1)
printNreverse(10)
def printNOdd(n):
    if n > 0:
        printNOdd(n-1)
        print(2*n-1, end=' ')
printNOdd(10)
def printNEven(n):
    if n > 0:
        printNEven(n-1)
        print(2*n, end='')
printNEven(10)
def printNEvenreverse(n):
    if n >0:
        print(2*n, end=' ')
        printNEvenreverse(n-1)
printNEvenreverse(10)
def printNOddreverse(n):
    if n > 0:
        print(2*n-1, end=' ')
        printNOddreverse(n-1)
printNOddreverse(10)