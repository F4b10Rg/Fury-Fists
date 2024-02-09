import pygame
from sys import exit
from scene_manager.scene_manager import Scene_manager
from characters.ryu import Ryu
from mouse.mouse import Mouse
pygame.init()

screen= pygame.display.set_mode((700,400))
clock = pygame.time.Clock()
icon= pygame.image.load("Resources/furyfist_icon.jpeg")
pygame.display.set_icon(icon)
spriteGroup=pygame.sprite.Group()
ryu =Ryu(spriteGroup)
mouse=Mouse(spriteGroup)
bck=pygame.image.load("Resources\stages\space.jpg")


while True:

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        ryu.controls.Update(event)
    
    screen.blit(bck,(0,-300))    
    spriteGroup.draw(screen)
    spriteGroup.update()
    pygame.display.update()
    clock.tick(60)