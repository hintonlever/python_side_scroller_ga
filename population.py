# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:38:51 2021

@author: Benji
"""

# Functions to apply genetic algos

import pilot
import pygame
import random

class Population():
    def __init__(self, size, GAME_HEIGHT, GAME_WIDTH):
        # Random ID for tracing population
        self.id = random.randint(0,10000)
        
        # How many iterations have we been through
        self.generation = 1
        

        
        # How many pilots in this population
        self.size = size
                
        # Stats about this population
        self.all_dead = False
        self.cur_best_score = 0
        self.cur_best_pilot = 0 # position of best pilot in list
        
        # Stats about all populations
        self.all_best_score = 0
        
        
        # Create players with random weights
        self.pilots = pygame.sprite.Group()
        for i in range(1,self.size):
            self.pilots.add(pilot.Pilot(GAME_HEIGHT, GAME_WIDTH))
                
            
    def check_all_dead(self):
        for pilot in self.pilots:
            if pilot.alive = True:
                self.all_dead = False
                break
        self.all_dead = True
    
    def natural_selection(self):
        
        new_gen_pilots = pygame.sprite.Group()
        
        new_gen_pilot_count = 1
        
        # Find best pilot and keep them alive
        for i, pilot in enumerate(self.pilots):
            if pilot.score > self.cur_best_score:
                self.cur_best_score = pilot.score
                self.cur_best_pilot = i
                
        new_gen_pilots.add(self.pilots[i])
        
    
        # Crossover and mutate until we get enough new players
        
        while new_gen_pilot_count < self.size:
            
            parent_1 = pick_pilot()
            parent_2 = pick_pilot()
            
            # Combine the brains of the parents
            child = parent_1.crossover(parent_2)
            
            # Mutate brain of child
            child.mutate()

            # Add child to the new population
            new_gen_pilots.add(child)           
            new_gen_pilot_count = new_gen_pilot_count + 1
        
        
        
        # Overwrite previous generation
        self.pilots = new_gen_pilots
            
        # Store best score so far
        self.all_best_score = self.cur_best_score 
        
        # Reset current stats
        self.all_dead = False
        self.cur_best_score = 0
        self.cur_best_pilot = 0
    





