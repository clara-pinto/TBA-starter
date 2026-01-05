# Define the Room class.

class Room:
   """The Room class represents a room in the game."""

    # Define the constructor. 
    def __init__(self, name, description, image=None):
        """
        Initialize a Room with a name and description.
        
        >>> room = Room("Hall", "dans un grand hall")
        >>> room.name
        'Hall'
        >>> room.description
        'dans un grand hall'
        >>> room.exits
        {}
        >>> room.image is None
        True
        """
        self.name = name
        self.description = description
        self.image = image # Path to image file (PNG/JPG) for this room
        self.exits = {}
        self.inventory = {}
        self.characters = {}
    
    # Define the get_exit method.
    def get_exit(self, direction):
        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.name} : {self.description}\n\n{self.get_exit_string()}\n"
    
    def get_inventory(self):
        if len(self.inventory) == 0 and len(self.characters) == 0:
            print("Il n'y a rien ici.\n")
            return
        print("On voit :\n")
        for item in self.inventory.values():
            print(f"\t- {item.name} : {item.description} ({item.weight} kg)\n")
        for character in self.characters.values():
            print(f"\t- {character.name} : {character.description}\n")