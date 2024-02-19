from scene_manager.scene import Scene
from Controls.controls import Controls
from scenes.dojo import dojo
from sys import exit
import pygame

class menu(Scene):
    def __init__(self, manager) -> None:
        super().__init__(manager)
        self.font = pygame.font.Font(r'Resources\fonts\ProtestStrike-Regular.ttf', 70)
        self.buttom_font= pygame.font.Font(r'Resources\fonts\ProtestRevolution-Regular.ttf', 30)
        self.image=pygame.image.load(r"Resources\UI\dojo.jpeg")
        midx=pygame.display.get_window_size()[0]/2
        midy=pygame.display.get_window_size()[1]/2
        self.title= self.font.render('FURY FIST', False,'white').convert_alpha()
        self.buttom_start=self.buttom_font.render('START', False,'black').convert_alpha()
        self.buttom_start_rect=self.buttom_start.get_rect(center=(midx,300))
        self.buttom_settings=self.buttom_font.render('SETTINGS', False,'black').convert_alpha()
        self.buttom_settings_rect=self.buttom_settings.get_rect(center=(midx,340))
        self.buttom_quit=self.buttom_font.render('QUIT', False,'black').convert_alpha()
        self.buttom_quit_rect=self.buttom_quit.get_rect(center=(midx,380))
        self.title_rect=self.title.get_rect(centerx=midx)
        self.rect=self.image.get_rect(center=(midx,midy))
        self.controls=Controls()
        self.selection_sound=pygame.mixer.Sound(r"Resources\sounds\608634__xxsamilytxx__selection.wav")
        self.actual_buttom=0
        
    def events(self, event):
        self.controls.Update(event)
        
        if self.controls.DOWN and self.actual_buttom<2:
            self.selection_sound.play()
            self.actual_buttom+=1
        elif  self.controls.DOWN and self.actual_buttom>=2:
            self.selection_sound.play()
            self.actual_buttom=0
        if self.controls.UP and self.actual_buttom<=0:
            self.selection_sound.play()
            self.actual_buttom=2
        elif  self.controls.UP and self.actual_buttom>0:
            self.selection_sound.play()
            self.actual_buttom-=1
            
        if self.actual_buttom==0:
            self.buttom_start=self.buttom_font.render('START', False,'white').convert_alpha()
            self.buttom_settings=self.buttom_font.render('SETTINGS', False,'black').convert_alpha()
            self.buttom_quit=self.buttom_font.render('QUIT', False,'black').convert_alpha()
        elif self.actual_buttom==1:
            self.buttom_start=self.buttom_font.render('START', False,'black').convert_alpha()
            self.buttom_settings=self.buttom_font.render('SETTINGS', False,'white').convert_alpha()
            self.buttom_quit=self.buttom_font.render('QUIT', False,'black').convert_alpha()
        elif self.actual_buttom==2:
            self.buttom_start=self.buttom_font.render('START', False,'black').convert_alpha()
            self.buttom_settings=self.buttom_font.render('SETTINGS', False,'black').convert_alpha()
            self.buttom_quit=self.buttom_font.render('QUIT', False,'white').convert_alpha()
        
        if self.controls.A and self.actual_buttom==0:
           self.manager.actual_scene=dojo(self.manager)
           pygame.mixer.music.stop()
        elif  self.controls.A and self.actual_buttom==1:
            print("settings start")
        elif  self.controls.A and self.actual_buttom==2:
             pygame.quit()
             exit()
        return super().events(event)

    def updateScene(self, screen):
        screen.blit(self.image,self.rect)
        screen.blit(self.title,self.title_rect)
        screen.blit(self.buttom_start,self.buttom_start_rect)
        screen.blit(self.buttom_settings,self.buttom_settings_rect)
        screen.blit(self.buttom_quit,self.buttom_quit_rect)
        