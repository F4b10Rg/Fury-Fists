from typing import Any
import pygame
from pygame.sprite import Group
from characters.character import character
from animations.animations import ryu_animations as Animations
class Ryu(character):
    def __init__(self,*groups:Group) -> None:
        super().__init__(*groups,)
        self.name="Ryu"
        self.Animator.load_animations(Animations)
        self.Animator.set_idle('ryu-idle')
        self.actual_image=pygame.image.load("Resources/ryu-animations/ryu-idle/ryu_idle_1.png")
        self.image=self.actual_image
        self.rect=self.image.get_rect(centery=300)
        self.mask=pygame.mask.from_surface(self.image)
        Animations["ryu-blocking"].isACicle=True
        Animations["ryu-crounch"].isACicle=True
        Animations["ryu-crounch"].isACicle=True
        Animations["ryu-jump"].delay=.6
        Animations["ryu-jump-foward"].delay=.7
        self.is_jumping=False
    def update(self, *args: Any, **kwargs: Any) -> None:
        pass
        
        
        
        
        
        
        

    
    
    