import streamlit as st
import pandas as pd
import numpy as np
import time
from random import random
from math import sin, cos, pi

from environment import *
from herbivore import *

def get_random_positions_in_sheffield(n, max):
    numCowsToDisplay = int(min(n, max))
    positions = np.random.randn(numCowsToDisplay, 2) / [50,50] + [53.38, -1.4786]
    return positions

def displayRandomOnMap(cow_population, title, size, colour):
    df = pd.DataFrame(
        get_random_positions_in_sheffield(cow_population, 200), columns = ["lat", "lon"]
    )
    st.write(title)
    st.map(df, zoom=11, size=size, color=colour)

def displayOnMap(cow_positions, title, size, colour):
    df = pd.DataFrame(
        cow_positions, columns = ["lat", "lon"]
    )
    st.write(title)
    return st.map(df, zoom=11, size=size, color=colour)

def get_offset_positions(prey_positions, predator_population):
    n = min(prey_positions.shape[0], predator_population)
    pairs = []
    for i in range(n):
        angle = random() * 2 * pi 
        pairs.append(
            [cos(angle)*0.0001 + prey_positions[i][0], sin(angle)*0.0001 + prey_positions[i][1]])
    return pairs


def eatCowsOnMap(cow_population, predator_population, title, cow_size, cow_colour, carnivore_size, carnivore_colour):
    prey_positions = get_random_positions_in_sheffield(cow_population, 500)
    map = displayOnMap(prey_positions, title, cow_size, cow_colour)

    time.sleep(5)

    predator_positions = get_offset_positions(prey_positions, predator_population)

    map.empty()

    colours = []
    for i in range(int(cow_population)):
        colours.append("#6e3300")
    for i in range(int(predator_population)):
        colours.append("#ff0000")
    
    combined_array = np.transpose(np.append(prey_positions, predator_positions, axis=0))

    combined_frame = pd.DataFrame( 
        {
        "latitudes" : combined_array[0],
        "longitudes" : combined_array[1],
        "colours" : colours
        }
    )

    map = st.map(combined_frame, latitude="latitudes", longitude="longitudes", color="colours")
    time.sleep(5)
    map.empty()
    if predator_population < cow_population:
        remaining_cows = []
        for i in range(int(predator_population), int(cow_population)):  #this feels wrong but it works, so it might create an error later
            remaining_cows.append(prey_positions[i])
        print(remaining_cows)
        map = displayOnMap(remaining_cows, title, cow_size, cow_colour)



env = Environment(15, 0.5, 1000)
cow = Herbivore(11, 0.75, 2)

eatCowsOnMap(cow.population, 10, "eating", 1, "#6e3300", 1, "#ff0000")

food_available_history = []
cow_population_history = []

for i in range(6):
    env.generatePlantLife()
    eaten = cow.dieOrReproduce(env.plantLifeAvailable)
    env.eatPlants(eaten * cow.kill_rate)
    print("Iteration n = " + str(i))
    print("Food available: " + str(env.plantLifeAvailable))
    print("Number of cows: " + str(cow.population))
    food_available_history.append(env.plantLifeAvailable)
    cow_population_history.append(cow.population)



st.line_chart(food_available_history)
st.line_chart(cow_population_history)

