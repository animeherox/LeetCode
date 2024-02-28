from collections import defaultdict
from sortedcontainers import SortedSet
from typing import List

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodToCuisineRating = {}
        self.cuisineToFoods = defaultdict(lambda: SortedSet(key=lambda x: (-x[0], x[1])))
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foodToCuisineRating[food] = (cuisine, rating)
            self.cuisineToFoods[cuisine].add((rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, oldRating = self.foodToCuisineRating[food]
        self.foodToCuisineRating[food] = (cuisine, newRating)
        self.cuisineToFoods[cuisine].remove((oldRating, food))
        self.cuisineToFoods[cuisine].add((newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisineToFoods[cuisine][0][1]