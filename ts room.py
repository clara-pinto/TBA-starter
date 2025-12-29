[1mdiff --git a/command.py b/command.py[m
[1mindex 919f71e..9678ab9 100644[m
[1m--- a/command.py[m
[1m+++ b/command.py[m
[36m@@ -1,8 +1,9 @@[m
[31m-# This file contains the Command class.[m
[32m+[m[32m"""This file contains the Command class"""[m
 [m
 class Command:[m
     """[m
[31m-    This class represents a command. A command is composed of a command word, a help string, an action and a number of parameters.[m
[32m+[m[32m    This class represents a command.[m[41m [m
[32m+[m[32m    A command is composed of a command word, a help string, an action and a number of parameters.[m
 [m
     Attributes:[m
         command_word (str): The command word.[m
[36m@@ -16,8 +17,8 @@[m [mclass Command:[m
 [m
     Examples:[m
 [m
[31m-    >>> from actions import go[m
[31m-    >>> command = Command("go", "Permet de se déplacer dans une direction.", go, 1)[m
[32m+[m[32m    >>> from actions import Actions[m
[32m+[m[32m    >>> command = Command("go", "Permet de se déplacer dans une direction.", Actions.go, 1)[m
     >>> command.command_word[m
     'go'[m
     >>> command.help_string[m
[36m@@ -35,12 +36,8 @@[m [mclass Command:[m
         self.help_string = help_string[m
         self.action = action[m
         self.number_of_parameters = number_of_parameters[m
[31m-    [m
[32m+[m
     # The string representation of the command.[m
     def __str__(self):[m
         return  self.command_word \[m
                 + self.help_string[m
[31m-                [m
[31m-    [m
[31m-[m
[31m-[m
