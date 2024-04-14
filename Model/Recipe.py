import requests


class Recipe:
    def __init__(self, title: str, ingredients, instructions, image):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions
        self.image = image

    def get_title(self):
        return self.title

    def get_ingredients(self):
        return self.ingredients

    def get_instructions(self):
        return self.instructions

    def get_image(self):
        return self.image