from scene_manager.scene import Scene
from Controls.controls import Controls
from scenes.selection import selection_scene
from random import random
from sys import exit
import pygame

class dojo(Scene):
    def __init__(self, manager) -> None:
        super().__init__(manager)
        self.background=pygame.image.load("Resources\stages\dojo.jpg")
        self.arcade_img=pygame.image.load(r"Resources\UI\dojo-ui\blue.png").convert_alpha()
        self.history_img=pygame.image.load(r"Resources\UI\dojo-ui\green.png").convert_alpha()
        self.versus_img=pygame.image.load(r"Resources\UI\dojo-ui\red.png").convert_alpha()
        self.training_img=pygame.image.load(r"Resources\UI\dojo-ui\yellow.png").convert_alpha()
        self.sensei_img=pygame.image.load(r"Resources\UI\sensei.png").convert_alpha()
        self.font=self.font = pygame.font.Font(r'Resources\fonts\ProtestStrike-Regular.ttf', 15)
        self.titles=pygame.font.Font(r"Resources\fonts\ProtestRevolution-Regular.ttf",20)
        self.arcade_title=self.titles.render("ARCADE",False,'black').convert_alpha()
        self.arcade_title_rect=self.arcade_title.get_rect(center=(200,50))
        self.history_title=self.titles.render("HISTORY",False,'black').convert_alpha()
        self.history_title_rect=self.history_title.get_rect(center=(200,120))
        self.versus_title=self.titles.render("VERSUS",False,'black').convert_alpha()
        self.versus_title_rect=self.versus_title.get_rect(center=(200,190))
        self.training_title=self.titles.render("TRAINING",False,'black').convert_alpha()
        self.training_title_rect=self.training_title.get_rect(center=(200,270))
        self.sensei_text=self.font.render('sensei kiko: welcome to the dojo', False,'black').convert_alpha()
        self.sensei_text_rect=self.sensei_text.get_rect(x=100,y=350)
        self.sensei_rect=self.sensei_img.get_rect(bottom=400, centerx=600)
        self.arcade_mask=pygame.mask.from_surface(self.arcade_img)
        self.controls=Controls()
        self.masky=0
        self.actual_buttom=0
        self.selection_sound=pygame.mixer.Sound(r"Resources\sounds\608634__xxsamilytxx__selection.wav")
        self.dialogs=["welcome to the dojo",
                      "Con gran poder viene una gran responsabilidad"
                      ,"Do it or do not, but do not try","its not just fight",
                      "Do not settle into a form, adapt it and build your own, and let it grow, be like water",
                      "hakuna matata",
                      "combos are difficult but efective"]
    def events(self, event):
        self.controls.Update(event)
        if self.controls.DOWN and self.actual_buttom<3:
            
            self.selection_sound.play()
            self.actual_buttom+=1
            self.masky+=70
        elif  self.controls.DOWN and self.actual_buttom>=3:
            self.selection_sound.play()
            self.sensei_text=self.font.render(self.dialogs[int(random()*len(self.dialogs))], False,'black').convert_alpha()
            self.actual_buttom=0
            self.masky=0
        if self.controls.UP and self.actual_buttom<=0:
            self.selection_sound.play()
            self.actual_buttom=3
            self.masky=210
            self.sensei_text=self.font.render(self.dialogs[int(random()*len(self.dialogs))], False,'black').convert_alpha()
        elif  self.controls.UP and self.actual_buttom>0:
            self.selection_sound.play()
            
            self.actual_buttom-=1
            self.masky-=70
        
        if self.controls.A and self.actual_buttom==0:
           self.manager.actual_scene=selection_scene(self.manager)
        elif  self.controls.A and self.actual_buttom==1:
            print("history")
        elif  self.controls.A and self.actual_buttom==2:
            print("versus")
        elif  self.controls.A and self.actual_buttom==3:
            self.manager.actual_scene=selection_scene(self.manager)
        return super().events(event)
    def updateScene(self, screen):
        screen.blit(self.background,(0,0))
        screen.blit(self.arcade_img,(-60,0))
        screen.blit(self.history_img,(-60,70))
        screen.blit(self.versus_img,(-60,140))
        screen.blit(self.training_img,(-60,210))
        screen.blit(self.sensei_img,self.sensei_rect)
        screen.blit(self.sensei_text,self.sensei_text_rect)
        screen.blit(self.arcade_title,self.arcade_title_rect)
        screen.blit(self.history_title,self.history_title_rect)
        screen.blit(self.versus_title,self.versus_title_rect)
        screen.blit(self.training_title,self.training_title_rect)
        for point in self.arcade_mask.outline():
            x=point[0]-60
            y=point[1]+self.masky
            pygame.draw.circle(screen,(255,255,255,0),(x,y),2)
        return super().updateScene(screen)