from scene_manager.scene import Scene
from scenes.menu import menu
import pygame
class Splash_scene(Scene):
    def __init__(self,manager) -> None:
        super().__init__(manager)
        self.image=pygame.image.load(r"Resources\UI\fabio_logo.jpg").convert()
        self.image_rect=self.image.get_rect(center=(pygame.display.get_window_size()[0]/2,(pygame.display.get_window_size()[1]/2)))
        self.dt= pygame.time.Clock().tick(60)/1000
        self.timer=0 
        self.music=pygame.mixer.music
        self.music.load(r"Resources\sounds\722859__audiocoffee__futuristic-sci-fi-cinematic-loop-ver.wav")
        self.music.play(3)
        
        self.alpha=0
    def updateScene(self,screen):
        screen.fill('black')
        self.animate_splah()
        
        if self.timer>=3:
            self.manager.actual_scene=menu(self.manager)
        
        screen.blit(self.image,self.image_rect)
    def events(self,event):
        if event.type == pygame.KEYDOWN:
            self.manager.actual_scene=menu(self.manager)
    
    def animate_splah(self):
        self.timer+=self.dt
        if self.timer<=1.5:
            self.alpha+=1
            self.image.set_alpha(self.alpha)
           
        else:
            self.alpha-=1
            self.image.set_alpha(self.alpha)
            
        