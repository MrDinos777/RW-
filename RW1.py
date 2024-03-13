with open('recipes.txt', 'r') as file:
    data = file.readlines()

cook_book = {}
for line in data:
    recipe_name, ingredients = line.strip().split(':')
    recipe_name = recipe_name.strip()
    ingredients = ingredients.strip()

    ingredients_list = ingredients.split('\n')

    recipe_ingredients = []
    for ingredient in ingredients_list:
        ingredient_name, quantity, measure = ingredient.strip().split('|')
        ingredient_name = ingredient_name.strip()
        quantity = quantity.strip()
        measure = measure.strip()

        recipe_ingredients.append({
            'ingredient_name': ingredient_name,
            'quantity': quantity,
            'measure': measure
        })

    cook_book[recipe_name] = recipe_ingredients

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))