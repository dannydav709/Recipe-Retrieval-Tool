import sys
# sys.path.append('./Model/Recipe_API.py')
from Model.Recipe_API import Recipe_API
from Model.Recipe_Service import Recipe_Service
from View.Recipe_Window import Recipe_Window2


def main():
    recipe_API = Recipe_API()
    api_response = recipe_API.search_API("potato")
    recipes = recipe_API.get_recipes()
    recipe_service = Recipe_Service(recipes)
    recipes = recipe_service.process_recipes(recipes)

    for recipe in recipes:
        recipe.print()
        print("------------------------------------------------")

    # window = Recipe_Window(recipes[0])

    app = Recipe_Window2(recipes[0])
    # app.mainloop()


main()