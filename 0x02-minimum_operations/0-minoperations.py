#!/usr/bin/python3

'''This function accept an intenger n
and return the fewest number of copy
and paste operations needed to create n number of H'''


def minOperations(n):
    '''This function accept an intenger n
    and return the fewest number of copy
    and paste operations needed to create n number of H'''

    ops = 0
    chars = 'H'
    # keeps accumulating as long as number of H's
    # is not upto n
    while (len(chars) < n):
        # Copy operation
        cChars = chars
        # increment numbers of operations performed
        ops += 1
        # Paste operation
        chars += cChars
        ops += 1
        # Paste again, if number of H's is not upto n
        if (len(chars) < n):
            chars += cChars
            ops += 1
        # Paste again, if this will be the last operation
        if (len(chars) < n and len(chars) + len(cChars) >= n):
            chars += cChars
            ops += 1
    return ops
