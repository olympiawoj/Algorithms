#!/usr/bin/python
'''
1. Understand

1 function, recipe_batches
receives 2 arguments
- recipe: a dict  - of what the recipe requires
- ingredients YOU have avail: a dict

keys: name
value: amount in recipe

output
- max # of whole batches that can be made for the supplied ingredient using the ingeds avail to you as indicated by the second dic

We need to loop through our recipe object

If 138//100 >=1, then print it


'''

import math


def recipe_batches(recipe, ingredients):
    if len(list(dict.values(recipe))) is not len(list(dict.values(ingredients))):
        return 0

    total_recipes = None

    for val in recipe:
        # Find how many recipes for each ingred
        total = ingredients[val] // recipe[val]

        if total_recipes is None:
            total_recipes = total

        # Total_recipes is only updated when it's greater than the total
        elif total < total_recipes:
            total_recipes = total

        print('total recipes', total_recipes)

    return total_recipes


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

# print(recipe_batches(
#     {'milk': 100, 'butter': 50, 'flour': 5},
#     {'milk': 138, 'butter': 48, 'flour': 51}
# ))
