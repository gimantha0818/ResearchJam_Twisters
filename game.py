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


import pygame
import sys
import random

LIMBS = ["h_l", "h_r", "f_l", "f_r"]
COLORS = ["r", "b", "g"]
PHASES = ["set", "move"]

ourLimbs = []
new_cmd = None

initialized:bool = False    

def create_rand_limb_pos():
    idx_limb = random.randint(0, len(LIMBS)-1)
    idx_color = random.randint(0, len(COLORS)-1)
    return (LIMBS[idx_limb], COLORS[idx_color]) 

class Limb:
    def __init__(self, limb:str, initial_pos):
      self.limb = limb
      self.pos = initial_pos
      phase = "set"

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
        # Steps:
        # 1)Starting position
        if event.type == pygame.KEYDOWN:
            if (initialized == False):
                if event.key == pygame.K_SPACE:
                    print("Start Initialize!")
                    newLimbs = [Limb(limb=LIMBS[0], initial_pos=(1,2)), 
                                Limb(limb=LIMBS[1], initial_pos=(1,1)),
                                Limb(limb=LIMBS[2], initial_pos=(0,2)),
                                Limb(limb=LIMBS[3], initial_pos=(0,1))]
                    initialized = True
            continue
        
        # 2)Randomize new action -> instructions displayed on Screen UI. 
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    new_cmd = create_rand_limb_pos()
        
    if(initialized):
        # GET THE CURRENT MEASUREMNTS
        touched_plates = []
        
        
        # are all limbs were they are supposed to be
        for limb in ourLimbs:
            if (limb.phase == "set"):
                if(limb.pos in touched_plates):
                    print(f"{limb.limb} is correct")
                else:
                    print(f"{limb.limb} - ERROR")
                    
            elif(limb.phase == "move"):
                # see if it touches sth, then compare it to new_cmd
                pass


    # 4)Limb phase -> contact or no-contact. 10kPa threshold for contact detection. 

    # 5)Allowed to move and not allowed to move and error of action -> Disqualified. 

    # 6)End -> Passed!


    # Drawing code goes here
    screen.fill((0, 0, 0))  # Fill screen with black

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()

