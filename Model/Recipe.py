import requests
from PIL import Image
import io

class Recipe:
    def __init__(self, title: str, ingredients, instructions, image_url):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.image_url = image_url  # Holds image url that is provided in the API response
        self.image = None  # Will hold image
        self.retrieve_image()

    def retrieve_image(self):
        """
        Downloads an image from the provided URL and stores it as a PIL Image object.

        This method fetches the image from `self.image_url`, converts the image data
        into a binary stream, and then creates a PIL Image object. The image is then
        stored in `self.image` attribute of the Recipe instance. If `self.image_url`
        is not defined, the method does nothing.

        Raises:
            HTTPError: An error occurs during the HTTP request for the image.

        Example usage:
            recipe = Recipe("Pasta", ["pasta", "tomato"], "Boil pasta, add tomato", "http://example.com/image.jpg")
            recipe.retrieve_image()  # Now recipe.image contains the PIL Image object
        """
        if self.image_url:
            # Perform an HTTP GET request to fetch the image
            response = requests.get(self.image_url)
            # If the request fails, an HTTPError will be raised
            response.raise_for_status()

            # Convert the raw image data into a binary buffer
            image_bytes = io.BytesIO(response.content)

            # Create a PIL Image object from the binary buffer and assign it to the self.image attribute
            self.image = Image.open(image_bytes)

            # Optionally display the image using the default image viewer
            self.image.show()


    def get_title(self):
        return self.title

    def get_ingredients(self):
        return self.ingredients

    def get_instructions(self):
        return self.instructions

    def get_image(self):
        return self.image

    def print_Recipe(self):
        print(f'Recipe: {self.title}')
        print("Ingredients:")
        print(self.ingredients)
        print("Instructions:")
        print(self.instructions)