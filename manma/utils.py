import math


def LEFT(index):
    return 2 * index


def RIGHT(index):
    return LEFT(index) + 1


def PARENT(index):
    return math.floor(index / 2)