import os, sys
from typing import List


def Total(items: List[int]=[]):
    if items == None:
        return 0
    return sum(items)
