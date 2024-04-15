from .Recipe import Recipe


class Recipe_Service:
    def __init__(self, recipes: list):

        """
        Takes the recipes list (originally contained in the API call result), and holds JSON object
        """
        self.recipes: list = recipes

    def process_ingredients(self, recipe_json):
        """
        Processes ingredients list (contained within a JSON recipe object as a very particular format).

        A recipe from an API response holds the ingredients (and their measurements) in a very particular format. This
        function processes the data in the recipe JSON object into a neat dictionary that holds the ingredient as the key,
        and the measurement as the value.

        Parameters:
            recipe_json: The JSON recipe object contained in the recipes list that we get from an API response

        Returns:
            ingredients_and_measures (dict): The {dict} holding ingredient as key, and  measurement as value
        """
        ingredients_and_measures = dict()
        strIngredient = "strIngredient"
        strMeasure = "strMeasure"
        i = 1
        while recipe_json[f'{strIngredient}{str(i)}'] != "":
            ingredient = recipe_json[f'{strIngredient}{str(i)}']
            measure = recipe_json[f'{strMeasure}{str(i)}']
            ingredients_and_measures[ingredient] = measure
            i += 1
        return ingredients_and_measures

    def process_recipe(self, recipe_json):
        """
        Will take a JSON object and will process it into a Recipe object

        Returns:
            Recipe Object
        """

        title: str = recipe_json.get("strMeal")
        strInstructions = recipe_json.get("strInstructions")
        # The URL of the image of the final cooked recipe
        strMealThumb = recipe_json.get("strMealThumb")
        recipe = Recipe(title, self.process_ingredients(recipe_json), strInstructions, strMealThumb)
        return recipe

