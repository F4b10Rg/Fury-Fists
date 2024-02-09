from scene_manager.scene import Scene
class Scene_manager():
    def __init__(self) -> None:
        self.actual_scene:Scene
    def set_Scene(self,scene):
        self.actual_scene=scene
    def scene_update(self,screen):
         self.actual_scene.updateScene(screen)