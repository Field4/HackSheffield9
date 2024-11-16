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

NUM_ITERATIONS = 100
plant_pop = []
cow_pop = []

for i in range(NUM_ITERATIONS):
    print("Iteration n = " + str(i))
    print("Food available: " + str(plant.population))
    print("Number of cows: " + str(cow.population))
    plant.grow()
    plant_pop.append(plant.population)
    cow_pop.append(cow.population)
    for animal in animals:
        animal.dieOrReproduce()

data = pd.DataFrame({"plants" : plant_pop, "cows" : cow_pop})
st.line_chart(data)