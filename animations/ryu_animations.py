from animator.animation import Animation
import pygame, os
Animations={}
def take_frames(path:str)->list:
    list_of_frames=[]
    files = os.listdir(path)

    for file in files:
        relative_path_file = os.path.join(path, file)
        list_of_frames.append(pygame.image.load(relative_path_file))
    return list_of_frames
def listar_archivos_en_directorio(root_dir):
    animations = {}
    for root, dirs, files in os.walk(root_dir):
        
        for dir_name in dirs:
            # Puedes procesar las subcarpetas aquí
            subfolder_path = os.path.join(root, dir_name)
            frames = take_frames(subfolder_path)  # Puedes llamar a una función para procesar las imágenes
            animations[dir_name] = Animation(dir_name,frames,.5)

    return animations
Animations=listar_archivos_en_directorio("Resources/ryu-animations")
print(Animations)

