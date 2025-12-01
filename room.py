# Define the Room class.

class Room:
    """
    This class represents a room. A room has a name, a description and exits.

    Attributes:
        name (str): The name of the room.
        description (str): The description of the room.
        exits (dict): The different exits you can access from the current room.

    Methods:
        __init__(self, name, description) : The constructor.
        get_exit(self, direction) : Return the room in the given direction if it exists.
        get_exit_string(self) : Return a string describing the room's exits.
        get_long_description(self) : Return a long description of this room including exits.

    Examples:

    >>> room = Room("cuisine", "La où on mange", {Salon})
    >>> room.name
    'cuisine'
    >>> room.description
    'La où on mange'
    >>> room.exits
    Salon
    >>> type(room.get_exit)
    <class 'function'>
    >>> type(room.get_exit_string)
    <class 'function'>
    >>> type(room.get_long_description)
    <class 'function'>

    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
    
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
        if len(self.inventory) == 0:
            print("Il n'y a rien ici.\n")
            return
        print("La pièce contient :\n")
        for item in self.inventory.values():
            print(f"\t- {item.name} : {item.description} ({item.weight} kg)\n")
