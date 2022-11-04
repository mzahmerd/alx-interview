def pascal_triangle(n):
    # empty list to store triangles
    triangle =[]
    
    # return an empty list, if n is less than 1
    if(n<=0): return triangle
    
    # Generage n number of rows 
    for i in range(n):
        # calculate each entry in the triangle with "n choose k" formula 
        # C(n,c) or n!/k!*(n-k)!
        # "!" means factorial: products of series of descending natural numbers of a given number.
        triangle.append([factorial(i)//(factorial(k)*factorial(i-k)) for k in range(i+1)])
    return triangle
    
def factorial(n):
    fact = 1
    if(n==0):
        return 1
    while(n>0):
        fact = n*fact
        n-=1
    return fact
