from environment import *
#from animal import *
from herbivore import *

env = Environment(15, 0.5)
cow = Herbivore(100, 0.75, 2)

for i in range(10):
    env.generatePlantLife()
    eaten = cow.dieOrReproduce(env.plantLifeAvailable)
    env.eatPlants(eaten)
    print("Iteration n = " + str(i))
    print("Food available: " + str(env.plantLifeAvailable))
    print("Number of cows: " + str(cow.population))