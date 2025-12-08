
DEBUG = True

# Define the Item class.
class Item():
    # Define the constructor.
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

     # The string representation of the item.
    def __str__(self):
        return  self.name \
                + self.description
