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

        # 3600

        # Make sure these values are not below 0
        if xoff >= 0 or xoff <= 2350:
            cls.cx = xoff
        else:
            print("[ERROR] Offset values can't be less than 0 or greater than 3600!")
            print("[INFO] Resetting ")

            if xoff < 0:
                cls.cx = 0
            else:
                cls.cx = 3600

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

    @classmethod
    # Returns a position that is rendered for the UI
    def RenderUIPosition(cls, width, height):
        x = width
        y = height

        return x, y

    @classmethod
    def GetXOffset(cls):
        return cls.cx

    @classmethod
    def GetYOffset(cls):
        return cls.cy

