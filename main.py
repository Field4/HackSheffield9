from environment import *
from animal import *
from producer import *

import streamlit as st
import pandas as pd

env = Environment(4, 0.5, 3000)
plant = Producer("plant", env, 2500)
cow = Animal("cow", 1000, 1, 0.8)
cow.food_sources = [plant]
animals = [cow]

NUM_ITERATIONS = 40 

plant_pop = []
cow_pop = []
dplant = []
dcow = []


for i in range(NUM_ITERATIONS):
    print("Iteration n = " + str(i))
    print("Food available: " + str(plant.population))
    print("Number of cows: " + str(cow.population))

    plant_pop.append(plant.population)
    cow_pop.append(cow.population)
    if i > 0:
        dplant.append(plant.population - plant_pop[i-1])
        dcow.append(cow.population - cow_pop[i-1])

    plant.grow(1)
    #plant.grow(2.72/cow.population)   
    for animal in animals:
        animal.dieOrReproduce()
    

data = pd.DataFrame({"plants" : plant_pop, "cows" : cow_pop})
st.line_chart(data)

derivatives = pd.DataFrame({"rate of change of plant" : dplant, "rate of change of cow" : dcow})
st.line_chart(derivatives)