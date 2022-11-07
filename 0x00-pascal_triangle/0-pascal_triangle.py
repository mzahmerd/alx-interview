#!/usr/bin/python3

''' This module generate a list of pascal triangle
given an integer.
'''
def pascal_triangle(n):
    '''This function accepts an integer (n)
    return a list containing the pascal triangle of n'''

    # empty list to store triangles
    triangle = []

    # return an empty list, if n is less than 1
    if(n<=0): return triangle

    # Generage n number of rows 
    for i in range(n):
        # calculate each entry in the triangle with "n choose k" formula 
        # C(n,c) or n!/k!*(n-k)! 
        # ref: https://www.mathsisfun.com/pascals-triangle.html
        # "!" means factorial: products of a series of 
        #descending natural numbers of a given number.
        triangle.append([factorial(i)//(factorial(k)*factorial(i-k)) for k in range(i+1)])
    return triangle


def factorial(n):
    '''This function accepts an integer n and returns a factorial value of n'''
    fact = 1
    if(n==0):
        return 1
    while(n > 0):
        fact = n * fact
        n -= 1
    return fact
