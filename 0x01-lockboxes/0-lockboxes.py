#!/usr/bin/python3
'''
Contains a method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    :param boxes: a list of lists, where each inner list represents a box
    and its contents (keys to other boxes).
    :return: True if all boxes can be opened, else False.
    """
    unlocked = set([0])  # set to keep track of unlocked boxes
    stack = [0]  # list to keep track of boxes to check next

    while stack:
        box = stack.pop()  # pop the last box in the stack
        for key in boxes[box]:  # check each key in the current box
            # if the key opens a box that hasn't been unlocked yet
            if key not in unlocked:
                # add that box to the set of unlocked boxes
                unlocked.add(key)
                # add that box to the stack to be checked later
                stack.append(key)

    # return True if all boxes can be unlocked, else False
    return len(unlocked) == len(boxes)
