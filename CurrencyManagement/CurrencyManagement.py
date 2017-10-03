"""
Currency System: start currency is the amount that you start with for level one
each method that has 'cost' in it is how much the unit cost
each method that has 'profit' in it is how much you gain when you kill one of those units
"""

class Currency:
    def StartCurrency():
        currency = 200
        return currency
    def HorseRifleBlastercost(unitcost, currency):
        currency = currency - unitcost
        return currency
    def HorseRifleBlasterprofit(currency):
        currency = currency + (random.randint(1,5) * 25)
        return currency
    def Planecost(unitcost, currency):
        currency = currency - unitcost
        return currency
    def Planeprofit(currency):
        currency = currency + (random.randint(1,5) * 100)
        return currency
    def RifleBlastercost(unitcost, currency):
        currency = currency - unitcost
        return currency
    def RifleBlasterprofit(currency):
        currency = currency + (random.randint(1,5) * 50)
        return currency
    def SpaceRaidercost(unitcost, currency):
        currency = currency - unitcost
        return currency
    def SpaceRaiderprofit(currency):
        currency = currency + (random.randint(1,5) * 25)
        return currency
    def Tankcost(unitcost, currency):
        currency = currency - unitcost
        return currency
    def Tankprofit(currency):
        currency = currency + (random.randint(1,5) * 100)
        return currency
    def Turretcost(unitcost, currency):
        currency = currency - unitcost
        return currency
    def Turretprofit(currency):
        currency = currency + (random.randint(1,5) * 100)
        return currency
