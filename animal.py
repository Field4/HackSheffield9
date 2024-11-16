class Animal:
    population:int = 0
    feedstock_utilisation:float = 0.5
    food_demand:int = 1

    def __init__(self, initial_pop : int, feedstock_utilisation : float, food_demand : int):
        self.population = initial_pop
        self.feedstock_utilisation = feedstock_utilisation
        self.food_demand = food_demand

    def foodNeeded(self):
        return self.food_demand * self.population
    
    def dieOrReproduce(self, food_available):
        food_ratio = food_available / self.foodNeeded()
        if food_ratio > 1.25:
            food_ratio = 1.25
        elif food_ratio < 0.75:
            food_ratio = 0.75
        self.population *= food_ratio
        return self.foodNeeded() * food_ratio
