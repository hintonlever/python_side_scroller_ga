# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:38:51 2021

@author: Benji
"""

# Functions to apply genetic algos

import pilot

class Population():
    def __init__(self, size):
        self.size = size
        
        # Create players with random weights
        self.pilots = []
        for i in range(1,self.size):
            self.pilots.append(pilot.Pilot())
                

    





