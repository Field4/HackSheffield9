class Animal:
    population:int = 0
    feedstock_utilisation:float = 0.5
    food_demand:float = 1
    food_sources:list = []
    name:str

    def __init__(self, name : str, initial_pop : int, food_demand: float):
        self.population = initial_pop
        self.food_sources
        self.name = name
        self.food_demand = food_demand

    def eat(self, food_weight):
        # eat an amount of each food source proportional to how much of each is left
        print(self.name, "is eating: ")
        for food in self.food_sources:
            food.population -=  food.population * food_weight
            print(food.name)
        


    def foodNeeded(self):
        return self.food_demand * self.population
    
    def dieOrReproduce(self):
        # count the total food value of all food sources
        total_food = 0
        for food in self.food_sources:
            total_food += food.population
        
        requiredFood = self.foodNeeded()

        food_ratio = min(max(total_food/requiredFood, 0.75), 1.25)
        if food_ratio <1: print(self.name, "population does not have enough food and will shrink")
        if food_ratio >1: print(self.name, "population has surplus food and will grow")

        self.population *= food_ratio

        self.eat(1/food_ratio)
