from environment import *
class Producer:
    population: int = 0
    environment: Environment
    name: str
    def __init__(self, name: str, env:Environment, pop: float):
        self.name = name
        self.population = pop
        self.environment = env
    
    def grow(self):
        env = self.environment
        self.population = min(env.getMaxPlantLife(), int(self.population * env.sunlight * env.temperature))