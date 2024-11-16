import streamlit as st
import pandas as pd
import numpy as np

from environment import *
from herbivore import *

def displayCowsOnMap(cow_population, title):
    numCowsToDisplay = int(min(cow_population, 200))
    df = pd.DataFrame(
        np.random.randn(numCowsToDisplay, 2) / [50,50] + [53.38, -1.4786], columns = ["lat", "lon"]
    )
    st.write(title)
    st.map(df, zoom=11)


env = Environment(15, 0.5, 1000)
cow = Herbivore(100, 0.75, 2)

food_available_history = []
cow_population_history = []

for i in range(50):
    env.generatePlantLife()
    eaten = cow.dieOrReproduce(env.plantLifeAvailable)
    env.eatPlants(eaten * cow.kill_rate)
    print("Iteration n = " + str(i))
    print("Food available: " + str(env.plantLifeAvailable))
    print("Number of cows: " + str(cow.population))
    food_available_history.append(env.plantLifeAvailable)
    cow_population_history.append(cow.population)
    if i % 10 == 0 and cow.population >= 1: displayCowsOnMap(cow.population, "Cows at iteration " + i)
st.line_chart(food_available_history)
st.line_chart(cow_population_history)

