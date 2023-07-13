#!/usr/bin/python3
"""THis momdule contains minOperations() function that takes an integer n as
input and returns the fewest number of operations
needed to obtain n H characters in the file, and getPrimeFactors() A helper
function that calculate the prime factors of a number n.add()
"""


def minOperations(n):
    '''
     takes an integer n as input and returns the fewest number of operations
     needed to obtain n H characters in the file.
    '''
    if n == 1:
        return 0

    operations = 0
    factors = getPrimeFactors(n)

    for factor in factors:
        operations += factor

    return operations


def getPrimeFactors(n):
    '''
    A helper function that calculate the prime factors of a number n.
    '''
    factors = []
    i = 2

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors
