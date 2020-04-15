#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    count = []
    for i, v in recipe.items():
        if ingredients.get(i) is None:
            return 0
        else:
            num = ingredients[i] // v
            count.append(num)
    return min(count)

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    # recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    recipe = { 'milk': 2, 'sugar': 40, 'butter': 20 }
    # ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    ingredients = { 'milk': 5, 'sugar': 120, 'butter': 500 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
