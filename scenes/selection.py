from scene_manager.scene import Scene
from Controls.controls import Controls
from fightManager.fight import fight 
from characters.player import Player
from characters.character import Character
import pygame
class selection_scene(Scene):
    def __init__(self, manager) -> None:
        super().__init__(manager)
        self.background= pygame.image.load(r"Resources\UI\mountains.jpeg")
        self.player_1=None
        self.player_2=None
        self.spriteGroup=pygame.sprite.Group()
        self.ryu_select=pygame.image.load(r"Resources\UI\selection_UI\ryu-selection.png")
        self.ryu_select_rect=self.ryu_select.get_rect(center=(100,100))
        self.ken_select=pygame.image.load(r"Resources\UI\selection_UI\ken-selection.png")
        self.ken_select_rect=self.ken_select.get_rect(center=(185,100))
        self.chun_lee_selection=pygame.image.load(r"Resources\UI\selection_UI\chun-lee-selection.png")
        self.chun_lee_selection_rect=self.chun_lee_selection.get_rect(center=(270,100))
        self.blanka_selection=pygame.image.load(r"Resources\UI\selection_UI\blanka-selection.png")
        self.blanka_selection_rect=self.blanka_selection.get_rect(center=(355,100))
        self.dee_jay_selection=pygame.image.load(r"Resources\UI\selection_UI\dee-jay-selection.png")
        self.dee_jay_selection_rect=self.dee_jay_selection.get_rect(center=(440,100))
        self.honda_selection=pygame.image.load(r"Resources\UI\selection_UI\honda-selection.png")
        self.honda_selection_rect=self.honda_selection.get_rect(center=(525,100))
        self.guille_selection=pygame.image.load(r"Resources\UI\selection_UI\guille-selection.png")
        self.guille_selection_rect=self.guille_selection.get_rect(center=(610,100))
        self.font=pygame.font.Font(r"Resources\fonts\ProtestRevolution-Regular.ttf",60)
        self.select_mask=pygame.mask.from_surface(self.ryu_select)
        self.maskx=self.ryu_select_rect.x
        self.masky=self.ryu_select_rect.y
        self.selection={
            "ryu":[self.ryu_select_rect.x,self.ryu_select_rect.y],
            "ken":[self.ken_select_rect.x,self.ken_select_rect.y],
            "chun-lee":[self.chun_lee_selection_rect.x,self.chun_lee_selection_rect.y],
            "blanka":[self.blanka_selection_rect.x,self.blanka_selection_rect.y],
            "dee-jay":[self.dee_jay_selection_rect.x,self.dee_jay_selection_rect.y],
            "honda":[self.honda_selection_rect.x,self.honda_selection_rect.y],
            "guile":[self.guille_selection_rect.x,self.guille_selection_rect.y]
        }
        self.controls=Controls()
        self.actual_selection=0
        self.character="ryu"
    def events(self, event):
        self.controls.Update(event)
        selection=list(self.selection.items())
        
        
        if self.controls.RIGHT:
            if self.actual_selection== len(selection)-1:
                self.actual_selection=0
            else:
                
                self.actual_selection+=1
            self.character,pos=selection[self.actual_selection]
            self.maskx=pos[0]
            self.masky=pos[1]
        if self.controls.LEFT:
            if self.actual_selection==0:
                self.actual_selection=len(selection)-1
            else:
                self.actual_selection-=1
            self.character,pos=selection[self.actual_selection]
            self.maskx=pos[0]
            self.masky=pos[1]
        if self.controls.ENTER:
                if not self.player_1 and not self.player_2:
                    self.player_1=Player(self.character,self.spriteGroup)
                elif not self.player_2:
                    self.player_2=Player(self.character,self.spriteGroup)
                else:
                    
                    self.manager.actual_scene=fight(self.manager,self.player_1,self.player_2,"Resources\stages\dojo.jpg",self.spriteGroup)
        
        return super().events(event)
    def updateScene(self, screen):
        
        screen.blit(self.background,(0,0))
        screen.blit(self.ryu_select,self.ryu_select_rect)
        screen.blit(self.ken_select,self.ken_select_rect)
        screen.blit(self.chun_lee_selection,self.chun_lee_selection_rect)
        screen.blit(self.blanka_selection,self.blanka_selection_rect)
        screen.blit(self.dee_jay_selection,self.dee_jay_selection_rect)
        screen.blit(self.honda_selection,self.honda_selection_rect)
        screen.blit(self.guille_selection,self.guille_selection_rect)
        if not self.player_1:
            for point in self.select_mask.outline():
                x=point[0]+self.maskx
                y=point[1]+self.masky
                pygame.draw.circle(screen,'blue',(x,y),2)
        elif not self.player_2:
            for point in self.select_mask.outline():
                x=point[0]+self.maskx
                y=point[1]+self.masky
                pygame.draw.circle(screen,'red',(x,y),2)
        else:
            star_game=self.font.render("ENTER TO START!",False,(181, 45, 38))
            start_rect=star_game.get_rect(center=(350,200))
            screen.blit(star_game,start_rect)
        return super().updateScene(screen)