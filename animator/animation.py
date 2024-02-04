import pygame
class Animation():
    def __init__(self,name:str,list_of_frames:list,delay:float,isACicle:bool) -> None:
        self.name:str=name
        self.frames:list=list_of_frames
        self.actual_image:int=0
        self.delay:float=delay
        self.isACicle=isACicle
        clock=pygame.time.Clock()
        self.dt=clock.tick(60)/1000
    def play_animation(self)->pygame.image:
        self.dt+=.1
        if self.dt>=self.delay:
            self.actual_image+=1
            self.dt=0
        self.actual_image = min(self.actual_image, len(self.frames) - 1)  # Limitar al máximo valor posible
        if self.actual_image>=len(self.frames):
            if self.isACicle:
                print("entro aca")
                self.actual_image=0
            else:
                pass    
            
        return self.frames[int(self.actual_image)]