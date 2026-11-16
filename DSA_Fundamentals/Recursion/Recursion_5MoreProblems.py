"""
Write a recursive function to calculate sum of first N natural numbers.
Write a recursive function to calculate sum of first N odd natural numbers.
Write a recursive function to calculate sum of first N even natural numbers.
Write a recursive function to calculate factorial of a number.
Write a recursive function to calculate sum of squares of first N natural numbers.
"""

def SumNaturalNo(n):
    if n == 1:
        return 1
    return n + SumNaturalNo(n-1)
print(SumNaturalNo(10))
def SumOddNaturalNo(n):
    if n == 1:
        return 1
    return 2*n-1 + SumNaturalNo(n-1)
print(SumNaturalNo(10))
def SumEvenNaturalNo(n):
    if n == 1:
        return 1
    return 2*n + SumEvenNaturalNo(n-1)
print(SumEvenNaturalNo(10))
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(10))
def SumNSquare(n):
    if n == 1:
        return 1
    return n*n + SumNSquare(n-1)
print(SumNSquare(20))