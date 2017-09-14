#Main class that provides "scene" information 
#Similar to Unity's scene system

class SceneBase:
    def __init__(self):
        self.next = self
        
    def ProcessInput(self, events, pressed_keys):
        #Manage input here
        print ("Ah")
        
    def Update(self):
        #Called each frame
        print ("Ah2")
        
    def Render(self, screen):
        print ("AHHHH")
        
    def SwitchToScene(self, next_scene):
        self.next = next_scene
        
    def Terminate(self):
        self.SwitchToScene(None)
        
        
    