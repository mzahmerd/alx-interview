#!/usr/bin/python3

'''This function accept an intenger n
and return the fewest number of copy
and paste operations needed to create n number of H'''


def prime_factors(num):
    '''This function generate a list prime factors of a given number'''
    i = 2
    factors = []
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors


def minOperations(n):
    '''This function accept an intenger n
    and return the fewest number of copy
    and paste operations needed to create n number of H'''
    ops = 0
    chars = 'H'

    # impossible case
    if n <= 0:
        return ops
    # Generate prime factors of n
    factors = prime_factors(n)

    # Iterate through the factors and perform operations
    # upto number of the available facotrs
    while factors != []:
        cCopy = chars
        for i in range(factors[0]):
            chars += cCopy
            ops += 1
        factors.remove(factors[0])

    return ops
