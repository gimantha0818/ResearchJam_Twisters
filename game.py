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
LIMBS_TEXT = ["Left Hand", "Right Hand", "Left Foot", "Right Foot"]

COLORS = ["r", "b", "g"]
COLORS_TEXT = ["Red", "Blue", "Green"]

PHASES = ["set", "move"]

RED = (255, 0, 0)
GREEN = (0, 255, 0)

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

# Spins the wheel and returns a random limb and color
def create_rand_limb_pos():

    # Randomly select a limb and color
    idx_limb = random.randint(0, len(LIMBS)-1)
    idx_color = random.randint(0, len(COLORS)-1)
    print(f"Selected Limb: {LIMBS[idx_limb]}, Color: {COLORS[idx_color]}")

    # Starting angle for the spinner
    angle = 15

    # Adjusts angle based on the selected limb and color
    if LIMBS[idx_limb] == "h_l":
        angle += 180
    elif LIMBS[idx_limb] == "f_l":
        angle += 90
    elif LIMBS[idx_limb] == "f_r":
        angle += 270

    if COLORS[idx_color] == "r":
        angle += 45
    elif COLORS[idx_color] == "g":
        angle += 67.5

    # Backs up arrow before spin so that it lands in the right position
    angle -= 118

    # Load and display an image at the center of the screen
    spinner_image = pygame.image.load("assets/spinner.jpg")
    spinner_rect = spinner_image.get_rect(center=(screen_width // 2, screen_height // 2))
    arrow_image = pygame.image.load("assets/arrow.png")

    # Set counter and initial speed for the spinner
    count = 200
    speed = 5

    while count > 0:
        # Re-draw the arrow
        rotated_arrow = pygame.transform.rotate(arrow_image, angle)
        rotated_rect = rotated_arrow.get_rect(center=spinner_rect.center)

        # Draw evreything to secreen
        screen.fill((0, 0, 0))  # Fill screen with black
        screen.blit(spinner_image, spinner_rect)  # Draw the arrow on top of the spinner
        screen.blit(rotated_arrow, rotated_rect)
        pygame.display.flip()

        # Change the angle and speed
        angle -= speed
        speed -= 0.02
        count -= 1
        pygame.time.delay(5)

    pygame.time.delay(1000)  # Delay to show the spinner for a second
    return (LIMBS[idx_limb], COLORS[idx_color]) 

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
            if event.key == pygame.K_SPACE:
                if (initialized == False):
                    print("Start Initialize!")
                    newLimbs = [Limb(limb=LIMBS[0], initial_pos=(1,2)), 
                                Limb(limb=LIMBS[1], initial_pos=(1,1)),
                                Limb(limb=LIMBS[2], initial_pos=(0,2)),
                                Limb(limb=LIMBS[3], initial_pos=(0,1))]
                    initialized = True
            
            elif(event.key == pygame.K_RETURN):
                # 2)Randomize new action -> instructions displayed on Screen UI. 
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

    # Draws the rectangles to display the tile state
    if(initialized):
        for i in range(6):
            for j in range(3):

                # Draw instructions at the top
                font = pygame.font.SysFont(None, 36)
                if new_cmd is not None:
                    limb_text = LIMBS_TEXT[LIMBS.index(new_cmd[0])]
                    color_text = COLORS_TEXT[COLORS.index(new_cmd[1])]
                    text = f"{limb_text} on {color_text}"
                else:
                    text = "Press ENTER to spin!"

                text_surface = font.render(text, True, (255, 255, 255))
                screen.blit(text_surface, (screen_width // 2 - text_surface.get_width() // 2, 50))

                # Draw grid of rectangles
                rect = pygame.Rect(i * 100 + 110, j * 100 + 200, 80, 80)
                touched_plates = [(0,0),(0,1),(1,1),(2,3)]
                # Color the tiles if they are touched or not
                if (i,j) in touched_plates:
                    pygame.draw.rect(screen, GREEN, rect)
                else:
                    pygame.draw.rect(screen, RED, rect)
    else:
        # Display the initial message
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render("Press SPACE to initialize!", True, (255, 255, 255))
        screen.blit(text_surface, (screen_width // 2 - text_surface.get_width() // 2, screen_height // 2 - 20))


    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()
