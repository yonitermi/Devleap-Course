def main(recipe, available_ingredients):
    max_cakes = []
    
    # For each ingredient in the recipe
    for ingredient, amount in recipe.items():
        # If the ingredient is not available, return 0 as we can't make any cakes without it
        if ingredient not in available_ingredients:
            return 0
        # Add to the list the number of times the available ingredient can be used 
        # as per the recipe requirement
        max_cakes.append(available_ingredients[ingredient] // amount)

    # Return the minimum value from the list which gives the number of cakes that can be made
    return min(max_cakes)

