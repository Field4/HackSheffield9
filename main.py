from environment import *
from animal import *
from producer import *
env = Environment(4, 0.5, 3000)
plant = Producer("plant", env, 2500)
cow = Animal("cow", 1000, 1, 0.8)
cow.food_sources = [plant]
animals = [cow]

NUM_ITERATIONS = 15

for i in range(NUM_ITERATIONS):
    print("Iteration n = " + str(i))
    print("Food available: " + str(plant.population))
    print("Number of cows: " + str(cow.population))
    plant.grow()
    for animal in animals:
        animal.dieOrReproduce()
    