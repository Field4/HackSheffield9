MAX_TEMP = 30

class Environment:
    temperature = 15
    sunlight = 0.5

    plantGrowthFactor = 0

    plantLifeAvailable : float = 100

    def __init__(self, t : int, s : float, initialFood : int):
        self.temperature = t
        self.sunlight = s
        self.plantLifeAvailable = initialFood
        self.plantGrowthFactor = 1 + (self.temperature * self.sunlight) / MAX_TEMP

    def generatePlantLife(self):
        self.plantLifeAvailable =  self.plantLifeAvailable * self.plantGrowthFactor

    def eatPlants(self, amountEaten : int):
        self.plantLifeAvailable -= amountEaten
        if self.plantLifeAvailable <= 0: self.plantLifeAvailable = 1
    