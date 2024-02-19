import pygame
from sys import exit
from scene_manager.scene_manager import Scene_manager
from characters.player import Player
from mouse.mouse import Mouse
from scenes.splash_scene import Splash_scene
from fightManager.fight import fight
pygame.init()
screen= pygame.display.set_mode((700,400))
clock = pygame.time.Clock()
icon= pygame.image.load("Resources/furyfist_icon.jpeg")
pygame.display.set_caption("FURY FIST")
pygame.display.set_icon(icon)
spriteGroup=pygame.sprite.Group()
manager=Scene_manager()

manager.actual_scene=Splash_scene(manager)
#mouse=Mouse(spriteGroup)


while True: 
    scene=manager.actual_scene    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        scene.events(event)
        

    manager.scene_update(screen)    
    pygame.display.update()
    clock.tick(60)