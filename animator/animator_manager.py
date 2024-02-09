import pygame
from animator.animation import Animation
class Animator():
    def __init__(self) -> None:
        self.current_animation:Animation=None
        self.animations={}
        self.idle_name:str
    def add_animation(self,name:str,animation:Animation):
        self.animations[name]=[False,animation]
    def play_animation(self, animation_name):
        if animation_name in self.animations:
            self.current_animation = self.animations[animation_name][1]
            self.animations[animation_name][0]=True
        
    def load_animations(self,animations):
        for name,animation in animations.items():
            self.add_animation(name,animation)
    def verify_animations(self):
        for name,animation in self.animations.items():
            if int(animation[1].actual_image)==len(animation[1].frames)-1 and not animation[1].isACicle:
                animation[0]=False
                animation[1].reset_animation()
            
    def update(self) -> pygame.Surface:
        self.verify_animations()
        if self.current_animation and self.animations[self.current_animation.name][0]:
            return self.current_animation.play_animation()
        else:
            self.play_animation(self.idle_name)
            return self.animations[self.idle_name][1].play_animation() 
    def set_idle(self,name:str):
        self.idle_name=name