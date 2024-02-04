import pygame
from sys import exit
from   Controls import controls
pygame.init()

screen= pygame.display.set_mode((600,600))
clock = pygame.time.Clock()
icon= pygame.image.load("Resources/furyfist_icon.jpeg")
pygame.display.set_icon(icon)
control=controls.Controls()
while True:
    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        control.Update(event)
        
    print(control.get_controls())
    pygame.display.update()
    clock.tick(60)