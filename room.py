"""Room module for the game."""


class Room():
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
    
    def get_exit(self, direction):
        """Return the room in the given direction if it exists."""
        if direction in self.exits:
            return self.exits[direction]
        return None

    def get_exits(self):
        """Return the exits dictionary."""
        return self.exits
    
    def get_exit_string(self):
        """Return a string describing the room's exits."""
        exit_string = "Sorties: "
        for exit_dir in self.exits:
            if self.exits.get(exit_dir) is not None:
                exit_string += exit_dir + ", "
        return exit_string.strip(", ")

    def get_long_description(self):
        """Return a long description of this room including exits."""
        return f"\nVous êtes dans {self.name} : {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """Display the inventory of the room."""
        if len(self.inventory) == 0 and len(self.characters) == 0:
            print("Il n'y a rien ici.\n")
            return
        print("On voit :\n")
        for item in self.inventory.values():
            print(f"\t- {item.name} : {item.description} ({item.weight} kg)\n")
        for character in self.characters.values():
            print(f"\t- {character.name} : {character.description}\n")