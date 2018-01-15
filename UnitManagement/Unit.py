from UnitAnimations.Walk import Walk
#Main class for managing and adjusting unit and unit information
#Should be linked to every unit on the game screen

class Unit():
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
    
    def __init__(self,stats,lane = 0):
        self.health = stats[1]
        self.damage = stats[2]
        self.speed = stats[3]
        self.attackrate = stats[4]
        self.unitrange = stats[5]
        self.unitcost = int(stats[6])
        self.buildtime = stats[7]
        self.imagepath = "UnitAnimations/"+stats[0]+"/"
        self.laneid = lane

        self.width = stats[8]
        self.hight = stats[9]
        self.animate = Walk(self.width,stats[10])
        
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
