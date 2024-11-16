import streamlit as st

from environment import *
from herbivore import *

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

#chart_data = pd.DataFrame({"food": food_available_history, "cows": cow_population_history})
st.line_chart(food_available_history)
st.line_chart(cow_population_history)