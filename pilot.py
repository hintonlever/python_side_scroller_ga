# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 20:51:39 2021

@author: Benji
"""

import neural_net
import pygame
import random

from pygame.locals import (
    RLEACCEL,
)


class Pilot(pygame.sprite.Sprite):
    def __init__(self, GAME_HEIGHT, GAME_WIDTH):
        super(Pilot, self).__init__()
        
        self.game_height = GAME_HEIGHT
        self.game_width = GAME_WIDTH
        
        # Using an image
        # the .convert() call optimizes the Surface, making future .blit() calls faster.
        self.surf = pygame.image.load("jet-fighter.png").convert()
        self.surf = pygame.transform.scale(self.surf,(40,40))
        # Reverse image
        self.surf = pygame.transform.flip(self.surf,1,0)        
        
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        
        #  Start on left wall somewhere
        self.rect = self.surf.get_rect(
            center=(
                20,
                # always start in middle
                # 300
                
                # Start randomly
                random.randint(0, self.game_height)
            )
        )
        self.alive = True
        
        
        # Initial score is zero, it has been alive 0 seconds!
        self.score = 0
        
        # The neural net brain
        self.nnet = neural_net.Neural_Net(3,4,1)

        
               

          
        
    def move_player(self,input_vector):
        
        # Let the net crunch the input and make a prediction
        brain_output = self.nnet.predict(input_vector)
        
        # Make a decision from the prediction
        # 0 is down, 1 is up
        up_or_down = round(brain_output[0])
        
        if up_or_down == 0:
            self.rect.move_ip(0, -5)
        if up_or_down == 1:
            self.rect.move_ip(0, 5)
            
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.game_width:
            self.rect.right = self.game_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.game_height:
            self.rect.bottom = self.game_height