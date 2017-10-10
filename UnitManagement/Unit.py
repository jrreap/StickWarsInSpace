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

    # Position information
    xpos = 15
    ypos = 500
    laneid = 0

    # Image and Graphic Information
    imagepath = "Empty"
    
    
    def __init__(self, uclass, uid, udamage, uspeed, uhealth, upcost, umbt, urate, urange):
        self.unitclass = uclass
        self.unitid = uid
        self.damage = udamage
        self.speed = uspeed
        self.health = uhealth
        self.unitcost = upcost
        self.buildtime = umbt
        self.attackrate = urate
        self.unitrange = urange

        self.xpos = 0
        self.ypos = 0
        self.laneid = 0
        
    def DamageUnit(self, amount):
        self.health = self.health - amount
        
    def HealUnit(self, amount):
        self.health = self.health + amount

    def SetLaneID(self, lid):
        self.laneid = lid

    def SetPosition(self, x, y):
        self.xpos = x
        self.ypos = y;
