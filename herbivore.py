class Herbivore:
    population : int = 0
    plantUtilisation : float = 0.5
    foodDemand : int = 1

    def __init__(self, initialPop : int, plantUtilisation : float, foodDemand : int):
        self.population = initialPop
        self.plantUtilisation = plantUtilisation
        self.foodDemand = foodDemand

    def foodNeeded(self):
        return self.foodDemand * self.population
    
    def dieOrReproduce(self, foodAvailable):
        foodRatio = foodAvailable / self.foodNeeded()
        if foodRatio > 1.25:
            foodRatio = 1.25
        elif foodRatio < 0.75:
            foodRatio = 0.75
        self.population *= foodRatio
        return self.foodNeeded() * foodRatio


