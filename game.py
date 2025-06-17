# **Stepscan Live**

# Pressure data. Serial ID of the tile can be identified from the API. 
# Install stepscanlive.msi
# DAQ.exe can be interfaced to the UI (C++ based) in Example Apps folder. 

# DAQ.exe has two configutation files 
# 1)DAQ.confiq is autogrenerated by stepscan live. 
# 2)Tilelookup -> serialnumbers.dat (the API will need the 12 tile associated lookup files). 
# So you would use the API in a loop. 

# E.g.: 
# while(TRUE) 
# api.read(data)

# titleReader.read()

# Colours:
# Red, Green and Blue

# split the two tile array to 3 colours. 720x240 dimensional block. 
# 1 player only. Get from point A to point B. 

# Steps:
# 1)Starting position

# 2)Randomize new action -> instructions displayed on Screen UI. 

# 3)Check correctness. 

# 4)Limb phase -> contact or no-contact. 10kPa threshold for contact detection. 

# 5)Allowed to move and not allowed to move and error of action -> Disqualified. 

# 6)End -> Passed!


import pygame
import sys
import random

LIMBS = ["h_l", "h_r", "f_l", "f_r"]
COLORS = ["r", "b", "g"]

# Initialize pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basic Pygame Loop")

# Set up the clock for framerate control
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Drawing code goes here
    screen.fill((0, 0, 0))  # Fill screen with black

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()

def create_rand_limb_pos():
    idx_limb = random.randint(0, len(LIMBS)-1)
    idx_color = random.randint(0, len(COLORS)-1)
    return (LIMBS[idx_limb], COLORS[idx_color]) 
