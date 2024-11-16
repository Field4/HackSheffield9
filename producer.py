from environment import *
class Producer:
    population: float = 0
    environment: Environment
    name: str
    def __init__(self, name: str, env:Environment, pop: float):
        self.name = name
        self.population = pop
        self.environment = env
    
    def grow(self):
        env = self.environment
        self.population = min(env.getMaxPlantLife(), self.population * env.nutrients * env.sunlight * env.temperature)
    
    def __toString__(self):
        return self.name
