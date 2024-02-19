from scene_manager.scene import Scene
import pygame
class fight(Scene):
    def __init__(self, manager,player_1,player_2,stage,sprite_group) -> None:
        super().__init__(manager)
        
        self.player_1=player_1
        self.player_2=player_2
        self.stage=stage
        self.sprite_group=sprite_group
        self.player_2.rect.x=500
        self.stage=pygame.image.load(stage)
        self.player_1_health_length = self.player_1.health
        self.player_2_health_length = self.player_2.health
        self.winner=None
        self.looser=None
        self.timer=120
        self.start_time= pygame.time.get_ticks()
        self.timer_font=pygame.font.Font(r"Resources\fonts\ProtestRevolution-Regular.ttf",60)
        self.timer_display= self.timer_font.render(f"{self.timer}",False,(181, 45, 38))
        self.timer_display_rect=self.timer_display.get_rect(center=(pygame.display.get_window_size()[0]/2,30))
    def events(self, event):
        self.player_1.events(event)
        #self.player_2.events(event)
        return super().events(event)
    def updateScene(self, screen):
        
        screen.blit(self.stage,(0,0))
       

        self.sprite_group.update()
        self.verify_player_orientation()
        self.sprite_group.draw(screen)
        self.update_player_health(screen)
        self.update_player_health(screen)
        remaining_seconds = self.timer_update()
        
        self.verify_winner(remaining_seconds)

        if self.winner!=None:

            winner=self.timer_font.render(f"{self.winner.name} WINS!!",False,(181, 45, 38))
            winner_rect=winner.get_rect(center=(350,200))
            screen.blit(winner,winner_rect)
       
        
        screen.blit(self.timer_display,self.timer_display_rect)
        return super().updateScene(screen)
    def verify_player_orientation(self):
        if self.player_1.rect.x>self.player_2.rect.x:
            self.player_1.image=pygame.transform.flip(self.player_1.image, True, False)
        else:
            self.player_1.image= self.player_1.image
        if self.player_2.rect.x>self.player_1.rect.x:
            self.player_2.image=pygame.transform.flip(self.player_2.image, True, False)
        else:
            self.player_2.image= self.player_2.image
    def verify_winner(self,time):
        remaining_seconds=time
        if remaining_seconds == 0:
            if self.player_1.health>self.player_2.health:
                self.winner=self.player_1
            elif self.player_2.health>self.player_1.health:
                 self.winner=self.player_2
        if not self.winner:
                
            if  self.player_1.health<=0:
                self.winner=self.player_2
                self.looser=self.player_1
                self.player_1.Animator.play_animation(animation_name=f"{self.player_1.name}-KO")

            elif self.player_2.health<=0:
                self.winner=self.player_1
                self.looser=self.player_2
                self.player_2.Animator.play_animation(animation_name=f"{self.player_2.name}-KO")

                
    def update_player_health(self,screen):
        if self.player_1.health >= 0:
            self.player_1_health_length = self.player_1.health
        if self.player_2.health >= 0: 
            self.player_2_health_length = self.player_2.health
        healt_lose=250-self.player_1.health
        pygame.draw.rect(screen,(181, 45, 38),((25+healt_lose),25,self.player_1.health,25))
        pygame.draw.rect(screen,(181, 45, 38),(425,25,self.player_2.health,25))
    def timer_update(self)->int:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time
        remaining_seconds = self.timer - elapsed_time // 1000
        if remaining_seconds<=0:
            remaining_seconds=0
        self.timer_display= self.timer_font.render(f"{remaining_seconds}",False,(181, 45, 38))
        return remaining_seconds