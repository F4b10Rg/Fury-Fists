from scene_manager.scene import Scene
import pygame

class menu(Scene):
    def __init__(self, manager) -> None:
        super().__init__(manager)
        self.image=pygame.image.load("Resources\UI\FURY-FIST-PORTADA.jpg")
        self.rect=self.imagr.get_rect()
        