import pygame

# Main class utilized to manage "camera" position and screen rendering
# Used by a lot of classes to correctly render objects on screen
# DO NOT TOUCH WITHOUT CONSULTING JAYDON

class Camera(object):

    cx = 0
    cy = 0

    # Method to set the Camera offset values used in screen rendering
    @classmethod
    def SetCameraOffset(cls, xoff, yoff):

        # Make sure these values are not below 0
        if xoff >= 0:
            cls.cx = xoff
        else:
            print("[ERROR] Whoa there, can't have the camera offset values be below 0")
            print("[INFO] Resetting ")
            cls.cx = 0

        if yoff >= 0:
            cls.cy = yoff
        else:
            print("[ERROR] Whoa there, can't have the camera offset values be below 0")
            print("[INFO] Resetting ")
            cls.cy = 0

    # Returns a position that is rendered in account with the camera offset values
    @classmethod
    def RenderPosition(cls, width, height):
        x = width - cls.cx
        y = height - cls.cy

        return x, y

