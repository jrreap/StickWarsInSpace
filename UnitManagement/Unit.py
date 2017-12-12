from UnitAnimations.Walk import Walk
#Main class for managing and adjusting unit and unit information
#Should be linked to every unit on the game screen

class Unit():

    # Class Information
    unitclass = "Empty"
    unitid = 0

    # Unit Stats
    damage = 0
    speed = 0
    health = 0
    unitcost = 0
    buildtime = 0
    attackrate = 0
    unitrange = 0
    attacking = False
    xpos = 0
    ypos = 0

    # Image and Graphic Information
    imagepath = "Empty"
    
    
    def __init__(self,stats,imagefolder,lane = 0):
        self.health = stats[0]
        self.damage = stats[1]
        self.speed = stats[2]
        self.attackrate = stats[3]
        self.unitrange = stats[4]
        self.unitcost = stats[5]
        self.buildtime = stats[6]
        self.imagepath = "UnitAnimations/+"imagefolder+"/"
        self.laneid = lane

        self.animate = Walk()
        
    def DamageUnit(self, amount):
        self.health = self.health - amount
        
    def HealUnit(self, amount):
        self.health = self.health + amount

    def SetLaneID(self, lid):
        self.laneid = lid

    def GetPositionX(self):
        return self.xpos

    def GetPositionY(self):
        return self.ypos

    def GetSpeed(self):
        return self.speed

    def SetPosition(self, x, y):
        self.xpos = x
        self.ypos = y
