from typing import Any
import pygame
from pygame.sprite import Group
class Mouse(pygame.sprite.Sprite):
    def __init__(self, *groups:Group) -> None:
        super().__init__(*groups)
        pygame.mouse.set_visible(False)
        self.pos= (pygame.mouse.get_pos())
        self.image=pygame.image.load("Resources/UI/Cursor/cursor.png").convert_alpha()
        self.rect=self.image.get_rect()

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.pos= (pygame.mouse.get_pos())
        self.rect=self.image.get_rect(center=self.pos)
        return super().update(*args, **kwargs)