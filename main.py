import sys
# sys.path.append('./Model/Recipe_API.py')
from Model.Recipe_API import Recipe_API


def main():
    recipe_test = Recipe_API()
    result = recipe_test.search_API()
    print(result)


main()