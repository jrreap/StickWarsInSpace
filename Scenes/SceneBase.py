# Main class that provides "scene" information and management methods
# Similar to Unity's scene system
# All scenes MUST inherit from this class for the system to work, think of each Scene as a differnt "view"
# or screen

class SceneBase:
    def __init__(self):
        self.next = self

    # This should be overridden in the child class and is where the input is handled
    def ProcessInput(self, events, pressed_keys):
        # Manage input here
        pass

    # This is called once per frame, this basically is used for stuff that is changing all the time
    def Update(self):
        # Called each frame
        pass

    # This is called to actually display the scene and the images/UI elements onto the screen
    def Render(self, screen):
        pass

    # This is called to switch to the next scene... usually this won't need to be changed
    def SwitchToScene(self, next_scene):

        if type(next_scene) == type(" "):
            components = next_scene.split('.')
            mod = __import__(components[0])
            for comp in components[1:]:
                mod = getattr(mod, comp)

            self.next = mod()
        else:
            self.next = next_scene

    # Called right before the scene is killed to clean up leftovers
    # If there are any high memory using variables, make sure to kill them in this method
    def Terminate(self):
        self.SwitchToScene(None)
