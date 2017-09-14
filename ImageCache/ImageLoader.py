import pygame
import os

#File that contains utility methods that help cache images so we don't waste
#memory resources

#Makes sure we are not creating multible copies of the same image
_image_library = {}
def GetImage(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image