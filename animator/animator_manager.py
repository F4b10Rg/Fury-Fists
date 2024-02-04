import pygame
from animator.animation import Animation
class Animator():
    def __init__(self,object) -> None:
        self.object= object
        self.animations={}
    def add_animation(self,name:str,animation:Animation):
        self.animations[name]=[False,animation]
    def update():
        pass
        
   