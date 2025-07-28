#!/usr/bin/python
# Author: Conan Yu
# Date: 11/26/2017

# Version 1.0
#====================================================================
from copy import copy, deepcopy

class Clone:
    """clone pattern的基類別"""

    def clone(self):
        """copy的方式clone對象"""
        return copy(self)

    def deepClone(self):
        """deepcopy的方式clone對象"""
        return deepcopy(self)