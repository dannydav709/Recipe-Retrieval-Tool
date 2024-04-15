import sys
# sys.path.append('./Model/Recipe_API.py')
from Model.Recipe_API import Recipe_API
from Model.Recipe_Service import Recipe_Service
from View.window_controller import Window_Controller

def main():
    # recipe_API = Recipe_API()
    # api_response = recipe_API.search_API()
    # recipes = recipe_API.get_recipes()
    # recipe_service = Recipe_Service(recipes)
    # recipe = recipe_service.process_recipe(recipes[0])
    #
    # recipe.print_Recipe()
    window = Window_Controller()

main()