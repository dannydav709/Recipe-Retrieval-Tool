import requests
from .tools import response_to_json
import traceback
from .Recipe import Recipe
from .Recipe_Service import Recipe_Service


#   https://www.themealdb.com/api.php
class Recipe_API:
    def __init__(self
                 , API_key="1"
                 , base_url="https://www.themealdb.com/api/json/v1"):
        """
            Receives API details.
            Calls API.
        """

        self.API_key = API_key
        self.base_url = base_url
        self.response_json = None

    def search_API(self, query: str = "french"):
        """
        Will call API with search query that user specifies.
        Will assign self.response to the response resulting from this function call

        Args:
            query (str) (default="french"): Recipe name / search term

        Returns:
            API response (JSON): JSON format of API response (processed by a custom function)
            None: if error

        Errors:
            Returns None
        """

        url = f'{self.base_url}/{self.API_key}/search.php?s={query}'

        print(url)
        try:
            response_json = response_to_json(url)
            self.response_json = response_json
            return response_json
        except Exception as e:
            traceback.print_exc()
            return None

    def get_recipes(self):
        """
        Will retrieve the recipes list (containing JSON format recipe objects) from the API response.

        :return: recipes (list): "recipes" list-object extracted from API response
        """
        recipes = self.response_json.get("meals", [])  # Default value is empty list.
        return recipes
