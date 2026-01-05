# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from quest import Quest
from item import DEBUG


class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
    # Setup the game
    def setup(self, player_name=None):
        """Initialize the game with rooms, commands, and quests."""
        self._setup_commands()
        self._setup_rooms()
        self._setup_player(player_name)
        self._setup_quests()

        # Setup commands
    def _setup_commands(self):
        """Initialize all game"""
        self.commands["help"] = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["quit"] = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["go"] = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["history"] = Command("history", " : accéder à l'historique des lieux", Actions.history, 0)
        self.commands["back"] = Command("back", " : revenir en arrière", Actions.back, 0)
        self.commands["look"] = Command("look", " : afficher la liste des items et des personnages présents dans le lieu actuel", Actions.look, 0)
        self.commands["take"] = Command("take", " : prendre les items dans le lieu actuel", Actions.take, 1)
        self.commands["check"] = Command("check", " : vérifier l'inventaire", Actions.check, 0)
        self.commands["talk"] = Command("talk", " <someone> : intéragir avec les personnages non joueurs", Actions.talk, 1)
        self.commands["quests"] = Command("quests", " : afficher la liste des quêtes", Actions.quests, 0)
        self.commands["quest"] = Command("quest", " <titre> : afficher les détails d'une quête", Actions.quest, 1)
        self.commands["activate"] = Command("activate", " <titre> : activer une quête", Actions.activate, 1)
        self.commands["rewards"] = Command("rewards", " : afficher vos récompenses", Actions.rewards, 0)
        
        
        self.directions = []
        for i in self.rooms:
            for direction in i.get_exits().keys():
                if direction not in self.directions:
                    self.directions.append(direction)
    

        # Setup rooms
    def _setup_rooms(self):
        """Initialize all rooms and their exits."""
        #Create rooms
        capitale = Room("la Capitale du Royaume Central", "une grande cité humaine, centre politique et culturel du royaume.")
        self.rooms.append(capitale)
        strahl = Room("Strahl", "une ville religieuse.")
        self.rooms.append(strahl)
        village = Room("le village de Heiter", "le village où habite Heiter, notre ami prêtre.")
        self.rooms.append(village)
        prairie = Room("la prairie", "grande étendue de fleurs.")
        self.rooms.append(prairie)
        donjon = Room("un donjon", "un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(donjon)
        domaine = Room("le domaine de Graf Grenat", "une ville fortifiée dans les contrées du Nord, protégée par une barrière magique empechant les démons d'entrer dans la cité.\nCependant, bien que la ville reste prospère, ses environs sont une zone de guerre entre Aura et ses démons et les humains.")
        self.rooms.append(domaine)
        plateau = Room("un des villages isolés du Plateau du Nord", "plaines isolées où se trouvent des villages et de grandes forêts enneigées.")
        self.rooms.append(plateau)
        ausserst = Room("Ausserst", "la cité magique du Nord, siège de l'Association Magique Continentale.\nC'est aussi une ville réputée pour ses académies et infrastructures dédiées aux mages.")
        self.rooms.append(ausserst)
        royaume = Room("le Royaume du Nord", "Prenez garde ! Les routes sont dangereuses et infestées de montres.")
        self.rooms.append(royaume)
        aureole = Room("Auréole", "le royaume où reposerait les âmes des défunts.")
        self.rooms.append(aureole)

        # Add rooms to game
        for room in [capitale, strahl, village, prairie, donjon, domaine, plateau, ausserst, royaume,aureole]:
            self.rooms.append(room)

        # Create exits for rooms
        capitale.exits = {"N" : strahl, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        strahl.exits = {"N" : prairie, "E" : None, "S" : capitale, "O" : village, "U" : None, "D" : None}
        village.exits = {"N" : None, "E" : strahl, "S" : None, "O" : None, "U" : None, "D" : None}
        prairie.exits = {"N" : domaine, "E" : None, "S" : strahl, "O" : None, "U" : None, "D" : donjon}
        donjon.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : prairie, "D" : None}
        domaine.exits = {"N" : None, "E" : None, "S" : prairie, "O" : plateau, "U" : None, "D" : None}
        plateau.exits = {"N" : None, "E" : domaine, "S" : None, "O" : ausserst, "U" : None, "D" : None}
        ausserst.exits = {"N" : royaume, "E" : plateau, "S" : None, "O" : None, "U" : None, "D" : donjon}
        royaume.exits = {"N" : aureole, "E" : None, "S" : ausserst, "O" : None, "U" : None, "D" : None}
        aureole.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}

        # Setup items
        capitale.inventory = {
            "sceptre": Item("sceptre", "bâton magique personnel.", "2")
        }
        village.inventory = {
            "grimoire": Item("grimoire de Flamme", "livre de sorts transmis par Flamme, notre mentor.", "1.5")
        }
        strahl.inventory = {
            "monument": Item("monument de la déesse", "statuette de la déesse en pierre, considéré comme un artéfact religieux .", "10")
        }
        domaine.inventory = {
            "reliques": Item("reliques impériales", "armes anciennes conservés par l'Empire.", "15"),
            "barriere": Item("barrière magique de Graf Grenat", "artéfact immatériel, barrière érigée par Flamme pour protéger la ville contre les démons.", "0")
        }
        plateau.inventory = {
            "artefacts": Item("artéfacts liés à Auréole", "objets mystiques censés guider vers Aureole (pierres, talismans).", "2")
        }
        ausserst.inventory = {
            "medaillon": Item("médaillon de l'Examen des Mages", "petit médaillon en métal, remis aux candidats pour prouver leur réussite à l'examen de mage de première classe.", "0.2")
        }
        royaume.inventory = {
            "statue": Item("Statues en Or", "habitants transformés en or par magie.", "247")
        }

        # Setup characters
        village.characters = {
            "fern": Character("Fern", "orpheline recuillie par le prêtre Heiter, talentueuse magicienne.", village, ["Si je ne m'occupe pas de tout, rien avance..."]),
            "heiter": Character("Heiter", "Prêtre du groupe originel, jovial mais alcoolique.", village, ["La vie est courte... alors profitons-en, même un verre à la main.", "Un verre de vin, et la vie devient plus douce."])
        }
        prairie.characters = {
            "stark": Character("Stark", "jeune guerrier élevé par Eisen, un ancien compagnon.", prairie, ["Je ne suis pas aussi fort que vous le pensez... mais je ferai de mon mieux pour vous protéger.","Je ne suis pas un héros, juste quelqu'un qui veut protéger ses amis."]),
            "eisen": Character("Eisen", "guerrier nain du groupe originel.", prairie, ["La force n'est rien sans le courage de l'utiliser pour les autres.","Un guerrier ne vit pas pour lui-même, mais pour ceux qu'il protège."])
        }
        aureole.characters = {
            "himmel": Character("Himmel", "le héros humain qui a vaincu le Roi Démon, avec nous.", aureole, ["Ce qui compte, ce n'est pas la durée... mais les souvenirs qu'on a créés ensemble.","Même si le monde est cruel, il y a toujours de la beauté à trouver."])
        }   
        strahl.characters = {
            "flamme": Character("Flamme", "grande magicienne qui nous a sauvé par le passé et qui nous a enseigné la magie.", strahl, ["La magie est une trace de notre passage dans le monde.","Chaque sort raconte une histoire."])
        }             

        # Setup player and starting room
    def _setup_player(self, player_name=None):
        """Initialize the player."""
        if player_name is None:
            player_name = input("\nEntrez votre nom: ")

        self.player = Player(player_name)
        self.player.current_room = self.rooms[0] #capitale

    def _setup_quests(self):
        """Initialize all quests."""
        exploration_quest = Quest(
            title="Grand Explorateur",
            description="Explorez tous les lieux de ce monde mystérieux.",
            objectives=["Visiter Forest"
                        , "Visiter Tower"
                        , "Visiter Cave"
                        , "Visiter Cottage"
                        , "Visiter Castle"],
            reward="Titre de Grand Explorateur"
        )

        travel_quest = Quest(
            title="Grand Voyageur",
            description="Déplacez-vous 10 fois entre les lieux.",
            objectives=["Se déplacer 10 fois"],
            reward="Bottes de voyageur"
        )

        discovery_quest = Quest(
            title="Découvreur de Secrets",
            description="Découvrez les trois lieux les plus mystérieux.",
            objectives=["Visiter Cave"
                        , "Visiter Tower"
                        , "Visiter Castle"],
            reward="Clé dorée"
        )

        # Add quests to player's quest manager
        self.player.quest_manager.add_quest(exploration_quest)
        self.player.quest_manager.add_quest(travel_quest)
        self.player.quest_manager.add_quest(discovery_quest)

    def win(self):
        """Check if all quests are completed to finish the game."""
        for elt in self.player.quests.values():
            if elt.is_completed():
                self.player.add_reward(elt.reward)
                print(f"\nFélicitations ! Vous avez complété la quête : {elt.title}\n")
            else:
                return False
        print("\nVous avez terminé toutes les quêtes du jeu ! Merci d'avoir joué.\n")
        return True
    
    def loose(self):
        """Check if the player has lost the game."""
        # when you enter in donjon with no the sceptre
        if sceptre not in self.player.inventory and self.player.current_room == donjon:
            print("\nVous avez perdu le jeu ! Il n'y a plus rien à faire ici.\n")
            return True
        return False

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
            for character in self.player.current_room.characters.values():
                character.move()
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print('>')
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)
    

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()