import random

class Animal:
    population:int = 0
    feedstock_utilisation:float = 1
    food_demand:float = 0.5
    food_sources:list = []
    name:str

    def __init__(self, name : str, initial_pop : int, food_demand: float, feedstock_utilisation: float):
        self.population = initial_pop
        self.food_sources
        self.name = name
        self.food_demand = food_demand
        self.feedstock_utilisation = feedstock_utilisation

    def eat(self, kill_rate):
        # eat an amount of each food source proportional to how much of each is left
        
        for food in self.food_sources:
            print("food population is ", food.population, " and weight is ", kill_rate)
            food.population -=  int(food.population * kill_rate)
        


    def foodWanted(self):
        return self.food_demand * self.population
    
    def dieOrReproduce(self):
        # count the total food value of all food sources
        total_food = 0
        for food in self.food_sources:
            total_food += food.population
        
        available_food = total_food * self.feedstock_utilisation
        
        satisfaction_ratio = available_food / self.foodWanted()  # the ratio between how much food the species needs to survive, and how much is available
        kill_rate = 1 / satisfaction_ratio # the proportion of plants that get eaten that don't survive into the next iteration
        self.grow(satisfaction_ratio)
        self.eat(kill_rate) # use new population for eating

    def grow(self, food_ratio):
        if food_ratio <1:
            print(self.name, "population does not have enough food and will shrink", "ratio = ", food_ratio)
            food_ratio -= 0.25  # die faster than they grow factor 
        elif food_ratio >1: 
            food_ratio = min(food_ratio, 2)
            print(self.name, "population has surplus food and will grow", "ratio = ", food_ratio)  
        else: 
            print(self.name, "population is in exact equilibrium with the amount of food, and so will shrink slightly.")
        self.population = max(1, int(food_ratio * self.population))
