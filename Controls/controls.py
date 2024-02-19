import pygame
class Controls():
    def __init__(self) -> None:
        self.UP=False
        self.DOWN=False
        self.RIGHT=False
        self.LEFT=False
        self.SPACE=False
        self.A=False
        self.S=False
        self.Z=False
        self.X=False
        #-------special
        self.ENTER=False
    def Update(self,event):
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                self.UP=True
            if event.key==pygame.K_DOWN:
                self.DOWN=True
            if event.key==pygame.K_RIGHT:
                self.RIGHT=True
            if event.key==pygame.K_LEFT:
                self.LEFT=True
            if event.key==pygame.K_SPACE:
                self.SPACE=True
            if event.key==pygame.K_a:
                self.A=True
            if event.key==pygame.K_s:
                self.S=True
            if event.key==pygame.K_z:
                self.Z=True
            if event.key==pygame.K_x:
                self.X=True
            if event.key==pygame.K_RETURN:
                self.ENTER=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                self.UP=False
            if event.key==pygame.K_DOWN:
                self.DOWN=False
            if event.key==pygame.K_RIGHT:
                self.RIGHT=False
            if event.key==pygame.K_LEFT:
                self.LEFT=False
            if event.key==pygame.K_SPACE:
                self.SPACE=False
            if event.key==pygame.K_a:
                self.A=False
            if event.key==pygame.K_s:
                self.S=False
            if event.key==pygame.K_z:
                self.Z=False
            if event.key==pygame.K_x:
                self.X=False
            if event.key==pygame.K_RETURN:
                self.ENTER=False
    def get_controls(self)->dict:
        controls_right=[self.UP,self.DOWN,self.RIGHT,self.LEFT]
        controls_left=[self.SPACE,self.A,self.S,self.Z,self.X]
        return {'right controls':controls_right,
                'left controls':controls_left}