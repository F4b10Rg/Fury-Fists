from typing import Any
import pygame
from animations.ryu_animations import Animations
from animator.animator_manager import Animator
from Controls.controls import Controls
from pygame.sprite import Group
class Ryu(pygame.sprite.Sprite):
    def __init__(self, *groups:Group) -> None:
        super().__init__(*groups)
        
        self.speed=1

        self.combo={}
        self.Animator=Animator()
        self.Animator.load_animations(Animations)
        self.Animator.set_idle('ryu-idle')
        self.actual_image=pygame.image.load("Resources/ryu-animations/ryu-idle/ryu_idle_1.png")
        self.image=self.actual_image
        self.rect=self.image.get_rect(centery=300)
        self.controls=Controls()
        self.gravity=0
        self.jump_velocity = 10
        Animations["ryu-blocking"].isACicle=True
        Animations["ryu-crounch"].isACicle=True
        Animations["ryu-jump"].delay=.6
    def update(self, *args: Any, **kwargs: Any) -> None:
        self.gravity+=1
        self.rect.y+=self.gravity
        if self.rect.centery>=300: self.rect.centery=300
        if self.controls.SPACE and self.rect.centery==300:
            self.gravity = -20 
            self.Animator.play_animation(animation_name="ryu-jump")
        if self.controls.RIGHT:
            self.rect.centerx+=self.speed
            self.Animator.play_animation(animation_name='ryu-walking')
        elif self.controls.LEFT:
            self.rect.centerx-=self.speed
            self.Animator.play_animation(animation_name='ryu-walking')
        if self.controls.UP:
            self.Animator.play_animation(animation_name="ryu-blocking")
        elif self.controls.DOWN:
            self.Animator.play_animation(animation_name="ryu-crounch")
        
        self.image=self.Animator.update()
        
        
        
        

    
    
    