import pygame  
import sys  
from  possision import possision
from shout import shout
# Position class with movement functionality  

# Initialize Pygame  
pygame.init()  

# Constants  
WIDTH, HEIGHT = 800, 600  
WHITE = (255, 255, 255)  
BLUE = (0, 0, 255)
RED=(255,0,0)

# Set up the display  
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Movement with Pygame")  

# Create a Position instance  
player = possision(100,100,WIDTH,HEIGHT/2,10)  
shuts=list()
# Game loop  
while True:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            sys.exit()  

    # Get the keys pressed  
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_UP]:  
        player.move('up')  
    if keys[pygame.K_DOWN]:  
        player.move('down')  
    if keys[pygame.K_LEFT]:  
        player.move('left')  
    if keys[pygame.K_RIGHT]:  
        player.move('right')  
    if keys[pygame.K_SPACE]:  
        shuts.append(shout(player.get_x(),player.get_y(),WIDTH,HEIGHT,player.dir)) 
    screen.fill(WHITE)  

    # Draw the player (a rectangle)  
    pygame.draw.rect(screen, BLUE, (player.get_x(), player.get_y(), 50, 50))
    for s1 in shuts:
        if s1.move():
            pygame.draw.rect(screen, RED, (s1.get_x(), s1.get_y(),10 , 10))
        else:
            shuts.remove(s1)
            pygame.draw.circle(screen,(0,255,0),(100,100),90)
    # Update the display  
    pygame.display.flip()  

    # Frame rate  
    pygame.time.Clock().tick(60)