# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 14:07:02 2021

@author: Benji
"""


# Based on this tutorial
# https://realpython.com/pygame-a-primer/#note-on-sources

import pygame

# Import random for random numbers
import random

from pygame.locals import *
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg


fig = plt.figure(figsize=[3, 3])
ax = fig.add_subplot(111)
canvas = agg.FigureCanvasAgg(fig)

def bar_plot(x,y):
    plt.bar(x, y, color='green')
     # plt.xlabel("Energy Source")
     # plt.ylabel("Energy Output (GJ)")
     # plt.title("Energy output from various fuel sources")
     
     # plt.xticks(x_pos, x)
     
     # plt.show()
    
    # ax.plot(data)
    canvas.draw()
    renderer = canvas.get_renderer()
    
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()
    
    return pygame.image.fromstring(raw_data, size, "RGB")



# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

GAME_WIDTH = 600
GAME_HEIGHT = 600

# Sprites are from flaticon.com

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # Simple rectangle
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
               
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
                random.randint(0, GAME_HEIGHT),
            )
        )
          

        
    # Move the sprite based on user keypresses
    # .move_ip(), which stands for move in place
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > GAME_WIDTH:
            self.rect.right = GAME_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= GAME_HEIGHT:
            self.rect.bottom = GAME_HEIGHT
            

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("enemy.png").convert()
        self.surf = pygame.transform.scale(self.surf,(40,40))
        self.surf = pygame.transform.rotate(self.surf,90)
        self.surf.set_colorkey((0,0, 0), RLEACCEL)
             
        self.rect = self.surf.get_rect(
            center=(
                random.randint(GAME_WIDTH + 20, GAME_WIDTH + 100),
                random.randint(0, GAME_HEIGHT),
            )
        )
        self.speed = random.randint(5, 10)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            
class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.score = 0
        self.surf = myfont.render(str(self.score), False, (0,0,0))
        self.rect = self.surf.get_rect(center = (800,30))
        
    def update(self,seconds_alive):
        self.score = seconds_alive
        self.surf = myfont.render(str(self.score), False, (0,0,0))

class Alive_Counter(pygame.sprite.Sprite):
    def __init__(self):
        super(Alive_Counter, self).__init__()
        self.alive_count = 0
        self.surf = myfont.render(str(self.alive_count), False, (0,0,0))
        self.rect = self.surf.get_rect(center = (800,80))
        
    def update(self,new_count):
        self.alive_count = new_count
        self.surf = myfont.render(str(self.alive_count), False, (0,0,0))

class Random_Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Random_Player, self).__init__()
               
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
                random.randint(0, GAME_HEIGHT)
            )
        )
        self.alive = True
        self.score = 0
          
        
    def move_player(self):
        # 0 is down, 1 is up
        up_or_down = round(random.random())
        
        if up_or_down == 0:
            self.rect.move_ip(0, -5)
        if up_or_down == 1:
            self.rect.move_ip(0, 5)
            
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > GAME_WIDTH:
            self.rect.right = GAME_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= GAME_HEIGHT:
            self.rect.bottom = GAME_HEIGHT


# Create the screen object
# The size is determined by the constant GAME_WIDTH and GAME_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Setup the clock for a decent framerate
clock = pygame.time.Clock()
            
# Initialize pygame
pygame.init()
# Need this for text
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# Create a custom event for adding a new enemy
# pygame defines events internally as integers, so you need to define a new event with a unique integer. The last event pygame reserves is called USEREVENT, so defining ADDENEMY = pygame.USEREVENT + 1 on line 83 ensures it’s unique.
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 300)


# Human player
human_player = Player()

# AI Players
total_random_players = 1000
players = pygame.sprite.Group()

for i in range(1,total_random_players):
    player = Random_Player()
    players.add(player)
    




score = Score()
alive_counter = Alive_Counter()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering

enemies = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
# all_sprites.add(human_player)
all_sprites.add(players)
all_sprites.add(score)
all_sprites.add(alive_counter)

start_ticks=pygame.time.get_ticks() #starter tick

# Run until the user asks to quit
running = True
while running:
    # Fill the screen with black
    screen.fill((255, 255, 255))
    pygame.draw.line(screen,"black",(600,0),(600,600)) 
        
    
  # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
            
              # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

 
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    
    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
 
            
    # Update score
    seconds=(pygame.time.get_ticks()-start_ticks)/1000 
    score.update(seconds)
    
    # LET THE AI'S PLAY
    alive_count = 0
    final_scores = []
    for player in players:
        if player.alive == True:
            alive_count = alive_count + 1
            player.score = seconds
            player.move_player()
        # if player.alive == False:
            
 
            # Check if any enemies have collided with the player
        if pygame.sprite.spritecollideany(player, enemies):
            # If so, then remove the player and stop the loop
            final_scores.append(player.score)
            player.kill()
            # player.alive = False
            # running = False
    alive_counter.update(alive_count)   
            
    # LET THE HUMAN PLAY
    # if pygame.sprite.spritecollideany(human_player, enemies):
    #     # If so, then remove the player and stop the loop
    #     human_player.kill()
    # Update the player sprite based on user keypresses
    player.update(pressed_keys)
    human_player.update(pressed_keys)
      
    
    # scores = 
    # for player in players:
    #     if player.alive == False:
            # print(player.score)
            

    # Plot score distribution
    x = np.array(final_scores)
    
    rounded = np.rint(x)
    unique_elements, counts_elements = np.unique(rounded, return_counts=True)

    surf = bar_plot(unique_elements,counts_elements)
    screen.blit(surf, (600, 400))

 
      
    # Update enemy position
    enemies.update()
    


    # Update the display
    pygame.display.flip()
    
    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)
  

# Done! Time to quit.
pygame.quit()