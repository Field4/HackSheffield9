class Environment:

    def __init__(self, t : int, s : float, n: float):
        self.temperature = t
        self.sunlight = s
        self.nutrients = n

    def getMaxPlantLife(self):
        return self.temperature * self.sunlight * self.nutrients
    
    
#newEnv = Environment(15, 0.5)
#print(newEnv.generatePlantLife())