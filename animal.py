class Animal:
    population:int = 0
    feedstock_utilisation:float = 0.5
    food_demand:float = 1
    food_sources:list = []
    name:str

    def __init__(self, name : str, initial_pop : int, food_demand: float, feedstock_utilisation: float):
        self.population = initial_pop
        self.food_sources
        self.name = name
        self.food_demand = food_demand
        self.feedstock_utilisation = feedstock_utilisation

    def eat(self, food_weight):
        # eat an amount of each food source proportional to how much of each is left
        #print(self.name, "is eating: ")
        for food in self.food_sources:
            food.population -=  int(food.population * food_weight)
        


    def foodNeeded(self):
        return self.food_demand * self.population
    
    def dieOrReproduce(self):
        # count the total food value of all food sources
        total_food = 0
        for food in self.food_sources:
            total_food += food.population
        
        available_food = total_food * self.feedstock_utilisation
        required_food = self.foodNeeded()
        #print(available_food, required_food)
        food_ratio = available_food/required_food
        food_ratio = min(food_ratio, 1.25)

        self.grow(food_ratio)

        self.eat(self.foodNeeded()/total_food) # use new population for eating

    def grow(self, food_ratio):
        if food_ratio <1: print(self.name, "population does not have enough food and will shrink")
        if food_ratio >1: print(self.name, "population has surplus food and will grow")

        self.population = int(food_ratio * self.population)