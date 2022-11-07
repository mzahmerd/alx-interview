#!/usr/bin/python3
'''Lockbox helps you determine if a list of locks can be unlock
from the key found in the boxes'''


def canUnlockAll(boxes):
    '''
    this function accept list of boxes
    and return wheather all the boxes can be open
    '''
    # first box is already opened
    unlocked = {0}

    # loop through each box
    for i in range(len(boxes)):
        for j in range(1, len(boxes)):
            # check if the box contain key of the current box,
            # and it's not the box we took keys from.
            if (j in boxes[i] and j != i):
                # add the number to unlocked box.
                unlocked.add(j)
    return len(unlocked) == len(boxes)
