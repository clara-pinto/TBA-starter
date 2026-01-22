# TBA

Ce repo contient la version finale d'un jeu d’aventure TBA, inspiré du monde du manga "Frieren".

Les lieux sont au nombre de 10, et on peut trouver dans certains des items et/ou des PNJ. 


## Structuration

Il y a 8 modules contenant chacun une classe.

- `game.py` / `Game` : description de l'environnement, interface avec le joueur ;
- `room.py` / `Room` : propriétés génériques d'un lieu  ;
- `player.py` / `Player` : le joueur ;
- `command.py` / `Command` : les consignes données par le joueur ;
- `actions.py` / `Action` : les fonctions qui sont appelées lorsque une commande est exécutée ;
- `item.py`  / `Item` : représenter les différents objets que le joueur pourra trouver dans les différents lieux de la map ;
- `character.py` / `Character` : représenter les différents personnages non joueurs ;
- `quest.py` / `Quest` et `QuestManager`: création des quêtes et gestion des quêtes ;
