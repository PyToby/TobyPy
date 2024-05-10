#!/usr/bin/env python3

"""
This program lets you analyze your disease.
"""

import random as ran
import time as tm


class Session():
    def __init__(self, diseases):
        self.diseases = diseases

    def analyze(self):
        print(ran.choice(self.diseases))


input("Enter your symptoms: ")
tm.sleep(1)
