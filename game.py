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

from pathlib import Path
import sys

# Tkinter imports for GUI
import tkinter as tk
from tkinter import ttk, simpledialog

import assets


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
        """Initialize all game commands"""
        self.commands["help"] = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["quit"] = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["go"] = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["history"] = Command("history", " : accéder à l'historique des lieux", Actions.history, 0)
        self.commands["back"] = Command("back", " : revenir en arrière", Actions.back, 0)
        self.commands["look"] = Command("look", " : afficher la liste des items et des personnages présents dans le lieu actuel", Actions.look, 0)
        self.commands["take"] = Command("take", " <name of item> : prendre les items dans le lieu actuel", Actions.take, 1)
        self.commands["drop"] = Command("drop", " <name of item> : remettre les items dans le lieu actuel", Actions.drop, 1)
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
        capitale = Room("la Capitale du Royaume Central", "une grande cité humaine, centre politique et culturel du royaume.", "capitale.jpg")
        self.rooms.append(capitale)
        strahl = Room("Strahl", "une ville religieuse.", "strahl.jpg")
        self.rooms.append(strahl)
        village = Room("le village de Heiter", "le village où habite Heiter, notre ami prêtre.", "village_heiter.jpg")
        self.rooms.append(village)
        prairie = Room("la prairie", "grande étendue de fleurs.", "prairie.jpg")
        self.rooms.append(prairie)
        donjon = Room("un donjon", "un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.", "donjon.jpg")
        self.rooms.append(donjon)
        domaine = Room("le domaine de Graf Grenat", "une ville fortifiée dans les contrées du Nord, protégée par une barrière magique empechant les démons d'entrer dans la cité.\nCependant, bien que la ville reste prospère, ses environs sont une zone de guerre entre Aura et ses démons et les humains.", "domaine.jpg")
        self.rooms.append(domaine)
        plateau = Room("un des villages isolés du Plateau du Nord", "plaines isolées où se trouvent des villages et de grandes forêts enneigées.", "plateau.jpg")
        self.rooms.append(plateau)
        ausserst = Room("Ausserst", "la cité magique du Nord, siège de l'Association Magique Continentale.\nC'est aussi une ville réputée pour ses académies et infrastructures dédiées aux mages.", "ausserst.jpg")
        self.rooms.append(ausserst)
        royaume = Room("le Royaume du Nord", "Prenez garde ! Les routes sont dangereuses et infestées de montres.", "quete.jpg")
        self.rooms.append(royaume)
        aureole = Room("Auréole", "le royaume où reposerait les âmes des défunts.", "aureole.jpg")
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
            # Check win and lose conditions at each turn
            if self.win():
                self.finished = True
            elif self.loose():
                self.finished = True
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
    
    
    # Setup quests
    def _setup_quests(self):
        """Initialize all quests."""
        exploration_quest = Quest(
            title="Vers Auréole",
            description="Franchissez les étapes nécessaires pour atteindre ce lieu légendaire.",
            objectives=["Visiter le village de Heiter"
                        , "parler avec fern"
                        , "parler avec heiter"
                        , "Visiter Ausserst"
                        , "prendre le medaillon"
                        , "Aller à Auréole"],
            reward="Bénédiction d'Auréole"
        )

        interaction_quest = Quest(
            title="Retrouver Himmel",
            description="Retrouvez votre ancien compagnon Himmel à Auréole.",
            objectives=["Aller à Auréole"
                        , "parler avec himmel"],
            reward="Souvenirs d'aventures récupérés"
        )

        item_quest = Quest(
            title="Récupérer le Sceptre",
            description="Récupérer le sceptre.",
            objectives=["Aller à la Capitale du Royaume Central"
                        , "prendre le sceptre"],
            reward="Sceptre"
        )

        # Add quests to player's quest manager
        self.player.quest_manager.add_quest(exploration_quest)
        self.player.quest_manager.add_quest(interaction_quest)
        self.player.quest_manager.add_quest(item_quest)

    def win(self):
        """Check if all quests are completed to finish the game."""
        for elt in self.player.quest_manager.quests:
            if elt.is_completed:
                self.player.add_reward(elt.reward)
                print(f"\nFélicitations ! Vous avez complété la quête : {elt.title}\n")
            else:
                return False
        print("\nVous avez terminé toutes les quêtes du jeu ! Merci d'avoir joué.\n")
        return True
    
    def loose(self):
        """Check if the player has lost the game."""
        # when you enter in donjon with no the sceptre
        donjon = self.rooms[4]  # donjon is at index 4 in self.rooms
        if "sceptre" not in self.player.inventory and self.player.current_room == donjon:
            print("\nVous avez perdu le jeu ! Il n'y a plus rien à faire ici.\n")
            return True
        return False


