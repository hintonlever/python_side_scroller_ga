# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:38:51 2021

@author: Benji
"""

# Functions to apply genetic algos

import pilot
import pygame

class Population():
    def __init__(self, size, GAME_HEIGHT, GAME_WIDTH):
        self.size = size
        
        # Create players with random weights
        self.pilots = pygame.sprite.Group()
        for i in range(1,self.size):
            self.pilots.add(pilot.Pilot(GAME_HEIGHT, GAME_WIDTH))
                

    





