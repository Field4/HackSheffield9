class Environment:
    temperature = 15
    sunlight = 0.5

    plantLifeAvailable = 100

    def __init__(self, t : int, s : float):
        self.temperature = t
        self.sunlight = s

    def generatePlantLife(self):
        self.plantLifeAvailable =  self.plantLifeAvailable * self.temperature * self.sunlight

    def eatPlants(self, amountEaten : int):
        self.plantLifeAvailable -= amountEaten
    
newEnv = Environment(15, 0.5)
print(newEnv.generatePlantLife())