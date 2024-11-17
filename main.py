from environment import *
from animal import *
from producer import *
from plot import *
import streamlit as sl
env = Environment(1.2, 300)
plant = Producer("plant", env, 100)
moose = Animal("moose", 100, 1, 0.7, 2)
moose.food_sources = [plant]
animals = [moose]
plants = [plant]

data = {}

NUM_ITERATIONS = 15
DEATH_RATE = 1.5

def main():
    for i in range(NUM_ITERATIONS):
        output("Iteration t", i, data)
        output("plant population", plant.population, data)
        output("Moose population", moose.population, data)

        for plnt in plants:
            plnt.grow(env.plantGrowthRate * plnt.population)
        
        for animal in animals:
            demand = animal.getDemand()
            available = animal.food_sources[0].population * animal.feedstock_utilisation

            if available > demand:
                excess = available - demand
                # cap demand to 125% of required
                #excessRatio = min(animal.growthRate, excess/demand)
                # grow based on how much excess food there is
                animal.grow(animal.population*(animal.growthRate-1))
                # eat based on new damand
                animal.eat(min(available, demand*animal.growthRate))
            
            if available < demand:
                # kill amount based on amount missing per demand
                animal.cull(DEATH_RATE * (demand-available)/demand)



    return toFrame(data)

main()