from typing import Any
from animator.animator_manager import Animator
from animations.animations import get_animations
from Controls.controls import Controls
from pygame.sprite import Group
from random import randint as random
import pygame
class Character(pygame.sprite.Sprite):
    def __init__(self,character:str,*groups:Group) -> None:
        super().__init__(*groups)
        self.name:str=character
        self.health:int=250
        self.speed:int=1
        self.gravity=0
        self.jump_velocity = 10
        self.is_jumping=False
        self.combo={}
        #------------------------configuration---------------------------------------
        self.image:pygame.surface=pygame.image.load(f"Resources/{self.name}-animations/{self.name}-idle/{self.name}_idle_1.png")
        self.rect=self.image.get_rect(bottom=450)
        self.mask:pygame.mask=pygame.mask.from_surface(self.image)
        self.Animator=Animator()
        self.controls=Controls()
        self.load_character()
    def events(self,event):
        self.controls.Update(event)
        pass
    def update(self, *args: Any, **kwargs: Any) -> None:
        
        return super().update(*args, **kwargs)
    def get_damage(self,damage:int):
        self.health-=damage
        hit=[f"{self.name}-hit",f"{self.name}-hit2"]
        self.Animator.play_animation(animation_name=hit[random(0,1)])
        if(self.health<=0):
            pass
    def make_damage(self,damage):
        if sprite:= pygame.sprite.spritecollide(self,self.groups()[0],False):
            sprite.remove(self)
            if mask:=pygame.sprite.spritecollide(self,self.groups()[0],False,pygame.sprite.collide_mask):
                mask.remove(self)
                if len(mask)>0:
                    mask[0].get_damage(damage)
    def load_character(self):
        self.Animator.load_animations(get_animations(f"Resources/{self.name}-animations"))
        self.Animator.set_idle(f'{self.name}-idle')
        
        self.rect=self.image.get_rect(centery=300)