import requests
from .tools import response_to_json
import traceback


#   https://www.themealdb.com/api.php
class Recipe_API:
    #   Example: www.themealdb.com/api/json/v1/1/random.php
    #   Base: www.themealdb.com/api/json/v1/1/
    #   Search: search.php?s=
    def __init__(self
                 , API_key="1"
                 , base_url="https://www.themealdb.com/api/json/v1"):

        self.API_key = API_key
        self.base_url = base_url

    def search_API(self, query: str = "french"):
        """
        Will try to call the API with a search query that user specifies.

        As of now:
            - calls url with "french" as query
            - gets "strInstructions" from the resulting JSON
            - if error:
                - prints error
                - returns None

        Args:
            query (string): Recipe name / search term

        Returns:
            Recipe object
        """

        url = f'{self.base_url}/{self.API_key}/search.php?s={query}'

        #   ------ Testing ------
        print(url)
        try:
            response_data = response_to_json(url)
            meals = response_data.get("meals", [])  # Default value is empty list
            if meals:  # Check if the list is not empty
                strInstructions = meals[0].get("strInstructions",
                                               "No instructions provided")  # Access the first meal's instructions
                print(strInstructions)
        except Exception as e:
            # print(e)
            # traceback.print_exc()
            traceback.format_exc()
            # print("End of exception\n\n")
            return None
