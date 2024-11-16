class Environment:
   
    

    def __init__(self, t : int, s : float, p: float, n: float):
        self.temperature = t
        self.sunlight = s
        self.plantLifeAvailable = p
        self.nutrients = n

    def getMaxPlantLife(self):
        return self.temperature * self.sunlight * self.nutrients
    

    def generatePlantLife(self):
        self.plantLifeAvailable = min(self.getMaxPlantLife(), self.plantLifeAvailable * self.temperature * self.sunlight)

    

    def eatPlants(self, amountEaten : int):
        self.plantLifeAvailable -= amountEaten
    
#newEnv = Environment(15, 0.5)
#print(newEnv.generatePlantLife())