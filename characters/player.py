from typing import Any
import pygame
from pygame.sprite import Group
from characters.character import Character
class Player(Character):
    def __init__(self,character:str,*groups:Group) -> None:
        super().__init__(character,*groups)

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.gravity+=1
        self.rect.y+=self.gravity
        
        if self.rect.centery>=300: 
            self.rect.centery=300
            self.is_jumping=False 
        if self.controls.SPACE and self.rect.centery==300:
            self.gravity = -20 
            self.is_jumping=True
            self.Animator.play_animation(animation_name=f"{self.name}-jump")
        if self.controls.RIGHT and not self.is_jumping:
            self.rect.centerx+=self.speed
            self.Animator.play_animation(animation_name=f'{self.name}-walking')
        elif self.controls.LEFT and not self.is_jumping :
            self.rect.centerx-=self.speed
            self.Animator.play_animation(animation_name=f'{self.name}-walking')
        elif self.controls.UP:
            self.Animator.play_animation(animation_name=f"{self.name}-blocking")
        elif self.controls.DOWN:
            self.Animator.play_animation(animation_name=f"{self.name}-crounch")
        if self.controls.A:
            self.Animator.play_animation(animation_name=f"{self.name}-left-punch")
            self.make_damage(1)
        if self.controls.S or self.controls.Z:
            self.Animator.play_animation(animation_name=f"{self.name}-mh-punch")
            self.make_damage(5)
        if self.is_jumping and self.controls.LEFT:
            self.rect.centerx-=self.speed+5
            self.Animator.play_animation(animation_name=f"{self.name}-jump-foward")
        if self.is_jumping and self.controls.RIGHT:
            self.rect.centerx+=self.speed+5
            self.Animator.play_animation(animation_name=f"{self.name}-jump-foward")
        self.image=self.Animator.update()
        
        self.mask=pygame.mask.from_surface(self.image)