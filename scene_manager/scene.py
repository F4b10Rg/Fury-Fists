
from abc import abstractmethod
class Scene():
    def __init__(self,manager) -> None:
        self.manager=manager
        self.objects=[]
        self.near_scenes=[]
    @abstractmethod 
    def updateScene(self,screen):
        pass
    @abstractmethod 
    def events(self,event):
        pass
    @abstractmethod 
    def load(self):
        return self
    def passObject():
        pass
    def saveScene():
        pass