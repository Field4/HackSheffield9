import streamlit as st
import pandas as pd
import numpy as np
import time
from random import random
from math import sin, cos, pi

from environment import *
from herbivore import *

def get_random_positions_in_sheffield(n, max):
    numpreysToDisplay = int(min(n, max))
    positions = np.random.randn(numpreysToDisplay, 2) / [50,50] + [53.38, -1.4786]
    return positions

def displayRandomOnMap(prey_population, title, size, colour):
    df = pd.DataFrame(
        get_random_positions_in_sheffield(prey_population, 200), columns = ["lat", "lon"]
    )
    st.write(title)
    st.map(df, zoom=11, size=size, color=colour)

def displayOnMap(prey_positions, title, size, colour):
    df = pd.DataFrame(
        prey_positions, columns = ["lat", "lon"]
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


def eatpreysOnMap(prey_population, predator_population, title, prey_size, prey_colour, carnivore_size, carnivore_colour):
    prey_positions = get_random_positions_in_sheffield(prey_population, 500)
    map = displayOnMap(prey_positions, title, prey_size, prey_colour)

    time.sleep(5)

    predator_positions = get_offset_positions(prey_positions, predator_population)

    map.empty()

    colours = []
    for i in range(int(prey_population)):
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
    if predator_population < prey_population:
        remaining_preys = []
        for i in range(int(predator_population), int(prey_population)):  #this feels wrong but it works, so it might create an error later
            remaining_preys.append(prey_positions[i])
        print(remaining_preys)
        map = displayOnMap(remaining_preys, title, prey_size, prey_colour)



env = Environment(15, 0.5, 1000)
prey = Herbivore(11, 0.75, 2)

eatpreysOnMap(prey.population, 10, "eating", 1, "#6e3300", 1, "#ff0000")

food_available_history = []
prey_population_history = []

for i in range(6):
    env.generatePlantLife()
    eaten = prey.dieOrReproduce(env.plantLifeAvailable)
    env.eatPlants(eaten * prey.kill_rate)
    print("Iteration n = " + str(i))
    print("Food available: " + str(env.plantLifeAvailable))
    print("Number of preys: " + str(prey.population))
    food_available_history.append(env.plantLifeAvailable)
    prey_population_history.append(prey.population)



st.line_chart(food_available_history)
st.line_chart(prey_population_history)