##############################
# Tkinter GUI Implementation #
##############################

class _StdoutRedirector:
    """Redirect sys.stdout writes into a Tkinter Text widget."""
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, msg):
        """Write message to the Text widget."""
        if msg:
            self.text_widget.configure(state="normal")
            self.text_widget.insert("end", msg)
            self.text_widget.see("end")
            self.text_widget.configure(state="disabled")

    def flush(self):
        """Flush method required by sys.stdout interface (no-op for Text widget)."""


class GameGUI(tk.Tk):
    """Tkinter GUI for the text-based adventure game.

    Layout layers:
    L3 (top): Split into left image area (600x400) and right buttons.
    L2 (middle): Scrolling terminal output.
    L1 (bottom): Command entry field.
    """

    IMAGE_WIDTH = 600
    IMAGE_HEIGHT = 400

    def __init__(self):
        super().__init__()
        self.title("TBA")
        self.geometry("900x700")  # Provide enough space
        self.minsize(900, 650)

        # Underlying game logic instance
        self.game = Game()

        # Ask player name via dialog (fallback to 'Joueur')
        name = simpledialog.askstring("Nom", "Entrez votre nom:", parent=self)
        if not name:
            name = "Joueur"
        self.game.setup(player_name=name)  # Pass name to avoid double prompt

        # Build UI layers
        self._build_layout()

        # Redirect stdout so game prints appear in terminal output area
        self.original_stdout = sys.stdout
        sys.stdout = _StdoutRedirector(self.text_output)

        # Print welcome text in GUI
        self.game.print_welcome()

        # Load initial room image
        self._update_room_image()

        # Handle window close
        self.protocol("WM_DELETE_WINDOW", self._on_close)


    # -------- Layout construction --------
    def _build_layout(self):
        # Configure root grid: 3 rows (L3, L2, L1)
        self.grid_rowconfigure(0, weight=0)  # Image/buttons fixed height
        self.grid_rowconfigure(1, weight=1)  # Terminal output expands
        self.grid_rowconfigure(2, weight=0)  # Entry fixed
        self.grid_columnconfigure(0, weight=1)

        # L3 Top frame
        top_frame = ttk.Frame(self)
        top_frame.grid(row=0, column=0, sticky="nsew", padx=6, pady=(6,3))
        top_frame.grid_columnconfigure(0, weight=0)
        top_frame.grid_columnconfigure(1, weight=1)

        # L3L Image area (left)
        image_frame = ttk.Frame(top_frame, width=self.IMAGE_WIDTH, height=self.IMAGE_HEIGHT)
        image_frame.grid(row=0, column=0, sticky="nw", padx=(0,6))
        image_frame.grid_propagate(False)  # Keep requested size
        self.canvas = tk.Canvas(image_frame,
                                width=self.IMAGE_WIDTH,
                                height=self.IMAGE_HEIGHT,
                                bg="#222")
        self.canvas.pack(fill="both", expand=True)

        # Initialize image reference (will be loaded by _update_room_image)
        self._image_ref = None  # Keep reference to prevent garbage collection
        # Initial image will be loaded after welcome message

        # L3R Buttons area (right)
        buttons_frame = ttk.Frame(top_frame)
        buttons_frame.grid(row=0, column=1, sticky="ne")
        for i in range(10):
            buttons_frame.grid_rowconfigure(i, weight=0)
        buttons_frame.grid_columnconfigure(0, weight=1)

        # Load button images (keep references to prevent garbage collection)
        assets_dir = Path(__file__).parent / 'assets'
        # Load pre-resized 50x50 PNG images for better quality
        self._btn_help = tk.PhotoImage(file=str(assets_dir / 'help-50.png'))
        self._btn_up = tk.PhotoImage(file=str(assets_dir / 'up-arrow-50.png'))
        self._btn_down = tk.PhotoImage(file=str(assets_dir / 'down-arrow-50.png'))
        self._btn_left = tk.PhotoImage(file=str(assets_dir / 'left-arrow-50.png'))
        self._btn_right = tk.PhotoImage(file=str(assets_dir / 'right-arrow-50.png'))
        self._btn_quit = tk.PhotoImage(file=str(assets_dir / 'quit-50.png'))

        # Command buttons
        tk.Button(buttons_frame,
                  image=self._btn_help,
                  command=lambda: self._send_command("help"),
                  bd=0).grid(row=0, column=0, sticky="ew", pady=2)
        # Movement buttons (N,E,S,O)
        move_frame = ttk.LabelFrame(buttons_frame, text="Déplacements")
        move_frame.grid(row=1, column=0, sticky="ew", pady=4)
        tk.Button(move_frame,
                  image=self._btn_up,
                  command=lambda: self._send_command("go N"),
                  bd=0).grid(row=0, column=0, columnspan=2)
        tk.Button(move_frame,
                  image=self._btn_left,
                  command=lambda: self._send_command("go O"),
                  bd=0).grid(row=1, column=0)
        tk.Button(move_frame,
                  image=self._btn_right,
                  command=lambda: self._send_command("go E"),
                  bd=0).grid(row=1, column=1)
        tk.Button(move_frame,
                  image=self._btn_down,
                  command=lambda: self._send_command("go S"),
                  bd=0).grid(row=2, column=0, columnspan=2)

        # Quit button
        tk.Button(buttons_frame,
                  image=self._btn_quit,
                  command=lambda: self._send_command("quit"),
                  bd=0).grid(row=2, column=0, sticky="ew", pady=(8,2))

        # L2 Terminal output area (Text + Scrollbar)
        output_frame = ttk.Frame(self)
        output_frame.grid(row=1, column=0, sticky="nsew", padx=6, pady=3)
        output_frame.grid_rowconfigure(0, weight=1)
        output_frame.grid_columnconfigure(0, weight=1)

        scrollbar = ttk.Scrollbar(output_frame, orient="vertical")
        self.text_output = tk.Text(output_frame,
                                   wrap="word",
                                   yscrollcommand=scrollbar.set,
                                   state="disabled",
                                   bg="#111", fg="#eee")
        scrollbar.config(command=self.text_output.yview)
        self.text_output.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # L1 Entry area
        entry_frame = ttk.Frame(self)
        entry_frame.grid(row=2, column=0, sticky="ew", padx=6, pady=(3,6))
        entry_frame.grid_columnconfigure(0, weight=1)

        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(entry_frame, textvariable=self.entry_var)
        self.entry.grid(row=0, column=0, sticky="ew")
        self.entry.bind("<Return>", self._on_enter)
        self.entry.focus_set()


    # -------- Image update --------
    def _update_room_image(self):
        """Update the canvas image based on the current room."""
        if not self.game.player or not self.game.player.current_room:
            return

        room = self.game.player.current_room
        assets_dir = Path(__file__).parent / 'assets'

        # Use room-specific image if available, otherwise fallback
        if room.image:
            image_path = assets_dir / room.image
        else:
            image_path = assets_dir / 'scene.png'

        try:
            # Load new image
            self._image_ref = tk.PhotoImage(file=str(image_path))
            # Clear canvas and redraw image
            self.canvas.delete("all")
            self.canvas.create_image(
                self.IMAGE_WIDTH/2,
                self.IMAGE_HEIGHT/2,
                image=self._image_ref
            )
        except (FileNotFoundError, tk.TclError):
            # Fallback to text if image not found or cannot be loaded
            self.canvas.delete("all")
            self.canvas.create_text(
                self.IMAGE_WIDTH/2,
                self.IMAGE_HEIGHT/2,
                text=f"Image: {room.name}",
                fill="white",
                font=("Helvetica", 18)
            )


    # -------- Event handlers --------
    def _on_enter(self, _event=None):
        """Handle Enter key press in the entry field."""
        value = self.entry_var.get().strip()
        if value:
            self._send_command(value)
        self.entry_var.set("")


    def _send_command(self, command):
        if self.game.finished:
            return
        # Echo the command in output area
        print(f"> {command}\n")
        self.game.process_command(command)
        # Check win and lose conditions at each turn
        if self.game.win():
            self.game.finished = True
        elif self.game.loose():
            self.game.finished = True
        # Update room image after command (in case player moved)
        self._update_room_image()
        if self.game.finished:
            # Disable further input and schedule close (brief delay to show farewell)
            self.entry.configure(state="disabled")
            self.after(600, self._on_close)


    def _on_close(self):
        # Restore stdout and destroy window
        sys.stdout = self.original_stdout
        self.destroy()

def main():
    """Entry point.

    If '--cli' is passed as an argument, start the classic console version.
    Otherwise launch the Tkinter GUI.
    Fallback to CLI if GUI cannot be initialized (e.g., headless environment).
    """
    args = sys.argv[1:]
    if '--cli' in args:
        Game().play()
        return
    try:
        app = GameGUI()
        app.mainloop()
    except tk.TclError as e:
        # Fallback to CLI if GUI fails (e.g., no DISPLAY, Tkinter not available)
        print(f"GUI indisponible ({e}). Passage en mode console.")
        Game().play()


if __name__ == "__main__":
    main()