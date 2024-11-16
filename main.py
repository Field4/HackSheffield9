from environment import *
from animal import *
from producer import *
env = Environment(15, 0.5, 100, 100)
plant = Producer("plant", env, 100)
cow = Animal("cow", 100, 1)
cow.food_sources = [plant]


NUM_ITERATIONS = 10

for i in range(NUM_ITERATIONS):
    plant.grow()
    for animal in [cow]:
        animal.dieOrReproduce()
    
    print("Iteration n = " + str(i))
    print("Food available: " + str(plant.population))
    print("Number of cows: " + str(cow.population))